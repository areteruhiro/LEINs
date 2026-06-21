const searchInput = document.querySelector("#category-search");
const cards = [...document.querySelectorAll(".category-card")];
const emptyMessage = document.querySelector("#empty-message");
const styleTabs = [...document.querySelectorAll("[data-style-tab]")];
const stylePanels = [...document.querySelectorAll("[data-style-panel]")];

function normalize(value) {
  return value.trim().toLowerCase();
}

searchInput?.addEventListener("input", () => {
  const query = normalize(searchInput.value);
  let visibleCount = 0;

  cards.forEach((card) => {
    const target = normalize(`${card.textContent} ${card.dataset.keywords || ""}`);
    const visible = query === "" || target.includes(query);
    card.hidden = !visible;
    if (visible) visibleCount += 1;
  });

  emptyMessage.hidden = visibleCount !== 0;
});

function setStylePanel(style) {
  styleTabs.forEach((tab) => {
    tab.classList.toggle("is-active", tab.dataset.styleTab === style);
  });

  stylePanels.forEach((panel) => {
    panel.classList.toggle("is-visible", panel.dataset.stylePanel === style);
  });
}

styleTabs.forEach((tab) => {
  tab.addEventListener("click", () => setStylePanel(tab.dataset.styleTab));
});

setStylePanel("standard");
