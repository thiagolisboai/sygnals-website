"""Generate the 4 legal HTML pages from the approved markdown in legal/.
Single source of truth = legal/*.md. Re-run after editing the markdown."""
import re
import unicodedata

BASE = "https://www.sygnals.in"


def slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    return re.sub(r"[\s]+", "-", s)


def inline(t: str) -> str:
    t = (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    return t


def md_body(md: str) -> str:
    """Convert the clause body (after the front-matter) to HTML. Skips the TOC."""
    # drop everything up to and including the first '---' (front matter), and a
    # '## Sumário'/'## Summary' TOC block up to its trailing '---'.
    parts = md.split("\n---\n")
    # parts[0]=front matter, parts[1]=TOC (Sumário/Summary), rest=clauses
    clause_md = "\n---\n".join(parts[2:]) if len(parts) > 2 else md
    out, i, lines = [], 0, clause_md.split("\n")
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln or ln == "---":
            i += 1
            continue
        if ln.startswith("## "):
            h = ln[3:].strip()
            out.append(f'<h2 id="{slug(h)}">{inline(h)}</h2>')
        elif ln.startswith("### "):
            out.append(f"<h3>{inline(ln[4:].strip())}</h3>")
        elif ln.startswith("- "):
            items = []
            while i < len(lines) and lines[i].lstrip().startswith("- "):
                items.append(f"<li>{inline(lines[i].lstrip()[2:].strip())}</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue
        else:
            out.append(f"<p>{inline(ln)}</p>")
        i += 1
    return "\n    ".join(out)


def front(md: str):
    title = re.search(r"^#\s+(.+)$", md, re.M).group(1).strip()
    ver = re.search(r"\*\*Vers[ãa]o:\*\*\s*(.+)|\*\*Version:\*\*\s*(.+)", md)
    upd = re.search(r"\*\*(?:Última atualização|Last updated):\*\*\s*(.+)", md)
    v = next((g for g in (ver.groups() if ver else []) if g), "1.0")
    return title, v.strip(), (upd.group(1).strip() if upd else "")


TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-JYTJ1MH0CV"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-JYTJ1MH0CV');</script>
  <title>{title} — Sygnals</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{title} — Sygnals">
  <meta property="og:image" content="https://www.sygnals.in/og.png">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 44 44'%3E%3Crect width='44' height='44' rx='10' fill='%230b0b0b'/%3E%3Cg transform='translate(3 6) scale(0.84)'%3E%3Cpath d='M2 20 H14 L18 8 L23 32 L28 20 H42' fill='none' stroke='%2300d4f5' stroke-width='3.8'/%3E%3Ccircle cx='18' cy='5.5' r='3.8' fill='%2300d4f5'/%3E%3C/g%3E%3C/svg%3E">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
  <style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#050505;color:#edf2f5;font-family:'Plus Jakarta Sans',system-ui,sans-serif;line-height:1.65;-webkit-font-smoothing:antialiased}}
a{{color:#00d4f5;text-decoration:none}}a:hover{{text-decoration:underline}}
.top{{border-bottom:1px dashed #2a2a2a}}
.top .in{{max-width:720px;margin:0 auto;padding:20px 24px;display:flex;align-items:center;justify-content:space-between}}
.back{{font-family:'JetBrains Mono',monospace;font-size:13px;color:#9f9f9f}}
.wrap{{max-width:720px;margin:0 auto;padding:48px 24px 110px}}
h1{{font-family:'Outfit',sans-serif;font-weight:800;font-size:clamp(30px,5vw,40px);letter-spacing:-.03em;margin-bottom:10px}}
.updated{{font-family:'JetBrains Mono',monospace;font-size:12px;color:#7e7e7e;margin-bottom:8px;text-transform:uppercase;letter-spacing:.06em}}
h2{{font-family:'Outfit',sans-serif;font-weight:700;font-size:20px;letter-spacing:-.02em;margin:38px 0 12px;scroll-margin-top:20px}}
h3{{font-family:'Outfit',sans-serif;font-weight:600;font-size:16px;margin:22px 0 10px;color:#dfe4e8}}
p{{color:#b8bcc0;font-size:15px;margin-bottom:14px}}
ul{{margin:0 0 14px 20px}}li{{color:#b8bcc0;font-size:15px;margin-bottom:8px}}
strong{{color:#edf2f5;font-weight:600}}
.foot{{max-width:720px;margin:0 auto;padding:0 24px 60px;font-size:13px;color:#7e7e7e;font-family:'JetBrains Mono',monospace}}
  </style>
</head>
<body>
  <div class="top"><div class="in">
    <a href="/" aria-label="Sygnals home"><svg viewBox="0 0 172 40" style="height:22px" fill="none"><path d="M 2 20 L 14 20 L 18 8 L 23 32 L 28 20 L 42 20" stroke="#00d4f5" stroke-width="3.2"/><circle cx="18" cy="5.5" r="3.6" fill="#00d4f5"/><text x="50" y="20" font-family="'Outfit',sans-serif" font-weight="700" font-size="30" letter-spacing="-1.35" dominant-baseline="middle"><tspan fill="#edf2f5">s</tspan><tspan fill="#00d4f5">y</tspan><tspan fill="#edf2f5">gnals</tspan></text></svg></a>
    <a class="back" href="/">{back}</a>
  </div></div>
  <main class="wrap">
    <div class="updated">{updated_label}</div>
    <h1>{h1}</h1>
    {body}
  </main>
  <div class="foot">{foot}</div>
</body>
</html>
"""

PAGES = [
    dict(src="legal/sygnals-terms-of-service-EN.md", out="terms/index.html", lang="en",
         desc="The terms that govern your use of Sygnals.", canonical=f"{BASE}/terms",
         back="← Back to site", ulabel="Version {v} · Updated {u}",
         foot='English · <a href="/pt-br/termos/">Português</a> · <a href="/privacy/">Privacy Policy</a>'),
    dict(src="legal/sygnals-privacy-policy-EN.md", out="privacy/index.html", lang="en",
         desc="How Sygnals handles personal data.", canonical=f"{BASE}/privacy",
         back="← Back to site", ulabel="Version {v} · Updated {u}",
         foot='English · <a href="/pt-br/privacidade/">Português</a> · <a href="/terms/">Terms of Service</a>'),
    dict(src="legal/sygnals-termos-de-servico-PT-BR.md", out="pt-br/termos/index.html", lang="pt-BR",
         desc="Os termos que regem o uso do Sygnals.", canonical=f"{BASE}/pt-br/termos",
         back="← Voltar ao site", ulabel="Versão {v} · Atualizado {u}",
         foot='<a href="/terms/">English</a> · Português · <a href="/pt-br/privacidade/">Privacidade</a>'),
    dict(src="legal/sygnals-politica-de-privacidade-PT-BR.md", out="pt-br/privacidade/index.html", lang="pt-BR",
         desc="Como o Sygnals trata dados pessoais.", canonical=f"{BASE}/pt-br/privacidade",
         back="← Voltar ao site", ulabel="Versão {v} · Atualizado {u}",
         foot='<a href="/privacy/">English</a> · Português · <a href="/pt-br/termos/">Termos</a>'),
]

for p in PAGES:
    md = open(p["src"], encoding="utf-8").read()
    title, v, u = front(md)
    body = md_body(md)
    # Rewrite the docs' /legal/* cross-links to the real per-locale page URLs.
    if p["lang"] == "pt-BR":
        body = body.replace('href="/legal/terms"', 'href="/pt-br/termos/"').replace('href="/legal/privacy"', 'href="/pt-br/privacidade/"')
    else:
        body = body.replace('href="/legal/terms"', 'href="/terms/"').replace('href="/legal/privacy"', 'href="/privacy/"')
    html = TEMPLATE.format(
        lang=p["lang"], title=title, desc=p["desc"], canonical=p["canonical"],
        back=p["back"], updated_label=p["ulabel"].format(v=v, u=u), h1=title,
        body=body, foot=p["foot"],
    )
    open(p["out"], "w", encoding="utf-8").write(html)
    print(f"wrote {p['out']} ({len(html)} bytes)")
