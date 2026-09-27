#!/usr/bin/env python3
"""Static site generator for the 3D Printer Troubleshooting Guide."""
import json
import os
import re
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(ROOT, "content")
DOCS = os.path.join(ROOT, "docs")
STATIC = os.path.join(ROOT, "static")

SITE_TITLE = "3D Printer Troubleshooting Guide"
TAGLINE = "Fix any failed print. Built around the Sovol SV01, useful for any FDM printer."


# ---------------- Markdown ----------------

def parse_frontmatter(text):
    meta = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm = text[3:end].strip()
            text = text[end + 4:].lstrip("\n")
            for line in fm.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, text


def inline_md(s):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+?)`", r"<code>\1</code>", s)
    s = re.sub(r"\[([^\]]+?)\]\(([^)]+?)\)", r'<a href="\2">\1</a>', s)
    return s


def md_to_html(text):
    lines = text.split("\n")
    html = []
    i = 0
    in_code = False
    code_buf = []

    def close_lists():
        pass

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            if in_code:
                html.append("<pre><code>" + "\n".join(
                    c.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                    for c in code_buf) + "</code></pre>")
                code_buf = []
                in_code = False
            else:
                in_code = True
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue

        if not stripped:
            i += 1
            continue
        if stripped == "---":
            html.append("<hr>")
            i += 1
            continue
        m = re.match(r"^(#{1,3})\s+(.*)", stripped)
        if m:
            level = len(m.group(1))
            html.append(f"<h{level}>{inline_md(m.group(2))}</h{level}>")
            i += 1
            continue
        if stripped.startswith("|") and stripped.endswith("|"):
            # table
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            # drop separator row
            rows = [r for r in rows if not all(re.match(r"^:?-{2,}:?$", c) for c in r)]
            out = ["<div class='table-wrap'><table>"]
            for ri, r in enumerate(rows):
                tag = "th" if ri == 0 else "td"
                out.append("<tr>" + "".join(f"<{tag}>{inline_md(c)}</{tag}>" for c in r) + "</tr>")
            out.append("</table></div>")
            html.append("\n".join(out))
            continue
        if re.match(r"^(\d+)\.\s+", stripped):
            items = []
            while i < len(lines) and re.match(r"^(\d+)\.\s+", lines[i].strip()):
                items.append(re.sub(r"^\d+\.\s+", "", lines[i].strip()))
                i += 1
            html.append("<ol>" + "".join(f"<li>{inline_md(x)}</li>" for x in items) + "</ol>")
            continue
        if re.match(r"^[-*]\s+", stripped):
            items = []
            while i < len(lines) and re.match(r"^[-*]\s+", lines[i].strip()):
                items.append(re.sub(r"^[-*]\s+", "", lines[i].strip()))
                i += 1
            html.append("<ul>" + "".join(f"<li>{inline_md(x)}</li>" for x in items) + "</ul>")
            continue
        if stripped.startswith("&gt;") or line.lstrip().startswith(">"):
            q = re.sub(r"^&gt;\s?", "", inline_md(stripped)).lstrip("> ")
            html.append(f"<blockquote>{inline_md(line.lstrip()[1:].strip())}</blockquote>")
            i += 1
            continue
        # paragraph: gather consecutive non-blank lines
        para = [stripped]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(
                r"^(#{1,3}\s+|[-*]\s+|\d+\.\s+|\||```|---$|>)", lines[i].strip()):
            para.append(lines[i].strip())
            i += 1
        html.append("<p>" + inline_md(" ".join(para)) + "</p>")

    return "\n".join(html)


# ---------------- Templates ----------------

BASE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page_title}</title>
<meta name="description" content="{meta_desc}">
<link rel="stylesheet" href="{root}style.css">
</head>
<body>
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="{root}index.html">&#x1F5A8;&#xFE0F; Print Fix Guide</a>
    <nav class="main-nav">
      <a href="{root}index.html#diagnose">Diagnose</a>
      <a href="{root}setup.html">Setup</a>
      <a href="{root}filament.html">Filament</a>
      <a href="{root}maintenance.html">Maintenance</a>
      <a href="{root}upgrades.html">Upgrades</a>
    </nav>
    <div class="search-wrap">
      <input id="site-search" type="search" placeholder="Search symptoms, e.g. &quot;spaghetti&quot;&hellip;" autocomplete="off" aria-label="Search the guide">
      <div id="search-results" class="search-results" hidden></div>
    </div>
  </div>
</header>
<main class="content">
{content}
</main>
<footer class="site-footer">
  <p>Built for the Sovol SV01 &mdash; applies to most FDM printers. <a href="{root}sources.html">Sources &amp; credits</a></p>
  <p class="disclaimer">Community knowledge, not manufacturer advice. When in doubt, check your printer's manual. Never leave a malfunctioning printer unattended.</p>
</footer>
<script>const SEARCH_ROOT = "{root}";</script>
<script src="{root}search.js"></script>
</body>
</html>
"""

ISSUE_BODY = """
<nav class="crumbs"><a href="{root}index.html">Guide</a> &rsaquo; <a href="{root}index.html#{cat_anchor}">{category}</a> &rsaquo; {title}</nav>
<h1>{title}</h1>
<div class="meta-row"><span class="badge">{category}</span> <span class="badge hw">{hw_sw}</span></div>
<aside class="callout"><strong>&#9889; Check this first:</strong> {check_first}</aside>
<h2>What it looks like</h2>
{looks_like}
<h2>Causes, most likely first</h2>
{causes}
<h2>Fixes, in the order to try them</h2>
{fixes}
<h2 class="related-h">Related issues</h2>
<ul class="related">{related}</ul>
"""

ARTICLE_BODY = """
<nav class="crumbs"><a href="{root}index.html">Guide</a> &rsaquo; {title}</nav>
<h1>{title}</h1>
<p class="lede">{description}</p>
{content}
"""


def render_issue(meta, body_html, root, related):
    return BASE.format(
        page_title=f"{meta['title']} | {SITE_TITLE}",
        meta_desc=meta.get("keywords", meta["title"])[:160],
        root=root,
        content=ISSUE_BODY.format(
            root=root,
            cat_anchor="cat-" + re.sub(r"[^a-z0-9]+", "-", meta["category"].lower()).strip("-"),
            category=meta["category"],
            title=meta["title"],
            hw_sw=meta.get("hw_sw", "Both"),
            check_first=inline_md(meta.get("check_first", "")),
            looks_like=body_html["looks_like"],
            causes=body_html["causes"],
            fixes=body_html["fixes"],
            related=related,
        ),
    )


# ---------------- Build ----------------

CATEGORIES = [
    "First Layer & Bed Adhesion",
    "Extrusion Problems",
    "Surface Quality",
    "Strength & Structure",
    "Printer Errors",
]

CATEGORY_BLURBS = {
    "First Layer & Bed Adhesion": "Nothing sticks, or the bottom of the print looks wrong. 80% of all print failures start here.",
    "Extrusion Problems": "Clicking, grinding, jams, gaps, or plastic not coming out right.",
    "Surface Quality": "The print finishes but the outside looks rough, stringy, or scarred.",
    "Strength & Structure": "Layers shift, split, or the part is weak and breaks.",
    "Printer Errors": "The printer itself halts, beeps, or throws temperature errors.",
}

DIAGNOSE_FLOWS = [
    ("It won't stick / the first layer fails",
     "Start here if the print never gets going, or the bottom looks wrong.",
     "First Layer & Bed Adhesion"),
    ("Plastic isn't coming out right",
     "Clicking, grinding, clogs, gaps in walls, or extrusion stopping mid-print.",
     "Extrusion Problems"),
    ("It finished but looks bad",
     "Strings, blobs, rough surfaces, scars, or visible layer lines.",
     "Surface Quality"),
    ("It's weak or falls apart",
     "Layer shifts, splitting, brittle parts, bad bridges or overhangs.",
     "Strength & Structure"),
    ("The printer shows an error / halts",
     "Thermal runaway, heating failures, and other firmware halts.",
     "Printer Errors"),
]


def section_html(md_text, heading):
    """Extract the HTML under a ## heading from a markdown doc."""
    pattern = re.compile(r"^##\s+" + re.escape(heading) + r"\s*$", re.MULTILINE)
    m = pattern.search(md_text)
    if not m:
        return ""
    rest = md_text[m.end():]
    m2 = re.search(r"^##\s+", rest, re.MULTILINE)
    if m2:
        rest = rest[:m2.start()]
    return md_to_html(rest.strip())


def main():
    if os.path.exists(DOCS):
        shutil.rmtree(DOCS)
    os.makedirs(DOCS)
    os.makedirs(os.path.join(DOCS, "issues"))

    issues = []
    idir = os.path.join(CONTENT, "issues")
    for fn in sorted(os.listdir(idir)):
        if not fn.endswith(".md"):
            continue
        slug = fn[:-3]
        with open(os.path.join(idir, fn), encoding="utf-8") as f:
            raw = f.read()
        meta, body = parse_frontmatter(raw)
        meta.setdefault("title", slug.replace("-", " ").title())
        meta.setdefault("category", "Extrusion Problems")
        issues.append({"slug": slug, "meta": meta, "body": body})

    articles = []
    adir = os.path.join(CONTENT, "articles")
    for fn in sorted(os.listdir(adir)):
        if not fn.endswith(".md"):
            continue
        slug = fn[:-3]
        with open(os.path.join(adir, fn), encoding="utf-8") as f:
            raw = f.read()
        meta, body = parse_frontmatter(raw)
        articles.append({"slug": slug, "meta": meta, "html": md_to_html(body)})

    # ---- issue pages ----
    for iss in issues:
        meta, body, slug = iss["meta"], iss["body"], iss["slug"]
        looks = section_html(body, "What it looks like")
        causes = section_html(body, "Causes")
        fixes = section_html(body, "Fixes")
        related = "".join(
            f'<li><a href="{o["slug"]}.html">{o["meta"]["title"]}</a></li>'
            for o in issues
            if o["slug"] != slug and o["meta"]["category"] == meta["category"]
        ) or "<li>None in this category yet.</li>"
        page = render_issue(meta, {"looks_like": looks, "causes": causes, "fixes": fixes},
                            "../", related)
        with open(os.path.join(DOCS, "issues", slug + ".html"), "w", encoding="utf-8") as f:
            f.write(page)

    # ---- article pages ----
    art_titles = {}
    for art in articles:
        meta, slug = art["meta"], art["slug"]
        art_titles[slug] = meta.get("title", slug)
        page = BASE.format(
            page_title=f"{meta.get('title', slug)} | {SITE_TITLE}",
            meta_desc=meta.get("description", "")[:160],
            root="",
            content=ARTICLE_BODY.format(root="", title=meta.get("title", slug),
                                        description=meta.get("description", ""),
                                        content=art["html"]),
        )
        with open(os.path.join(DOCS, slug + ".html"), "w", encoding="utf-8") as f:
            f.write(page)

    # ---- home page ----
    cat_sections = []
    for cat in CATEGORIES:
        anchor = "cat-" + re.sub(r"[^a-z0-9]+", "-", cat.lower()).strip("-")
        cards = "".join(
            f'<a class="issue-card" href="issues/{i["slug"]}.html">'
            f'<span class="issue-title">{i["meta"]["title"]}</span>'
            f'<span class="issue-kw">{i["meta"].get("keywords", "")}</span></a>'
            for i in issues if i["meta"]["category"] == cat
        )
        cat_sections.append(
            f'<section class="cat-section" id="{anchor}">'
            f'<h2>{cat}</h2><p class="cat-blurb">{CATEGORY_BLURBS[cat]}</p>'
            f'<div class="issue-grid">{cards}</div></section>'
        )

    diag_cards = "".join(
        f'<a class="diag-card" href="#cat-{re.sub(r"[^a-z0-9]+", "-", cat.lower()).strip("-")}">'
        f'<strong>{title}</strong><span>{blurb}</span></a>'
        for title, blurb, cat in DIAGNOSE_FLOWS
    )

    home_content = f"""
<section class="hero">
  <h1>{SITE_TITLE}</h1>
  <p class="tagline">{TAGLINE}</p>
  <div class="hero-search">
    <input id="hero-search" type="search" placeholder="Describe your problem: &quot;spaghetti&quot;, &quot;stringing&quot;, &quot;won't stick&quot;&hellip;" autocomplete="off" aria-label="Search the guide">
    <div id="hero-results" class="search-results" hidden></div>
  </div>
  <p class="hero-hint">{len(issues)} issues covered &middot; symptom-first &middot; works offline once loaded</p>
</section>
<section id="diagnose" class="diag-section">
  <h2>Diagnose by symptom</h2>
  <p>Pick what best matches. You'll land on the right category.</p>
  <div class="diag-grid">{diag_cards}</div>
</section>
<section class="start-here">
  <h2>New to 3D printing? Start here</h2>
  <div class="link-cards">
    <a href="setup.html"><strong>Setup &amp; calibration</strong><span>Unbox to first perfect print: leveling, Z-offset, e-steps, PID, retraction.</span></a>
    <a href="filament.html"><strong>Filament guide</strong><span>PLA, PETG, ABS/ASA, TPU: temps, storage, drying.</span></a>
    <a href="maintenance.html"><strong>Maintenance schedule</strong><span>Daily, weekly, monthly checklists.</span></a>
    <a href="upgrades.html"><strong>SV01 upgrades</strong><span>What's worth it, what to skip.</span></a>
  </div>
</section>
{''.join(cat_sections)}
<section class="sv01-box">
  <h2>Your printer: Sovol SV01</h2>
  <ul>
    <li><strong>Build volume:</strong> 280 &times; 240 &times; 300 mm &middot; <strong>Extruder:</strong> direct drive (Titan-style) &middot; <strong>Bed:</strong> heated glass, manual 4-knob leveling</li>
    <li><strong>Max temps:</strong> 250&deg;C nozzle / 100&deg;C bed &middot; <strong>Board:</strong> Creality 2.2 (8-bit) &middot; <strong>Firmware:</strong> Marlin</li>
    <li><strong>Extras:</strong> dual Z lead screws, filament runout sensor, power-loss resume, thermal runaway protection enabled</li>
  </ul>
  <p>Direct drive means short retractions (around 1&ndash;2 mm) and easy TPU printing. Manual leveling means the paper method is your best friend &mdash; see <a href="setup.html">Setup &amp; calibration</a>.</p>
</section>
"""
    home = BASE.format(page_title=SITE_TITLE + " | Fix any failed print",
                       meta_desc=TAGLINE, root="",
                       content=home_content)
    with open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8") as f:
        f.write(home)

    # ---- search index ----
    index = []
    for i in issues:
        m = i["meta"]
        excerpt = re.sub(r"\s+", " ",
                         section_html(i["body"], "What it looks like"))
        excerpt = re.sub(r"<[^>]+>", "", excerpt)[:220]
        index.append({"title": m["title"], "url": "issues/" + i["slug"] + ".html",
                      "category": m["category"], "keywords": m.get("keywords", ""),
                      "excerpt": excerpt})
    for a in articles:
        m = a["meta"]
        text = re.sub(r"<[^>]+>", "", a["html"])
        text = re.sub(r"\s+", " ", text)[:4000]
        index.append({"title": m.get("title", a["slug"]), "url": a["slug"] + ".html",
                      "category": "Guide", "keywords": m.get("description", ""),
                      "excerpt": m.get("description", ""), "body": text})
    with open(os.path.join(DOCS, "search.json"), "w", encoding="utf-8") as f:
        json.dump(index, f)

    # ---- static ----
    for fn in ("style.css", "search.js"):
        shutil.copy(os.path.join(STATIC, fn), os.path.join(DOCS, fn))

    print(f"Built {len(issues)} issues + {len(articles)} articles -> {DOCS}")


if __name__ == "__main__":
    main()
