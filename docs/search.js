/* Instant client-side search over search.json */
(function () {
  var index = null;
  var loading = null;

  function loadIndex() {
    if (index) return Promise.resolve(index);
    if (loading) return loading;
    loading = fetch(SEARCH_ROOT + "search.json")
      .then(function (r) { return r.json(); })
      .then(function (data) { index = data; return index; })
      .catch(function () { return []; });
    return loading;
  }

  function score(entry, q) {
    var t = (entry.title + " " + entry.keywords + " " + entry.category).toLowerCase();
    var words = q.toLowerCase().split(/\s+/).filter(Boolean);
    var s = 0;
    for (var i = 0; i < words.length; i++) {
      var w = words[i];
      if (entry.title.toLowerCase().indexOf(w) !== -1) s += 5;
      else if ((entry.keywords || "").toLowerCase().indexOf(w) !== -1) s += 3;
      else if (t.indexOf(w) !== -1) s += 1;
      else if (entry.body && entry.body.toLowerCase().indexOf(w) !== -1) s += 0.5;
      else return 0;
    }
    return s;
  }

  function render(box, results, q) {
    box.innerHTML = "";
    if (!q) { box.hidden = true; return; }
    if (!results.length) {
      box.innerHTML = '<div class="sr-empty">No matches. Try fewer or different words, e.g. "stick", "string", "shift".</div>';
      box.hidden = false;
      return;
    }
    results.slice(0, 12).forEach(function (r) {
      var a = document.createElement("a");
      a.href = SEARCH_ROOT + r.url;
      var cat = document.createElement("span");
      cat.className = "sr-cat";
      cat.textContent = r.category;
      var title = document.createElement("span");
      title.className = "sr-title";
      title.textContent = r.title;
      var ex = document.createElement("span");
      ex.className = "sr-ex";
      ex.textContent = r.excerpt || "";
      a.appendChild(cat);
      a.appendChild(title);
      a.appendChild(ex);
      box.appendChild(a);
    });
    box.hidden = false;
  }

  function attach(inputId, boxId) {
    var input = document.getElementById(inputId);
    var box = document.getElementById(boxId);
    if (!input || !box) return;
    var t = null;
    input.addEventListener("input", function () {
      clearTimeout(t);
      t = setTimeout(function () {
        var q = input.value.trim();
        if (q.length < 2) { box.hidden = true; return; }
        loadIndex().then(function (idx) {
          var scored = [];
          for (var i = 0; i < idx.length; i++) {
            var s = score(idx[i], q);
            if (s > 0) scored.push({ e: idx[i], s: s });
          }
          scored.sort(function (a, b) { return b.s - a.s; });
          render(box, scored.map(function (x) { return x.e; }), q);
        });
      }, 120);
    });
    document.addEventListener("click", function (e) {
      if (!box.contains(e.target) && e.target !== input) box.hidden = true;
    });
    input.addEventListener("keydown", function (e) {
      if (e.key === "Escape") box.hidden = true;
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    attach("site-search", "search-results");
    attach("hero-search", "hero-results");
  });
})();

/* hamburger drawer + auto-hide header (same pattern as Trending Reality Check) */
(function () {
  var menuBtn = document.getElementById("menuBtn"),
      drawer = document.getElementById("drawer"),
      scrim = document.getElementById("scrim");
  function setMenu(open) {
    menuBtn.classList.toggle("open", open);
    drawer.classList.toggle("open", open);
    scrim.classList.toggle("show", open);
  }
  menuBtn.addEventListener("click", function () { setMenu(!drawer.classList.contains("open")); });
  scrim.addEventListener("click", function () { setMenu(false); });
  drawer.querySelectorAll("a").forEach(function (a) {
    a.addEventListener("click", function () { setMenu(false); });
  });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });

  var lastY = window.scrollY, hdr = document.querySelector(".site-header");
  window.addEventListener("scroll", function () {
    var y = window.scrollY;
    if (y > lastY + 4 && y > 140) { hdr.classList.add("hide"); }
    else if (y < lastY - 4) { hdr.classList.remove("hide"); }
    lastY = y;
  }, { passive: true });
})();
