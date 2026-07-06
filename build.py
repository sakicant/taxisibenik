"""Static site build script.

Each page lives in src/pages/<page-id>/<lang>/ as a meta.json + content.html
pair. <page-id> groups the translations of one logical page together (e.g.
"about"); <lang> is an ISO 639-1 code such as "en", "hr", "de", "pl", "cs",
"it", "fr", "nl". English is the canonical language and is served at the
site root (e.g. /about/); every other language is served under its own
language prefix (e.g. /hr/o-meni/).

For every page-id, the build script automatically generates a reciprocal
set of hreflang alternate links across all language variants that exist for
that page, plus an x-default pointing at the English version. This is safe
to run at any point: a page-id with only an "en" folder just gets a single
self-referencing hreflang tag until more languages are added alongside it.

Run `python build.py` after editing any partial or page content.
"""
import hashlib
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
PAGES_DIR = os.path.join(SRC, "pages")
PARTIALS_DIR = os.path.join(SRC, "partials")

SITE_URL = "https://taxisibenik.hr"
DEFAULT_OG_IMAGE = f"{SITE_URL}/assets/img/hero-bg.webp"
DEFAULT_LANG = "en"

# Supported languages. Codes must be valid ISO 639-1 for correct hreflang.
LANGUAGES = ["en", "hr", "de", "pl", "cs", "it", "fr", "nl"]


def compute_asset_version():
    """Short hash of styles.css + script.js so browsers fetch fresh copies
    whenever either file changes, instead of serving a stale cached copy."""
    hasher = hashlib.md5()
    for name in ("styles.css", "script.js"):
        with open(os.path.join(ROOT, name), "rb") as f:
            hasher.update(f.read())
    return hasher.hexdigest()[:10]


ASSET_VERSION = compute_asset_version()


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def canonical_url(lang, slug):
    if lang == DEFAULT_LANG:
        path = f"{slug}/" if slug else ""
    else:
        path = f"{lang}/{slug}/" if slug else f"{lang}/"
    return f"{SITE_URL}/{path}"


def output_path(lang, slug):
    if lang == DEFAULT_LANG:
        rel = os.path.join(slug, "index.html") if slug else "index.html"
    else:
        rel = os.path.join(lang, slug, "index.html") if slug else os.path.join(lang, "index.html")
    return os.path.join(ROOT, rel)


def discover_pages():
    """Returns {page_id: {lang: meta_dict}} for every page-id/lang combo found."""
    pages = {}
    for page_id in sorted(os.listdir(PAGES_DIR)):
        page_dir = os.path.join(PAGES_DIR, page_id)
        if not os.path.isdir(page_dir):
            continue
        variants = {}
        for lang in sorted(os.listdir(page_dir)):
            lang_dir = os.path.join(page_dir, lang)
            meta_path = os.path.join(lang_dir, "meta.json")
            if lang not in LANGUAGES or not os.path.isfile(meta_path):
                continue
            with open(meta_path, "r", encoding="utf-8") as f:
                meta = json.load(f)
            variants[lang] = meta
        if variants:
            pages[page_id] = variants
    return pages


def build_hreflang_block(page_id, variants):
    if DEFAULT_LANG not in variants:
        # No English source for this page-id; skip cross-linking rather
        # than guess at an x-default target.
        links = []
        for lang, meta in variants.items():
            url = canonical_url(lang, meta.get("slug", ""))
            links.append(f'<link rel="alternate" hreflang="{lang}" href="{url}">')
        return "\n".join(links)

    links = []
    for lang, meta in variants.items():
        url = canonical_url(lang, meta.get("slug", ""))
        links.append(f'<link rel="alternate" hreflang="{lang}" href="{url}">')
    default_url = canonical_url(DEFAULT_LANG, variants[DEFAULT_LANG].get("slug", ""))
    links.append(f'<link rel="alternate" hreflang="x-default" href="{default_url}">')
    return "\n".join(links)


LANGUAGE_LABELS = {
    "en": "EN", "hr": "HR", "de": "DE", "pl": "PL",
    "cs": "CS", "it": "IT", "fr": "FR", "nl": "NL",
}

LANGUAGE_FLAGS = {
    "en": "\U0001F1EC\U0001F1E7", "hr": "\U0001F1ED\U0001F1F7",
    "de": "\U0001F1E9\U0001F1EA", "pl": "\U0001F1F5\U0001F1F1",
    "cs": "\U0001F1E8\U0001F1FF", "it": "\U0001F1EE\U0001F1F9",
    "fr": "\U0001F1EB\U0001F1F7", "nl": "\U0001F1F3\U0001F1F1",
}


def build_lang_switcher(variants, current_lang):
    current_flag = LANGUAGE_FLAGS[current_lang]
    current_label = LANGUAGE_LABELS[current_lang]

    items = []
    for lang in LANGUAGES:
        flag = LANGUAGE_FLAGS[lang]
        label = LANGUAGE_LABELS[lang]
        if lang in variants:
            url = canonical_url(lang, variants[lang].get("slug", ""))
            cls = "nav-lang-item active" if lang == current_lang else "nav-lang-item"
            items.append(f'<a href="{url}" class="{cls}">{flag} {label}</a>')
        else:
            items.append(f'<span class="nav-lang-item soon" title="Coming soon">{flag} {label}</span>')
    menu_items = "\n          ".join(items)

    return f'''<div class="nav-dropdown nav-lang-dropdown">
        <button class="nav-dropdown-toggle">{current_flag} {current_label} <span class="caret"></span></button>
        <div class="nav-dropdown-menu">
          {menu_items}
        </div>
      </div>'''


def quote_widget_html():
    global _QUOTE_WIDGET
    if _QUOTE_WIDGET is None:
        _QUOTE_WIDGET = read(os.path.join(PARTIALS_DIR, "quote-widget.html"))
    return _QUOTE_WIDGET


_QUOTE_WIDGET = None


def build_variant(lang, meta, content_path, base_tpl, header_tpl, footer_html, hreflang_block, variants):
    body = read(content_path)
    body = body.replace("{{QUOTE_WIDGET}}", quote_widget_html())
    slug = meta.get("slug", "")
    canonical = canonical_url(lang, slug)
    header_html = header_tpl.replace("{{LANG_SWITCHER}}", build_lang_switcher(variants, lang))

    schema = meta.get("schema")
    schema_list = schema if isinstance(schema, list) else ([schema] if schema else [])
    schema_block = "\n".join(
        '<script type="application/ld+json">\n' + json.dumps(s, indent=2, ensure_ascii=False) + "\n</script>"
        for s in schema_list
    )

    html = base_tpl
    html = html.replace("{{LANG}}", lang)
    html = html.replace("{{TITLE}}", meta["title"])
    html = html.replace("{{DESCRIPTION}}", meta["description"])
    html = html.replace("{{KEYWORDS}}", meta.get("keywords", ""))
    html = html.replace("{{CANONICAL}}", canonical)
    html = html.replace("{{HREFLANGS}}", hreflang_block)
    html = html.replace("{{OG_IMAGE}}", meta.get("og_image", DEFAULT_OG_IMAGE))
    html = html.replace("{{SCHEMA}}", schema_block)
    html = html.replace("{{ASSET_VERSION}}", ASSET_VERSION)
    html = html.replace("{{HEADER}}", header_html)
    html = html.replace("{{FOOTER}}", footer_html)
    html = html.replace("{{BODY}}", body)

    out_path = output_path(lang, slug)
    write(out_path, html)
    rel = os.path.relpath(out_path, ROOT)
    print(f"built {rel}")


def main():
    base_tpl = read(os.path.join(PARTIALS_DIR, "base.html"))
    header_tpl = read(os.path.join(PARTIALS_DIR, "header.html"))
    footer_html = read(os.path.join(PARTIALS_DIR, "footer.html"))

    pages = discover_pages()

    for page_id, variants in pages.items():
        hreflang_block = build_hreflang_block(page_id, variants)
        for lang, meta in variants.items():
            content_path = os.path.join(PAGES_DIR, page_id, lang, "content.html")
            build_variant(lang, meta, content_path, base_tpl, header_tpl, footer_html, hreflang_block, variants)


if __name__ == "__main__":
    main()
