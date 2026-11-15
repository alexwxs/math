(() => {
  const panel = document.getElementById("toc-panel");
  const toggle = document.querySelector(".toc-toggle");

  function setTocOpen(open) {
    document.body.classList.toggle("toc-open", open);
    if (toggle) toggle.setAttribute("aria-expanded", open ? "true" : "false");
  }

  toggle?.addEventListener("click", () => {
    setTocOpen(!document.body.classList.contains("toc-open"));
  });

  // Close mobile TOC after navigating
  panel?.querySelectorAll('a[href^="#"]').forEach((a) => {
    a.addEventListener("click", () => {
      if (window.matchMedia("(max-width: 960px)").matches) setTocOpen(false);
    });
  });

  // Update summary hint text when open/closed
  function syncHint(details) {
    const hint = details.querySelector(".solution-hint");
    if (!hint) return;
    hint.textContent = details.open ? "Hide" : "Show";
  }

  document.querySelectorAll("details.solution-block").forEach((d) => {
    syncHint(d);
    d.addEventListener("toggle", () => syncHint(d));
  });

  document.querySelectorAll("[data-action='expand-all']").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll("details.solution-block").forEach((d) => {
        d.open = true;
        syncHint(d);
      });
    });
  });

  document.querySelectorAll("[data-action='collapse-all']").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll("details.solution-block").forEach((d) => {
        d.open = false;
        syncHint(d);
      });
    });
  });

  // Highlight TOC link for the section in view
  const targets = [...document.querySelectorAll("h1.section[id], h2.question[id]")];
  if (!("IntersectionObserver" in window) || !targets.length) return;

  const linkById = new Map(
    [...document.querySelectorAll('.toc a[href^="#"]')].map((a) => [
      a.getAttribute("href").slice(1),
      a,
    ])
  );

  const observer = new IntersectionObserver(
    (entries) => {
      const visible = entries
        .filter((e) => e.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio);
      if (!visible.length) return;
      const id = visible[0].target.id;
      linkById.forEach((a) => a.classList.remove("is-active"));
      linkById.get(id)?.classList.add("is-active");
    },
    { rootMargin: "-20% 0px -65% 0px", threshold: [0, 0.25, 0.5, 1] }
  );

  targets.forEach((el) => observer.observe(el));
})();
