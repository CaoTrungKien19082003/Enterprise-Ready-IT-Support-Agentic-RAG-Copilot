(() => {
  "use strict";

  const KEY = "itcopilot:prefs";
  const ACCENTS = ["green", "blue", "violet", "amber"];
  const root = document.documentElement;
  const media = window.matchMedia("(prefers-color-scheme: light)");

  const load = () => {
    try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch { return {}; }
  };
  const save = () => {
    try { localStorage.setItem(KEY, JSON.stringify(prefs)); } catch { /* storage unavailable */ }
  };
  const prefs = load();

  function apply() {
    root.dataset.theme = prefs.theme || (media.matches ? "light" : "dark");
    root.dataset.accent = ACCENTS.includes(prefs.accent) ? prefs.accent : "green";

    const toggle = document.getElementById("themeToggle");
    if (toggle) {
      const next = root.dataset.theme === "dark" ? "light" : "dark";
      toggle.setAttribute("aria-label", `Switch to ${next} mode`);
      toggle.title = `Switch to ${next} mode`;
    }
    document.querySelectorAll(".swatch").forEach((b) =>
      b.setAttribute("aria-checked", String(b.dataset.accent === root.dataset.accent)));
  }

  apply(); // runs from <head>, so the saved theme is set before the first paint
  media.addEventListener("change", () => { if (!prefs.theme) apply(); });

  document.addEventListener("DOMContentLoaded", () => {
    apply();
    const toggle = document.getElementById("themeToggle");
    if (toggle) toggle.addEventListener("click", () => {
      prefs.theme = root.dataset.theme === "dark" ? "light" : "dark";
      save(); apply();
    });
    document.querySelectorAll(".swatch").forEach((b) =>
      b.addEventListener("click", () => { prefs.accent = b.dataset.accent; save(); apply(); }));
  });
})();
