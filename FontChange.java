package io.github.hiro.LEINs.hooks;

import android.content.Context;
import android.graphics.Typeface;
import android.net.Uri;

import androidx.documentfile.provider.DocumentFile;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.lang.reflect.Field;
import java.util.List;

import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.XC_MethodReplacement;
import de.robv.android.xposed.XposedBridge;
import de.robv.android.xposed.XposedHelpers;
import de.robv.android.xposed.callbacks.XC_LoadPackage;
import io.github.hiro.LEINs.Constants;
import io.github.hiro.LEINs.FontRepositoryDetector;
import io.github.hiro.LEINs.LEINsOptions;

public class FontChange implements IHook {

    private static Typeface mLoadedFont = null;
    private static boolean  mFontReady  = false;

    private static final String CLS_FONT_MANAGER  = "k6.m";
    private static final String CLS_FONT_SETTINGS = FontRepositoryDetector.Font_Class.className;

    private static final String MTH_GET_FONT_CONFIG   = "a";
    private static final String MTH_INITIALIZE_FONT   = "b";
    private static final String MTH_GET_FONT_SETTINGS = FontRepositoryDetector.Font_Class.methodName;
    private static final String MTH_ON_FONT_CHANGED   = "b";
    private static final float ASCENT_RATIO  = 0.92f;
    private static final float DESCENT_RATIO = 0.22f;

    private Context mContext;

    @Override
    public void apply(LEINsOptions options, XC_LoadPackage.LoadPackageParam lpp) throws Throwable {
        if (!LEINsOptions.FontChange.checked) return;

        XposedHelpers.findAndHookMethod(
                "android.app.Application",
                lpp.classLoader,
                "onCreate",
                new XC_MethodHook() {
                    @Override
                    protected void afterHookedMethod(MethodHookParam param) throws Throwable {
                        if (mContext != null) return;

                        mContext = (Context) param.thisObject;
                        XposedBridge.log("[LEINs] Application context ready: "
                                + mContext.getPackageName());

                        prepareFontFromStorage();
                        if (!mFontReady || mLoadedFont == null) return;
                        registerAllFontHooks(lpp);
                    }
                });
    }
    private void prepareFontFromStorage() {
        try {
            String rawUri = readStoredUri(mContext);
            if (rawUri == null || rawUri.isEmpty()) {
                XposedBridge.log("[LEINs] フォント URI 未設定");
                mFontReady = false;
                return;
            }

            DocumentFile dir = DocumentFile.fromTreeUri(mContext, Uri.parse(rawUri));
            if (dir == null || !dir.exists()) {
                XposedBridge.log("[LEINs] ディレクトリが見つかりません: " + rawUri);
                mFontReady = false;
                return;
            }

            DocumentFile target = dir.findFile("lein.ttf");
            if (target == null || !target.exists()) {
                XposedBridge.log("[LEINs] lein.ttf が見つかりません: " + dir.getName());
                mFontReady = false;
                return;
            }

            File tmp = extractToCache(target.getUri());
            if (tmp == null) {
                XposedBridge.log("[LEINs] キャッシュへのコピーに失敗しました");
                mFontReady = false;
                return;
            }

            mLoadedFont = Typeface.createFromFile(tmp);
            mFontReady  = (mLoadedFont != null);
            if (mFontReady) XposedBridge.log("[LEINs] フォント読み込み完了 (URI)");

        } catch (Throwable t) {
            XposedBridge.log("[LEINs] フォント初期化エラー: " + t);
            mFontReady = false;
        }
    }

    private String readStoredUri(Context ctx) {
        File f = new File(ctx.getFilesDir(), "LEINsBackup/backup_uri.txt");
        if (!f.exists()) return null;
        try (BufferedReader br = new BufferedReader(new FileReader(f))) {
            return br.readLine();
        } catch (IOException e) {
            XposedBridge.log("[LEINs] URI 読み込みエラー: " + e.getMessage());
            return null;
        }
    }

    private File extractToCache(Uri src) {
        try {
            File dest = new File(mContext.getCacheDir(), "lein.ttf");
            try (InputStream  in  = mContext.getContentResolver().openInputStream(src);
                 OutputStream out = new FileOutputStream(dest)) {
                if (in == null) {
                    XposedBridge.log("[LEINs] InputStream null: " + src);
                    return null;
                }
                byte[] buf = new byte[8192];
                int n;
                while ((n = in.read(buf)) != -1) out.write(buf, 0, n);
            }
            return dest;
        } catch (Throwable t) {
            XposedBridge.log("[LEINs] extractToCache エラー: " + t);
            return null;
        }
    }

    private void registerAllFontHooks(XC_LoadPackage.LoadPackageParam lpp) {
        XposedBridge.log("[LEINs] フォントフック登録開始");
        hookSystemTypeface();
        hookTextViewSetTypeface(lpp);
        hookPaintFontMetrics();
        hookLineFontPipeline(lpp);
    }
    private void hookSystemTypeface() {
        XC_MethodReplacement fontReplacer = new XC_MethodReplacement() {
            @Override
            protected Object replaceHookedMethod(MethodHookParam param) {
                return mLoadedFont;
            }
        };
        XposedHelpers.findAndHookMethod(Typeface.class, "create",
                String.class, int.class, fontReplacer);
        XposedHelpers.findAndHookMethod(Typeface.class, "create",
                Typeface.class, int.class, fontReplacer);
        XposedHelpers.findAndHookMethod(Typeface.class, "defaultFromStyle",
                int.class, fontReplacer);
    }

    private void hookTextViewSetTypeface(XC_LoadPackage.LoadPackageParam lpp) {
        XC_MethodHook setTypefaceHook = new XC_MethodHook() {
            @Override
            protected void beforeHookedMethod(MethodHookParam param) {
                if (!mFontReady || mLoadedFont == null) return;
                if (param.args.length > 0 && param.args[0] instanceof Typeface) {
                    param.args[0] = mLoadedFont;
                }
                clearEditTextPadding(param.thisObject);
            }
        };

        XC_MethodHook constructorHook = new XC_MethodHook() {
            @Override
            protected void afterHookedMethod(MethodHookParam param) {
                if (!mFontReady || mLoadedFont == null) return;
                clearEditTextPadding(param.thisObject);
            }
        };

        try {
            XposedHelpers.findAndHookMethod("android.widget.TextView",
                    lpp.classLoader, "setTypeface",
                    Typeface.class, int.class, setTypefaceHook);
            XposedHelpers.findAndHookMethod("android.widget.TextView",
                    lpp.classLoader, "setTypeface",
                    Typeface.class, setTypefaceHook);

            XposedHelpers.findAndHookConstructor("android.widget.TextView",
                    lpp.classLoader,
                    android.content.Context.class, android.util.AttributeSet.class,
                    constructorHook);
            XposedHelpers.findAndHookConstructor("android.widget.TextView",
                    lpp.classLoader,
                    android.content.Context.class, android.util.AttributeSet.class,
                    int.class, constructorHook);
        } catch (Throwable t) {
            XposedBridge.log("[LEINs] TextView フックエラー: " + t);
        }
    }

    private void clearEditTextPadding(Object view) {
        try {
            if (view instanceof android.widget.EditText) {
                XposedHelpers.callMethod(view, "setPadding", 0, 0, 0, 0);
            }
        } catch (Throwable ignored) {}
    }

    private void hookPaintFontMetrics() {
        XC_MethodHook metricsHook = new XC_MethodHook() {
            @Override
            protected void afterHookedMethod(MethodHookParam param) {
                if (!mFontReady || mLoadedFont == null) return;

                android.graphics.Paint paint = (android.graphics.Paint) param.thisObject;
                Typeface tf = paint.getTypeface();
                if (tf != null && tf != mLoadedFont
                        && !(paint instanceof android.text.TextPaint)) return;

                Object metrics = (param.args.length > 0) ? param.args[0] : param.getResult();
                if (!(metrics instanceof android.graphics.Paint.FontMetricsInt)) return;

                applyMetricsScale(
                        (android.graphics.Paint.FontMetricsInt) metrics,
                        paint.getTextSize());
            }
        };

        try {
            XposedHelpers.findAndHookMethod(android.graphics.Paint.class,
                    "getFontMetricsInt",
                    android.graphics.Paint.FontMetricsInt.class, metricsHook);
            XposedHelpers.findAndHookMethod(android.graphics.Paint.class,
                    "getFontMetricsInt", metricsHook);
        } catch (Throwable t) {
            XposedBridge.log("[LEINs] FontMetrics フックエラー: " + t);
        }
    }

    private static void applyMetricsScale(
            android.graphics.Paint.FontMetricsInt fmi, float sz) {
        if (sz <= 0) return;
        fmi.ascent  = Math.round(-sz * ASCENT_RATIO);
        fmi.descent = Math.round( sz * DESCENT_RATIO);
        fmi.top     = fmi.ascent;
        fmi.bottom  = fmi.descent;
        fmi.leading = 0;
    }

    private void hookLineFontPipeline(XC_LoadPackage.LoadPackageParam lpp) {

        XposedHelpers.findAndHookMethod(
                Constants.CLS_FONT_CONFIG.className, lpp.classLoader,
                MTH_GET_FONT_CONFIG,
                android.content.Context.class, java.util.List.class,
                int.class, boolean.class, int.class,
                android.os.Handler.class, Constants.CLS_FONT_CALLBACK.className,
                new XC_MethodHook() {
                    @Override
                    protected void beforeHookedMethod(MethodHookParam param) {
                        dispatchFontCallback(param.args[6]);
                        param.setResult(mLoadedFont);
                    }
                });

        XposedHelpers.findAndHookMethod(
                Constants.CLS_FONT_CALLBACK.className, lpp.classLoader,
                MTH_ON_FONT_CHANGED, Typeface.class,
                new XC_MethodHook() {
                    @Override
                    protected void beforeHookedMethod(MethodHookParam param) {
                        param.args[0] = mLoadedFont;
                    }
                });

        hookFontManagerByVersion(lpp);
        hookFontSettingsOptional(lpp);
    }

    private void dispatchFontCallback(Object callback) {
        if (callback == null) return;
        try {
            XposedHelpers.callMethod(callback, MTH_ON_FONT_CHANGED, mLoadedFont);
        } catch (Throwable ignored) {}
    }

    private void hookFontManagerByVersion(XC_LoadPackage.LoadPackageParam lpp) {
        if (Constants.versionName.equals("15.12.2")) {
            XposedHelpers.findAndHookMethod(
                    "L2.h", lpp.classLoader, "b",
                    int.class, Context.class, String.class, List.class,
                    new XC_MethodHook() {
                        @Override
                        protected void afterHookedMethod(MethodHookParam param) {
                            injectTypefaceField(param.getResult());
                        }
                    });
        } else {
            XposedHelpers.findAndHookMethod(
                    CLS_FONT_MANAGER, lpp.classLoader, MTH_INITIALIZE_FONT,
                    String.class, android.content.Context.class,
                    java.util.List.class, int.class,
                    new XC_MethodHook() {
                        @Override
                        protected void afterHookedMethod(MethodHookParam param) {
                            injectTypefaceField(param.getResult());
                        }
                    });
        }
    }

    private void injectTypefaceField(Object target) {
        if (target == null) return;
        String fieldName = resolveTypefaceField(target.getClass());
        if (fieldName == null) {
            XposedBridge.log("[LEINs] Typeface フィールドが見つかりません: "
                    + target.getClass().getName());
            return;
        }
        XposedBridge.log("[LEINs] Typeface フィールド検出: " + fieldName);
        XposedHelpers.setObjectField(target, fieldName, mLoadedFont);
    }

    private void hookFontSettingsOptional(XC_LoadPackage.LoadPackageParam lpp) {
        try {
            XposedHelpers.findAndHookMethod(
                    CLS_FONT_SETTINGS, lpp.classLoader, MTH_GET_FONT_SETTINGS,
                    int.class, Constants.SelectedFontRepository_InvokeSuspend.className,
                    new XC_MethodHook() {
                        @Override
                        protected void beforeHookedMethod(MethodHookParam param) {
                            param.setResult(mLoadedFont);
                        }
                    });
        } catch (Throwable t) {
            XposedBridge.log("[LEINs] FontSettings フックをスキップ: " + t);
        }
    }

    private static String resolveTypefaceField(Class<?> cls) {
        for (Class<?> c = cls; c != null && c != Object.class; c = c.getSuperclass()) {
            for (Field f : c.getDeclaredFields()) {
                if (f.getType() == Typeface.class) return f.getName();
            }
        }
        return null;
    }
}
