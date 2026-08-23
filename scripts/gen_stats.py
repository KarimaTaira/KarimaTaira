#!/usr/bin/env python3
"""Generate a themed GitHub stats SVG. No external image services."""
import json, os, sys, urllib.request

USER = os.environ.get("GH_USER", "KarimaTaira")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = os.environ.get("OUT", "assets/stats.svg")

BG="#0B0F17"; PANEL="#111827"; STROKE="#1F2937"
G="#5CF19E"; A="#F2B84B"; M="#6B7A8F"; T="#D3DDE9"
MONO="ui-monospace, 'SF Mono', Menlo, Consolas, monospace"


def api(url):
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": USER,
        **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def collect():
    user = api(f"https://api.github.com/users/{USER}")
    repos, page = [], 1
    while True:
        batch = api(f"https://api.github.com/users/{USER}/repos?per_page=100&page={page}")
        repos += batch
        if len(batch) < 100:
            break
        page += 1
    stars = sum(r.get("stargazers_count", 0) for r in repos)
    langs = {}
    for r in repos:
        if r.get("language"):
            langs[r["language"]] = langs.get(r["language"], 0) + 1
    top = sorted(langs.items(), key=lambda kv: -kv[1])[:5]
    return {
        "repos": user.get("public_repos", 0),
        "followers": user.get("followers", 0),
        "stars": stars,
        "top": top,
    }


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render(d, w=1200, h=250):
    tiles = [
        ("PUBLIC REPOS", d["repos"], G),
        ("TOTAL STARS", d["stars"], A),
        ("FOLLOWERS", d["followers"], G),
    ]
    tx = ""
    for i, (lab, val, col) in enumerate(tiles):
        x = 40 + i * ((w - 80) / 3)
        tw = (w - 80) / 3 - 16
        tx += (
            f'<rect x="{x}" y="72" width="{tw}" height="64" rx="8" fill="{PANEL}" stroke="{STROKE}"/>'
            f'<rect x="{x}" y="72" width="3" height="64" rx="1.5" fill="{col}" opacity="0.85"/>'
            f'<text x="{x+16}" y="95" font-family="{MONO}" font-size="10.5" fill="{M}" letter-spacing="1.5">{lab}</text>'
            f'<text x="{x+16}" y="122" font-family="{MONO}" font-size="23" font-weight="700" fill="{col}">{val}</text>'
        )

    total = sum(c for _, c in d["top"]) or 1
    bar, bx = "", 40
    bw = w - 80
    palette = [G, A, "#7CC4FF", "#C08CFF", "#FF8C8C"]
    legend = ""
    for i, (lang, cnt) in enumerate(d["top"]):
        seg = bw * cnt / total
        col = palette[i % len(palette)]
        bar += f'<rect x="{bx:.1f}" y="172" width="{max(seg-3,2):.1f}" height="12" rx="3" fill="{col}"/>'
        legend += (
            f'<circle cx="{bx+5:.1f}" cy="209" r="4.5" fill="{col}"/>'
            f'<text x="{bx+16:.1f}" y="213" font-family="{MONO}" font-size="11.5" fill="{M}">{esc(lang)}</text>'
        )
        bx += seg
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="{h}">
<rect width="{w}" height="{h}" rx="12" fill="{BG}" stroke="{STROKE}"/>
<text x="40" y="46" font-family="{MONO}" font-size="17" font-weight="700" fill="{G}">$ <tspan fill="{T}">gh api users/{esc(USER)} --stats</tspan></text>
{tx}
<text x="40" y="163" font-family="{MONO}" font-size="10.5" fill="{M}" letter-spacing="1.5">LANGUAGE DISTRIBUTION</text>
{bar}{legend}
</svg>'''


if __name__ == "__main__":
    try:
        data = collect()
    except Exception as e:
        print(f"API fetch failed: {e}", file=sys.stderr)
        sys.exit(1)
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w") as f:
        f.write(render(data))
    print(f"wrote {OUT}: {data}")
