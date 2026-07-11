# Sygnals Marketing Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a single-page, dark, on-brand Sygnals marketing landing page (EN + pt-BR) as self-contained static HTML, converting B2B founders/SMBs into booked demos.

**Architecture:** Two self-contained static files — `index.html` (EN, default) and `pt-br/index.html` (pt-BR) — each with inline `<style>`, inline SVG logo, and minimal vanilla JS. No framework, no build step. A tiny geo-redirect + a footer language toggle (localStorage) route between languages. Local dev via the house Node tooling (`serve.mjs` + `screenshot.mjs`, Puppeteer 24.37.5). Verification is visual: serve locally, screenshot desktop + mobile, inspect.

**Tech Stack:** HTML5, inline CSS (custom properties from brand tokens), vanilla JS (IntersectionObserver reveal, FAQ accordion, sticky nav, count-up), Google Fonts (DM Sans 700 + Inter), Cal.com embed for demo booking, Node 24 + Puppeteer for local preview/screenshots.

**Verification model (replaces unit tests for this static build):** Each build task ends by (a) serving via `node serve.mjs`, (b) screenshotting at desktop (1440) and mobile (390) with `node screenshot.mjs`, (c) confirming the new section renders on-brand with no console errors. "Expected" describes what the screenshot must show.

---

## File Structure

- Create: `index.html` — EN landing page, all 10 sections, inline CSS/JS. Single responsibility: the English marketing page.
- Create: `pt-br/index.html` — pt-BR translation of the same page (structure identical, copy + `lang` + currency note differ).
- Create: `serve.mjs` — static dev server on :3000 with `decodeURIComponent` (house pattern, needed for spaces in paths).
- Create: `screenshot.mjs` — Puppeteer screenshot helper → `./temporary screenshots/`.
- Create: `package.json` — `"type":"module"`, puppeteer 24.37.5 devDependency.
- Create: `vercel.json` — static hosting config + clean routes (no trailingSlash — house lesson: it breaks path rewrites).
- Create: `.gitignore` — `node_modules/`, `temporary screenshots/`, `.superpowers/`.
- Existing: `brand_assets/` — reference only (logo SVG is inlined, not linked).

**Shared design tokens:** the `:root` CSS variable block and the inline SVG logo are authored once in Task 3 and copied verbatim into `pt-br/index.html` in Task 12. They must stay byte-identical between the two files.

---

## Task 1: Project tooling & scaffolding

**Files:**
- Create: `package.json`
- Create: `serve.mjs`
- Create: `screenshot.mjs`
- Create: `.gitignore`

- [ ] **Step 1: Create `package.json`**

```json
{
  "name": "sygnals-website",
  "version": "1.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "node serve.mjs",
    "shot": "node screenshot.mjs"
  },
  "devDependencies": {
    "puppeteer": "24.37.5"
  }
}
```

- [ ] **Step 2: Create `serve.mjs`** (house pattern — MUST `decodeURIComponent` for paths with spaces)

```js
import { createServer } from 'http';
import { readFile } from 'fs/promises';
import { extname, join } from 'path';

const ROOT = process.cwd();
const PORT = 3000;
const MIME = {
  '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript',
  '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.ico': 'image/x-icon',
  '.json': 'application/json', '.woff2': 'font/woff2'
};

createServer(async (req, res) => {
  try {
    let urlPath = decodeURIComponent(req.url.split('?')[0]);
    if (urlPath === '/') urlPath = '/index.html';
    if (urlPath.endsWith('/')) urlPath += 'index.html';
    const file = join(ROOT, urlPath);
    const data = await readFile(file);
    res.writeHead(200, { 'Content-Type': MIME[extname(file)] || 'application/octet-stream' });
    res.end(data);
  } catch {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('404');
  }
}).listen(PORT, () => console.log(`http://localhost:${PORT}`));
```

- [ ] **Step 3: Create `screenshot.mjs`** (house pattern — cached Chrome path, domcontentloaded + wait for Cal embeds)

```js
import puppeteer from 'puppeteer';

const url = process.argv[2] || 'http://localhost:3000';
const label = process.argv[3] || 'shot';
const CHROME = 'C:/Users/tlisb/.cache/puppeteer/chrome/win64-145.0.7632.77/chrome-win64/chrome.exe';

const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new' });
for (const [w, tag] of [[1440, 'desktop'], [390, 'mobile']]) {
  const page = await browser.newPage();
  await page.setViewport({ width: w, height: 900 });
  await page.goto(url, { waitUntil: 'domcontentloaded' });
  await new Promise(r => setTimeout(r, 2000));
  await page.screenshot({ path: `./temporary screenshots/${label}-${tag}.png`, fullPage: true });
  await page.close();
}
await browser.close();
console.log('done');
```

- [ ] **Step 4: Create `.gitignore`**

```
node_modules/
temporary screenshots/
.superpowers/
```

- [ ] **Step 5: Install puppeteer** (house note: use `--ignore-scripts`, Chrome already cached)

Run: `npm install --ignore-scripts`
Expected: `node_modules/` created, puppeteer 24.37.5 present, no Chrome download.

- [ ] **Step 6: Create `./temporary screenshots/` dir and verify server boots**

Run: `mkdir -p "temporary screenshots" && node serve.mjs &` then `curl -s -o /dev/null -w "%{http_code}" http://localhost:3000` (expect `404` — no index.html yet, server alive), then stop the server.
Expected: server prints `http://localhost:3000`; curl returns a status (not a connection error).

---

## Task 2: HTML skeleton, `<head>`, fonts

**Files:**
- Create: `index.html`

- [ ] **Step 1: Write the document head + empty body scaffold**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sygnals — Reach out the moment they show buying intent</title>
  <meta name="description" content="Sygnals monitors LinkedIn engagement, scores buying intent in real time, and hands you warm leads. Book a demo.">
  <meta property="og:title" content="Sygnals — LinkedIn intent signals">
  <meta property="og:description" content="Reach out the moment they show buying intent.">
  <meta property="og:type" content="website">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>/* tokens + styles added in Task 3 */</style>
</head>
<body>
  <!-- sections added in Tasks 4-11 -->
  <script>/* JS added in Task 11 */</script>
</body>
</html>
```

- [ ] **Step 2: Serve and verify**

Run: `node serve.mjs` then open `http://localhost:3000`.
Expected: blank page, HTTP 200, no console errors, fonts request succeeds in network tab.

- [ ] **Step 3: Commit**

Run: `git init` (if not already a repo) then:
```bash
git add package.json serve.mjs screenshot.mjs .gitignore index.html
git commit -m "chore: scaffold sygnals website tooling and html skeleton"
```

---

## Task 3: Design tokens, base styles, inline SVG logo, reveal CSS

**Files:**
- Modify: `index.html` (the `<style>` block)

- [ ] **Step 1: Replace the `<style>` placeholder with the token + base block**

```css
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{
  --cyan:#00d4f5;--cyan-lt:#0094b3;--black:#000;--surf:#0a0a0a;--elev:#181818;
  --border:#1a1a1a;--border2:#262626;--text:#edf2f5;--muted:#9f9f9f;--dim:#3a3a3a;
  --green:#00c758;--red:#ff2323;--amber:#edb200;--blue:#47a8ff;
  --font-display:'DM Sans',-apple-system,sans-serif;
  --font:'Inter',-apple-system,sans-serif;
  --mono:ui-monospace,'SF Mono',monospace;
  --maxw:1160px;
}
html{scroll-behavior:smooth}
body{background:var(--black);color:var(--text);font-family:var(--font);-webkit-font-smoothing:antialiased;line-height:1.5;overflow-x:hidden}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 24px}
h1,h2,h3{font-family:var(--font-display);font-weight:700;letter-spacing:-.03em;line-height:1.05}
a{color:inherit;text-decoration:none}
.eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--cyan);font-weight:600}
.section{padding:clamp(64px,9vw,120px) 0;border-top:1px solid var(--border)}
.section-surf{background:var(--surf)}
/* buttons — brand spec */
.btn{display:inline-flex;align-items:center;gap:8px;font-family:var(--font-display);font-weight:700;font-size:15px;letter-spacing:-.02em;border-radius:999px;padding:13px 26px;cursor:pointer;border:none;transition:transform .15s ease,background .15s ease}
.btn.primary{background:var(--cyan);color:#000}
.btn.primary:hover{transform:translateY(-1px);background:#3ce0ff}
.btn.secondary{background:transparent;color:var(--text);border:1px solid var(--border2)}
.btn.secondary:hover{border-color:var(--cyan);color:var(--cyan)}
.btn:focus-visible{outline:none;box-shadow:0 0 0 2px #000,0 0 0 4px var(--cyan)}
/* reveal-on-scroll */
.pre-reveal{opacity:0;transform:translateY(12px)}
.revealed{opacity:1;transform:none;transition:opacity .6s ease,transform .6s ease}
@media (prefers-reduced-motion:reduce){.pre-reveal{opacity:1;transform:none}.revealed{transition:none}*{scroll-behavior:auto}}
```

- [ ] **Step 2: Add reusable inline logo markup as an HTML snippet reference**

Document the canonical logo SVG (used verbatim in navbar, hero, footer). Add this comment block right after `<body>` so future tasks copy it exactly:

```html
<!-- CANONICAL LOGO — inline SVG, brand-locked. Copy verbatim. Dark: stroke #00d4f5.
<svg class="logo" viewBox="0 0 172 40" fill="none" role="img" aria-label="Sygnals" style="height:28px;width:auto">
  <path d="M 2 20 L 14 20 L 18 8 L 23 32 L 28 20 L 42 20" stroke="#00d4f5" stroke-width="3.2" stroke-linecap="butt" stroke-linejoin="miter"/>
  <circle cx="18" cy="5.5" r="3.6" fill="#00d4f5"/>
  <text x="50" y="20" font-family="'DM Sans',sans-serif" font-weight="700" font-size="30" letter-spacing="-1.35" dominant-baseline="middle">
    <tspan fill="#edf2f5">s</tspan><tspan fill="#00d4f5">y</tspan><tspan fill="#edf2f5">gnals</tspan>
  </text>
</svg>
-->
```

- [ ] **Step 3: Serve, screenshot, verify base**

Run: `node screenshot.mjs http://localhost:3000 task3-base`
Expected: black page, no errors. (No visible content yet — confirms tokens load cleanly.)

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "feat: add design tokens, base styles, canonical logo reference"
```

---

## Task 4: Sticky navbar

**Files:**
- Modify: `index.html` (add nav markup + nav CSS in `<style>`)

- [ ] **Step 1: Add navbar CSS**

```css
.nav{position:sticky;top:0;z-index:50;background:rgba(0,0,0,.72);backdrop-filter:blur(12px);border-bottom:1px solid transparent;transition:border-color .2s,background .2s}
.nav.scrolled{border-bottom-color:var(--border);background:rgba(0,0,0,.9)}
.nav-inner{display:flex;align-items:center;justify-content:space-between;height:64px}
.nav-links{display:flex;gap:28px;align-items:center}
.nav-links a{font-size:14px;color:var(--muted);font-weight:500}
.nav-links a:hover{color:var(--text)}
.nav-right{display:flex;gap:14px;align-items:center}
.lang-toggle{font-family:var(--mono);font-size:11px;color:var(--muted);border:1px solid var(--border2);border-radius:999px;padding:5px 10px;letter-spacing:.05em}
.lang-toggle:hover{color:var(--cyan);border-color:var(--cyan)}
.nav-burger{display:none}
@media(max-width:820px){.nav-links{display:none}.nav-burger{display:flex}}
```

- [ ] **Step 2: Add navbar markup** (first element inside `<body>`, after the logo comment)

```html
<header class="nav" id="nav">
  <div class="wrap nav-inner">
    <a href="/" aria-label="Sygnals home">
      <svg class="logo" viewBox="0 0 172 40" fill="none" role="img" aria-label="Sygnals" style="height:26px;width:auto">
        <path d="M 2 20 L 14 20 L 18 8 L 23 32 L 28 20 L 42 20" stroke="#00d4f5" stroke-width="3.2" stroke-linecap="butt" stroke-linejoin="miter"/>
        <circle cx="18" cy="5.5" r="3.6" fill="#00d4f5"/>
        <text x="50" y="20" font-family="'DM Sans',sans-serif" font-weight="700" font-size="30" letter-spacing="-1.35" dominant-baseline="middle"><tspan fill="#edf2f5">s</tspan><tspan fill="#00d4f5">y</tspan><tspan fill="#edf2f5">gnals</tspan></text>
      </svg>
    </a>
    <nav class="nav-links">
      <a href="#how">How it works</a>
      <a href="#features">Features</a>
      <a href="#pricing">Pricing</a>
      <a href="#faq">FAQ</a>
    </nav>
    <div class="nav-right">
      <a href="/pt-br/" class="lang-toggle" id="langToggle">PT-BR</a>
      <a href="#demo" class="btn primary" style="padding:9px 18px;font-size:14px">Book a demo</a>
    </div>
  </div>
</header>
```

- [ ] **Step 3: Screenshot and verify**

Run: `node screenshot.mjs http://localhost:3000 task4-nav`
Expected: sticky top bar, cyan-accented wordmark left, 4 muted links, PT-BR pill + cyan "Book a demo" pill right. On mobile (390) links hidden.

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "feat: add sticky navbar with logo, links, lang toggle, demo CTA"
```

---

## Task 5: Hero section

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Add hero CSS**

```css
.hero{position:relative;padding:clamp(72px,11vw,140px) 0 clamp(64px,8vw,110px);overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(120% 90% at 50% -10%,rgba(0,212,245,.14),transparent 55%);pointer-events:none}
.hero-inner{position:relative;display:grid;grid-template-columns:1.1fr .9fr;gap:56px;align-items:center}
.hero h1{font-size:clamp(38px,6vw,68px);margin:18px 0 20px}
.hero h1 b{color:var(--cyan);font-weight:700}
.hero-sub{color:var(--muted);font-size:clamp(16px,1.6vw,19px);max-width:520px;margin-bottom:32px}
.hero-cta{display:flex;gap:14px;flex-wrap:wrap}
.hero-trust{margin-top:28px;font-size:13px;color:var(--dim);display:flex;gap:8px;align-items:center}
/* hero visual card */
.iscore{background:var(--surf);border:1px solid var(--border2);border-radius:14px;padding:22px 24px;box-shadow:0 24px 60px -24px rgba(0,212,245,.25)}
.iscore-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px}
.iscore-name{font-weight:600;font-size:15px}
.iscore-sub{font-size:12px;color:var(--muted)}
.badge{display:inline-flex;align-items:center;gap:6px;padding:4px 11px;border-radius:999px;font-size:12px;font-weight:600}
.badge .dot{width:5px;height:5px;border-radius:50%}
.badge.warm{background:rgba(237,178,0,.12);color:#e3b341;border:1px solid rgba(237,178,0,.25)}
.badge.warm .dot{background:var(--amber)}
.badge.hot{background:rgba(255,35,35,.13);color:#ff6b6b;border:1px solid rgba(255,35,35,.3)}
.badge.hot .dot{background:var(--red)}
.iscore-row{display:flex;justify-content:space-between;font-size:13px;padding:7px 0;border-bottom:1px solid var(--border)}
.iscore-row .lbl{color:var(--muted)}
.iscore-row .val{font-family:var(--mono)}
.iscore-row .val.pos{color:var(--text)}
.iscore-row .val.neg{color:var(--dim)}
.iscore-total{display:flex;justify-content:space-between;align-items:center;padding-top:14px;margin-top:8px;border-top:1px solid var(--border2)}
.iscore-total .num{font-family:var(--font-display);font-size:30px;font-weight:700;color:var(--cyan);letter-spacing:-.03em}
@media(max-width:820px){.hero-inner{grid-template-columns:1fr;gap:36px}.hero-cta{flex-direction:column}.hero-cta .btn{width:100%;justify-content:center}}
```

- [ ] **Step 2: Add hero markup** (after `</header>`)

```html
<section class="hero">
  <div class="wrap hero-inner">
    <div class="pre-reveal">
      <span class="eyebrow">LinkedIn intent signals</span>
      <h1>Reach out the <b>moment</b> they show buying intent.</h1>
      <p class="hero-sub">Sygnals monitors LinkedIn activity, scores intent in real time, and hands you warm leads — so you stop cold-pitching and start closing.</p>
      <div class="hero-cta">
        <a href="#demo" class="btn primary">Book a demo →</a>
        <a href="#how" class="btn secondary">See how it works</a>
      </div>
      <div class="hero-trust">Built for B2B founders &amp; sales teams · No cold lists</div>
    </div>
    <div class="pre-reveal iscore" aria-label="Example intent score">
      <div class="iscore-head">
        <div><div class="iscore-name">Guilherme Mussi</div><div class="iscore-sub">VP Sales · commented 3× this week</div></div>
        <span class="badge warm"><span class="dot"></span>Warm</span>
      </div>
      <div class="iscore-row"><span class="lbl">Frequency (3×)</span><span class="val pos">+30</span></div>
      <div class="iscore-row"><span class="lbl">Seniority (VP)</span><span class="val pos">+40</span></div>
      <div class="iscore-row"><span class="lbl">Type (comment)</span><span class="val pos">+20</span></div>
      <div class="iscore-row"><span class="lbl">Recency (5 days)</span><span class="val neg">−17</span></div>
      <div class="iscore-total"><span class="iscore-sub">Intent Score</span><span class="num" data-countup="73">73</span></div>
    </div>
  </div>
</section>
```

- [ ] **Step 3: Screenshot and verify**

Run: `node screenshot.mjs http://localhost:3000 task5-hero`
Expected: two-column hero, cyan radial glow up top, headline with cyan "moment", dual pill CTAs, Intent Score card right showing breakdown summing to 73 + Warm badge. Mobile: stacked, full-width buttons.

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "feat: add hero section with intent-score showcase card"
```

---

## Task 6: Problem section

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Add problem CSS**

```css
.prob-head{max-width:680px;margin-bottom:44px}
.prob-head h2{font-size:clamp(28px,4vw,42px);margin-bottom:14px}
.prob-head p{color:var(--muted);font-size:17px}
.prob-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.prob-card{background:var(--surf);border:1px solid var(--border);border-radius:12px;padding:26px}
.prob-card .k{font-family:var(--mono);color:var(--red);font-size:13px;margin-bottom:10px}
.prob-card h3{font-size:18px;margin-bottom:8px}
.prob-card p{color:var(--muted);font-size:14px}
@media(max-width:820px){.prob-grid{grid-template-columns:1fr}}
```

- [ ] **Step 2: Add problem markup**

```html
<section class="section">
  <div class="wrap">
    <div class="prob-head pre-reveal">
      <span class="eyebrow">The problem</span>
      <h2>Cold outreach is a numbers game you lose.</h2>
      <p>You blast the same pitch to people who aren't in-market — burning your time, your credits, and your LinkedIn reputation.</p>
    </div>
    <div class="prob-grid">
      <div class="prob-card pre-reveal"><div class="k">01</div><h3>No timing</h3><p>You reach out on your calendar, not theirs. By the time you message, the moment's gone.</p></div>
      <div class="prob-card pre-reveal"><div class="k">02</div><h3>No signal</h3><p>Every lead looks the same in a spreadsheet. Nothing tells you who's actually paying attention.</p></div>
      <div class="prob-card pre-reveal"><div class="k">03</div><h3>Wasted effort</h3><p>Hours of manual scrolling to find one warm lead — that a competitor already messaged.</p></div>
    </div>
  </div>
</section>
```

- [ ] **Step 3: Screenshot and verify**

Run: `node screenshot.mjs http://localhost:3000 task6-problem`
Expected: heading block + 3 red-numbered cards. Mobile: single column.

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "feat: add problem section"
```

---

## Task 7: How it works (3 steps)

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Add how-it-works CSS**

```css
.how-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;margin-top:44px;border:1px solid var(--border);border-radius:12px;overflow:hidden}
.how-step{background:var(--surf);padding:34px 30px}
.how-step .n{font-family:var(--mono);font-size:12px;color:var(--cyan);letter-spacing:.1em}
.how-step h3{font-size:20px;margin:16px 0 10px}
.how-step p{color:var(--muted);font-size:14px}
.how-wave{margin-top:20px;opacity:.5}
@media(max-width:820px){.how-grid{grid-template-columns:1fr}}
```

- [ ] **Step 2: Add how-it-works markup**

```html
<section class="section section-surf" id="how">
  <div class="wrap">
    <div class="prob-head pre-reveal">
      <span class="eyebrow">How it works</span>
      <h2>From noise to warm leads in three steps.</h2>
    </div>
    <div class="how-grid">
      <div class="how-step pre-reveal"><div class="n">STEP 01</div><h3>Choose who to monitor</h3><p>Point Sygnals at the people and accounts that matter — prospects, target roles, ICP champions.</p></div>
      <div class="how-step pre-reveal"><div class="n">STEP 02</div><h3>Sygnals watches LinkedIn</h3><p>We track their engagement — posts, comments, reactions — continuously, in the background.</p></div>
      <div class="how-step pre-reveal"><div class="n">STEP 03</div><h3>Intent Score surfaces the hot ones</h3><p>Each lead gets a live score. Hot and Warm rise to the top, ready for you to reach out.</p></div>
    </div>
  </div>
</section>
```

- [ ] **Step 3: Screenshot and verify**

Run: `node screenshot.mjs http://localhost:3000 task7-how`
Expected: surf-background section, 3 joined step panels with cyan step labels. Mobile: stacked.

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "feat: add how-it-works section"
```

---

## Task 8: Intent Score showcase

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Add showcase CSS**

```css
.showcase{display:grid;grid-template-columns:.95fr 1.05fr;gap:56px;align-items:center;margin-top:24px}
.showcase-factors{display:flex;flex-direction:column;gap:14px}
.factor{display:flex;gap:14px;align-items:flex-start}
.factor .icn{width:34px;height:34px;border-radius:8px;background:rgba(0,212,245,.1);border:1px solid rgba(0,212,245,.25);flex-shrink:0;display:flex;align-items:center;justify-content:center;color:var(--cyan);font-family:var(--mono);font-size:13px}
.factor h4{font-size:15px;margin-bottom:3px}
.factor p{color:var(--muted);font-size:13px}
@media(max-width:820px){.showcase{grid-template-columns:1fr;gap:36px}}
```

- [ ] **Step 2: Add showcase markup** (reuses `.iscore` card styles from Task 5)

```html
<section class="section">
  <div class="wrap">
    <div class="prob-head pre-reveal">
      <span class="eyebrow">Intent Score</span>
      <h2>One number that tells you who's ready.</h2>
      <p>Sygnals weighs four signals into a single 0–100 score, so you always know who to message first.</p>
    </div>
    <div class="showcase">
      <div class="showcase-factors">
        <div class="factor pre-reveal"><div class="icn">Hz</div><div><h4>Frequency</h4><p>How often they engage with relevant content. More activity, more intent.</p></div></div>
        <div class="factor pre-reveal"><div class="icn">Sr</div><div><h4>Seniority</h4><p>Decision-makers weigh heavier. A VP comment beats ten interns.</p></div></div>
        <div class="factor pre-reveal"><div class="icn">Ty</div><div><h4>Engagement type</h4><p>A thoughtful comment signals more than a passive like.</p></div></div>
        <div class="factor pre-reveal"><div class="icn">Rc</div><div><h4>Recency</h4><p>Fresh signals score higher. Old activity decays automatically.</p></div></div>
      </div>
      <div class="iscore pre-reveal">
        <div class="iscore-head">
          <div><div class="iscore-name">Raphael Bozza</div><div class="iscore-sub">Founder · engaged 6× in 48h</div></div>
          <span class="badge hot"><span class="dot"></span>Hot</span>
        </div>
        <div class="iscore-row"><span class="lbl">Frequency (6×)</span><span class="val pos">+45</span></div>
        <div class="iscore-row"><span class="lbl">Seniority (Founder)</span><span class="val pos">+40</span></div>
        <div class="iscore-row"><span class="lbl">Type (comment)</span><span class="val pos">+20</span></div>
        <div class="iscore-row"><span class="lbl">Recency (2 days)</span><span class="val neg">−13</span></div>
        <div class="iscore-total"><span class="iscore-sub">Intent Score</span><span class="num" data-countup="92">92</span></div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 3: Screenshot and verify**

Run: `node screenshot.mjs http://localhost:3000 task8-showcase`
Expected: left column 4 factors with cyan icon chips, right column Hot score card = 92. Mobile: stacked.

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "feat: add intent-score showcase section"
```

---

## Task 9: Features grid + dashboard preview

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Add features + preview CSS**

```css
.feat-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:44px}
.feat{background:var(--surf);border:1px solid var(--border);border-radius:12px;padding:26px;transition:border-color .2s}
.feat:hover{border-color:var(--border2)}
.feat .ic{width:38px;height:38px;color:var(--cyan);margin-bottom:16px}
.feat h3{font-size:17px;margin-bottom:8px}
.feat p{color:var(--muted);font-size:14px}
.preview{margin-top:56px;background:var(--surf);border:1px solid var(--border2);border-radius:16px;padding:20px;overflow:hidden}
.preview-bar{display:flex;gap:6px;padding:0 4px 16px}
.preview-bar i{width:9px;height:9px;border-radius:50%;background:var(--border2)}
.sig-list{display:flex;flex-direction:column;gap:8px}
.sig{display:flex;justify-content:space-between;align-items:center;padding:12px 16px;background:#000;border:1px solid var(--border);border-radius:8px}
.sig-left{display:flex;align-items:center;gap:11px}
.sig-dot{width:7px;height:7px;border-radius:50%}
.sig-name{font-size:14px;font-weight:500}
@media(max-width:820px){.feat-grid{grid-template-columns:1fr}}
```

- [ ] **Step 2: Add features markup** (inline SVG icons, cyan stroke line style)

```html
<section class="section" id="features">
  <div class="wrap">
    <div class="prob-head pre-reveal">
      <span class="eyebrow">Features</span>
      <h2>Everything you need to sell on signal.</h2>
    </div>
    <div class="feat-grid">
      <div class="feat pre-reveal"><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 12h4l3-9 4 18 3-9h4"/></svg><h3>Signal monitoring</h3><p>Track LinkedIn engagement across the people and accounts you care about, 24/7.</p></div>
      <div class="feat pre-reveal"><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg><h3>Real-time intent scoring</h3><p>Every lead gets a live 0–100 Intent Score. Hot and Warm rise to the top automatically.</p></div>
      <div class="feat pre-reveal"><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18"/></svg><h3>Connect LinkedIn accounts</h3><p>Link one or more LinkedIn accounts to expand reach across your team's network.</p></div>
      <div class="feat pre-reveal"><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M2 7l10-5 10 5"/></svg><h3>Credit-based usage</h3><p>Pay for what you monitor. Transparent credits, no per-seat lock-in, upgrade anytime.</p></div>
      <div class="feat pre-reveal"><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v12H8l-4 4z"/></svg><h3>Export &amp; integrate</h3><p>Push warm leads to CSV, Clay, or your CRM via webhooks. Sygnals fits your stack.</p></div>
      <div class="feat pre-reveal"><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 8a6 6 0 0112 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10 21h4"/></svg><h3>Real-time alerts</h3><p>Get notified the instant a lead crosses into Hot — so you're first to the conversation.</p></div>
    </div>

    <div class="preview pre-reveal" aria-label="Dashboard preview">
      <div class="preview-bar"><i></i><i></i><i></i></div>
      <div class="sig-list">
        <div class="sig"><div class="sig-left"><span class="sig-dot" style="background:var(--red)"></span><span class="sig-name">Raphael Bozza</span></div><span class="badge hot"><span class="dot"></span>Hot · 92</span></div>
        <div class="sig"><div class="sig-left"><span class="sig-dot" style="background:var(--amber)"></span><span class="sig-name">Guilherme Mussi</span></div><span class="badge warm"><span class="dot"></span>Warm · 73</span></div>
        <div class="sig"><div class="sig-left"><span class="sig-dot" style="background:var(--blue)"></span><span class="sig-name">David Costa Lima</span></div><span class="badge" style="background:rgba(71,168,255,.1);color:var(--blue);border:1px solid rgba(71,168,255,.22)"><span class="dot" style="background:var(--blue)"></span>Partial</span></div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 3: Screenshot and verify**

Run: `node screenshot.mjs http://localhost:3000 task9-features`
Expected: 6 feature cards with cyan line icons (first icon = waveform matching the mark), then a framed dashboard mock with 3 signal rows (Hot 92 / Warm 73 / Partial). Mobile: single column.

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "feat: add features grid and dashboard preview"
```

---

## Task 10: Pricing section

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Add pricing CSS**

```css
.price-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:44px;align-items:stretch}
.price{background:var(--surf);border:1px solid var(--border);border-radius:14px;padding:30px 28px;display:flex;flex-direction:column}
.price.feat{border-color:var(--cyan);box-shadow:0 20px 60px -30px rgba(0,212,245,.4)}
.price-tag{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--cyan);margin-bottom:8px;min-height:14px}
.price h3{font-size:20px;margin-bottom:6px}
.price .amt{font-family:var(--font-display);font-size:40px;font-weight:700;letter-spacing:-.03em;margin:10px 0 2px}
.price .amt span{font-size:15px;color:var(--muted);font-weight:500}
.price ul{list-style:none;margin:22px 0 26px;display:flex;flex-direction:column;gap:11px;flex:1}
.price li{font-size:14px;color:var(--muted);display:flex;gap:9px;align-items:flex-start}
.price li::before{content:'';width:16px;height:16px;flex-shrink:0;margin-top:2px;background:no-repeat center/contain url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2300d4f5' stroke-width='3'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E")}
.price-note{text-align:center;margin-top:24px;color:var(--dim);font-size:13px}
@media(max-width:820px){.price-grid{grid-template-columns:1fr}}
```

- [ ] **Step 2: Add pricing markup** (numbers from owner-locked board; Explorer highlighted)

```html
<section class="section section-surf" id="pricing">
  <div class="wrap">
    <div class="prob-head pre-reveal" style="text-align:center;margin:0 auto 0">
      <span class="eyebrow">Pricing</span>
      <h2>Plans that scale with your pipeline.</h2>
    </div>
    <div class="price-grid">
      <div class="price pre-reveal">
        <div class="price-tag">&nbsp;</div>
        <h3>Starter</h3>
        <div class="amt">$99<span>/mo</span></div>
        <ul>
          <li>10,000 credits / mo</li>
          <li>10 signals</li>
          <li>1 LinkedIn account</li>
          <li>Intent scoring &amp; alerts</li>
          <li>CSV &amp; webhook export</li>
        </ul>
        <a href="#demo" class="btn secondary" style="justify-content:center">Book a demo</a>
      </div>
      <div class="price feat pre-reveal">
        <div class="price-tag">Most popular</div>
        <h3>Explorer</h3>
        <div class="amt">$179<span>/mo</span></div>
        <ul>
          <li>25,000 credits / mo</li>
          <li>20 signals</li>
          <li>3 LinkedIn accounts</li>
          <li>Everything in Starter</li>
          <li>Priority support</li>
        </ul>
        <a href="#demo" class="btn primary" style="justify-content:center">Book a demo</a>
      </div>
      <div class="price pre-reveal">
        <div class="price-tag">&nbsp;</div>
        <h3>Pro</h3>
        <div class="amt">$349<span>/mo</span></div>
        <ul>
          <li>50,000 credits / mo</li>
          <li>40 signals</li>
          <li>10 LinkedIn accounts</li>
          <li>Unlimited workspaces</li>
          <li>Lower overage rate</li>
        </ul>
        <a href="#demo" class="btn secondary" style="justify-content:center">Book a demo</a>
      </div>
    </div>
    <p class="price-note">Credit overage from $12/1k · LinkedIn-account add-on $15/mo · Prices in USD</p>
  </div>
</section>
```

- [ ] **Step 3: Screenshot and verify**

Run: `node screenshot.mjs http://localhost:3000 task10-pricing`
Expected: 3 pricing cards, Explorer center with cyan border + "Most popular" + glow + primary CTA; others secondary CTA. Numbers match board ($99/$179/$349). Mobile: stacked.

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "feat: add pricing section from owner-locked board"
```

---

## Task 11: FAQ, Final CTA, Footer, and all JS

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Add FAQ / CTA / footer CSS**

```css
.faq{max-width:820px;margin:44px auto 0}
.faq-item{border-bottom:1px solid var(--border)}
.faq-q{width:100%;text-align:left;background:none;border:none;color:var(--text);font-family:var(--font-display);font-weight:600;font-size:17px;padding:22px 0;cursor:pointer;display:flex;justify-content:space-between;gap:16px;align-items:center}
.faq-q .pm{color:var(--cyan);font-size:22px;line-height:1;flex-shrink:0;transition:transform .2s}
.faq-item.open .faq-q .pm{transform:rotate(45deg)}
.faq-a{max-height:0;overflow:hidden;transition:max-height .3s ease}
.faq-a p{color:var(--muted);font-size:15px;padding:0 0 22px;line-height:1.6}
.faq-item.open .faq-a{max-height:320px}
.cta-final{position:relative;text-align:center;overflow:hidden}
.cta-final::before{content:'';position:absolute;inset:0;background:radial-gradient(90% 120% at 50% 120%,rgba(0,212,245,.16),transparent 60%);pointer-events:none}
.cta-final h2{position:relative;font-size:clamp(30px,5vw,52px);margin-bottom:18px}
.cta-final p{position:relative;color:var(--muted);font-size:18px;margin-bottom:32px}
.footer{border-top:1px solid var(--border);padding:56px 0 40px}
.footer-inner{display:flex;justify-content:space-between;gap:40px;flex-wrap:wrap;align-items:flex-start}
.footer-cols{display:flex;gap:64px;flex-wrap:wrap}
.footer-col h5{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--dim);margin-bottom:14px}
.footer-col a{display:block;color:var(--muted);font-size:14px;margin-bottom:10px}
.footer-col a:hover{color:var(--text)}
.footer-bottom{display:flex;justify-content:space-between;flex-wrap:wrap;gap:16px;margin-top:48px;padding-top:24px;border-top:1px solid var(--border);font-size:12px;color:var(--dim)}
@media(max-width:820px){.footer-inner{flex-direction:column}}
```

- [ ] **Step 2: Add FAQ + Final CTA + Footer markup** (Cal.com placeholder link at `#demo`)

```html
<section class="section" id="faq">
  <div class="wrap">
    <div class="prob-head pre-reveal" style="text-align:center;margin:0 auto 0">
      <span class="eyebrow">FAQ</span>
      <h2>Questions, answered.</h2>
    </div>
    <div class="faq">
      <div class="faq-item open"><button class="faq-q" onclick="toggleFaq(this)">Is Sygnals LinkedIn-compliant?<span class="pm">+</span></button><div class="faq-a"><p>Sygnals monitors public engagement signals and connects through your own LinkedIn account. We never scrape private data or automate outreach on your behalf — you stay in control of every conversation.</p></div></div>
      <div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)">What is a credit?<span class="pm">+</span></button><div class="faq-a"><p>Credits are consumed as Sygnals monitors activity and enriches leads. Each plan includes a monthly credit allowance; you can add credit packs or let overage cover spikes.</p></div></div>
      <div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)">Which LinkedIn accounts can I connect?<span class="pm">+</span></button><div class="faq-a"><p>Any standard LinkedIn account. Plans include 1 to 10 connected accounts; add more for $15/account/month as your team grows.</p></div></div>
      <div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)">How is the Intent Score calculated?<span class="pm">+</span></button><div class="faq-a"><p>Four weighted factors: engagement frequency, the person's seniority, the type of engagement, and how recent it is. Together they produce a live 0–100 score, bucketed into Warm (60–79) and Hot (80–100).</p></div></div>
      <div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)">Can I cancel anytime?<span class="pm">+</span></button><div class="faq-a"><p>Yes. Plans are monthly and you can cancel or change tiers whenever you like — no annual lock-in.</p></div></div>
    </div>
  </div>
</section>

<section class="section cta-final" id="demo">
  <div class="wrap">
    <h2>See Sygnals on your pipeline.</h2>
    <p>Book a 20-minute demo — we'll show you live intent signals for your market.</p>
    <a href="https://cal.com/sygnals/demo" class="btn primary" style="font-size:16px;padding:15px 32px">Book a demo →</a>
  </div>
</section>

<footer class="footer">
  <div class="wrap">
    <div class="footer-inner">
      <div>
        <svg class="logo" viewBox="0 0 172 40" fill="none" role="img" aria-label="Sygnals" style="height:26px;width:auto">
          <path d="M 2 20 L 14 20 L 18 8 L 23 32 L 28 20 L 42 20" stroke="#00d4f5" stroke-width="3.2" stroke-linecap="butt" stroke-linejoin="miter"/>
          <circle cx="18" cy="5.5" r="3.6" fill="#00d4f5"/>
          <text x="50" y="20" font-family="'DM Sans',sans-serif" font-weight="700" font-size="30" letter-spacing="-1.35" dominant-baseline="middle"><tspan fill="#edf2f5">s</tspan><tspan fill="#00d4f5">y</tspan><tspan fill="#edf2f5">gnals</tspan></text>
        </svg>
        <p style="color:var(--dim);font-size:13px;margin-top:14px;max-width:240px">Reach out the moment they show buying intent.</p>
      </div>
      <div class="footer-cols">
        <div class="footer-col"><h5>Product</h5><a href="#how">How it works</a><a href="#features">Features</a><a href="#pricing">Pricing</a></div>
        <div class="footer-col"><h5>Company</h5><a href="#demo">Book a demo</a><a href="#">Blog</a><a href="mailto:hello@sygnals.com">Contact</a></div>
        <div class="footer-col"><h5>Legal</h5><a href="#">Privacy</a><a href="#">Terms</a></div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Sygnals. All rights reserved.</span>
      <a href="/pt-br/" class="lang-toggle">Ver em Português →</a>
    </div>
  </div>
</footer>
```

- [ ] **Step 3: Replace the `<script>` placeholder with all page JS**

```html
<script>
// Reveal-on-scroll
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.remove('pre-reveal');
      e.target.classList.add('revealed');
      if (e.target.dataset.countup) countUp(e.target);
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.12 });
document.querySelectorAll('.pre-reveal').forEach(el => io.observe(el));

// Count-up for Intent Score numbers
function countUp(el){
  const target = parseInt(el.dataset.countup, 10);
  let n = 0; const step = Math.max(1, Math.round(target / 28));
  const t = setInterval(() => { n += step; if (n >= target){ n = target; clearInterval(t);} el.textContent = n; }, 24);
}

// FAQ accordion — close siblings on open
function toggleFaq(btn){
  const item = btn.closest('.faq-item');
  const open = item.classList.contains('open');
  document.querySelectorAll('.faq-item.open').forEach(i => i.classList.remove('open'));
  if (!open) item.classList.add('open');
}

// Sticky nav condense
const nav = document.getElementById('nav');
addEventListener('scroll', () => nav.classList.toggle('scrolled', scrollY > 12), { passive: true });

// Language preference persistence (EN page)
try {
  if (localStorage.getItem('syg_lang') === 'pt-br' && !location.pathname.startsWith('/pt-br')) {
    location.replace('/pt-br/');
  }
  document.getElementById('langToggle')?.addEventListener('click', () => localStorage.setItem('syg_lang', 'pt-br'));
} catch(e){}
</script>
```

- [ ] **Step 4: Screenshot and verify full EN page**

Run: `node screenshot.mjs http://localhost:3000 task11-full`
Expected: FAQ accordion (first item open), cyan-glow final CTA band with "Book a demo" (→ cal.com placeholder), footer with logo + 3 link columns + pt-BR toggle. Scroll: numbers count up, nav condenses, sections fade in. No console errors.

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "feat: add faq, final cta, footer, and page interactions"
```

---

## Task 12: pt-BR version

**Files:**
- Create: `pt-br/index.html`

- [ ] **Step 1: Copy EN file as base**

Run: `mkdir -p pt-br && cp index.html pt-br/index.html`
Expected: identical file at `pt-br/index.html`.

- [ ] **Step 2: Translate all copy + swap attributes** (edit `pt-br/index.html`)

Apply these exact changes:
- `<html lang="en">` → `<html lang="pt-BR">`
- `<title>` → `Sygnals — Fale com quem está pronto para comprar`
- meta description → `Sygnals monitora o engajamento no LinkedIn, mede a intenção de compra em tempo real e entrega leads quentes. Agende uma demonstração.`
- Nav links: `How it works`→`Como funciona`, `Features`→`Recursos`, `Pricing`→`Preços`, `FAQ`→`FAQ`
- Lang toggle `PT-BR` → `EN`, `href="/pt-br/"` → `href="/"`; footer toggle `Ver em Português →` → `View in English →` with `href="/"`
- Nav + all CTAs `Book a demo` → `Agende uma demonstração`; hero secondary `See how it works` → `Ver como funciona`
- Eyebrows: `LinkedIn intent signals`→`Sinais de intenção no LinkedIn`; `The problem`→`O problema`; `How it works`→`Como funciona`; `Intent Score`→`Intent Score`; `Features`→`Recursos`; `Pricing`→`Preços`; `FAQ`→`FAQ`
- Hero H1 → `Fale com quem está <b>pronto</b> para comprar.`
- Hero sub → `O Sygnals monitora a atividade no LinkedIn, mede a intenção em tempo real e entrega leads quentes — pare de mandar pitch frio e comece a fechar.`
- Hero trust → `Feito para founders e times de vendas B2B · Sem listas frias`
- Problem H2 → `Prospecção fria é um jogo de números que você perde.`; sub → `Você dispara o mesmo pitch para quem não está no momento de compra — queimando seu tempo, seus créditos e sua reputação no LinkedIn.`
- Problem cards: `No timing`/`No signal`/`Wasted effort` → `Sem timing`/`Sem sinal`/`Esforço desperdiçado`, and translate each `<p>` (Sem timing: "Você fala na sua agenda, não na dele. Quando manda a mensagem, o momento já passou." · Sem sinal: "Todo lead parece igual numa planilha. Nada mostra quem está de fato prestando atenção." · Esforço desperdiçado: "Horas rolando o feed pra achar um lead quente — que um concorrente já abordou.")
- How steps: `Choose who to monitor`→`Escolha quem monitorar` ("Aponte o Sygnals para as pessoas e contas que importam — prospects, cargos-alvo, campeões do seu ICP."); `Sygnals watches LinkedIn`→`O Sygnals observa o LinkedIn` ("Rastreamos o engajamento — posts, comentários, reações — continuamente, em segundo plano."); `Intent Score surfaces the hot ones`→`O Intent Score destaca os quentes` ("Cada lead recebe um score ao vivo. Quentes e mornos sobem para o topo, prontos para você abordar."); section H2 → `Do ruído a leads quentes em três passos.`; `STEP 0x`→`PASSO 0x`
- Showcase H2 → `Um número que mostra quem está pronto.`; sub → `O Sygnals combina quatro sinais num único score de 0–100, para você sempre saber quem abordar primeiro.`; factors `Frequency/Seniority/Engagement type/Recency` → `Frequência/Senioridade/Tipo de engajamento/Recência` (translate the four `<p>`: Frequência: "Com que frequência engajam com conteúdo relevante. Mais atividade, mais intenção." · Senioridade: "Decisores pesam mais. Um comentário de VP vale mais que dez de estagiários." · Tipo de engajamento: "Um comentário pensado sinaliza mais que um like passivo." · Recência: "Sinais recentes pontuam mais. Atividade antiga decai automaticamente."); card subs `commented 3× this week`→`comentou 3× nesta semana`, `engaged 6× in 48h`→`engajou 6× em 48h`; row labels `Frequency/Seniority/Type/Recency`→`Frequência/Senioridade/Tipo/Recência`; `Warm`/`Hot` badges → `Morno`/`Quente`
- Features H2 → `Tudo o que você precisa para vender no sinal.`; card titles/descs translate: `Signal monitoring`→`Monitoramento de sinais` ("Acompanhe o engajamento no LinkedIn das pessoas e contas que importam, 24/7."); `Real-time intent scoring`→`Score de intenção em tempo real` ("Cada lead recebe um Intent Score ao vivo de 0–100. Quentes e mornos sobem sozinhos."); `Connect LinkedIn accounts`→`Conecte contas do LinkedIn` ("Conecte uma ou mais contas para ampliar o alcance na rede do seu time."); `Credit-based usage`→`Uso por créditos` ("Pague pelo que monitora. Créditos transparentes, sem trava por assento, upgrade quando quiser."); `Export & integrate`→`Exporte e integre` ("Envie leads quentes para CSV, Clay ou seu CRM via webhooks. O Sygnals encaixa no seu stack."); `Real-time alerts`→`Alertas em tempo real` ("Seja avisado no instante em que um lead vira Quente — para ser o primeiro na conversa."); preview badges `Hot · 92`/`Warm · 73`/`Partial`→`Quente · 92`/`Morno · 73`/`Parcial`
- Pricing H2 → `Planos que crescem com seu pipeline.`; `Most popular`→`Mais popular`; feature bullets translate (`credits / mo`→`créditos / mês`, `signals`→`sinais`, `LinkedIn account(s)`→`conta(s) do LinkedIn`, `Intent scoring & alerts`→`Score de intenção e alertas`, `CSV & webhook export`→`Exportação CSV e webhook`, `Everything in Starter`→`Tudo do Starter`, `Priority support`→`Suporte prioritário`, `Unlimited workspaces`→`Workspaces ilimitados`, `Lower overage rate`→`Taxa de excedente menor`); note → `Excedente de créditos a partir de $12/1k · Add-on de conta LinkedIn $15/mês · Cobrança em BRL para clientes no Brasil`
- FAQ H2 → `Perguntas, respondidas.`; translate all 5 Q/A to pt-BR (Q1 `O Sygnals respeita as regras do LinkedIn?` A: "O Sygnals monitora sinais públicos de engajamento e conecta pela sua própria conta do LinkedIn. Nunca extraímos dados privados nem automatizamos abordagem no seu lugar — você controla cada conversa." · Q2 `O que é um crédito?` A: "Créditos são consumidos conforme o Sygnals monitora atividade e enriquece leads. Cada plano inclui uma franquia mensal; você pode adicionar pacotes ou deixar o excedente cobrir picos." · Q3 `Quais contas do LinkedIn posso conectar?` A: "Qualquer conta padrão do LinkedIn. Os planos incluem de 1 a 10 contas conectadas; adicione mais por $15/conta/mês conforme o time cresce." · Q4 `Como o Intent Score é calculado?` A: "Quatro fatores ponderados: frequência de engajamento, senioridade da pessoa, tipo de engajamento e quão recente é. Juntos produzem um score ao vivo de 0–100, dividido em Morno (60–79) e Quente (80–100)." · Q5 `Posso cancelar quando quiser?` A: "Sim. Os planos são mensais e você pode cancelar ou trocar de nível quando quiser — sem trava anual.")
- Final CTA H2 → `Veja o Sygnals no seu pipeline.`; p → `Agende uma demo de 20 minutos — mostramos sinais de intenção ao vivo para o seu mercado.`
- Footer tagline → `Fale com quem está pronto para comprar.`; columns `Product/Company/Legal`→`Produto/Empresa/Legal`; links `How it works/Features/Pricing`→`Como funciona/Recursos/Preços`, `Book a demo/Blog/Contact`→`Agende uma demo/Blog/Contato`, `Privacy/Terms`→`Privacidade/Termos`; copyright `All rights reserved.`→`Todos os direitos reservados.`
- In the `<script>`, flip the language persistence for the pt-BR page: replace the localStorage block with:

```js
try {
  document.getElementById('langToggle')?.addEventListener('click', () => localStorage.setItem('syg_lang', 'en'));
} catch(e){}
```

- [ ] **Step 3: Screenshot and verify pt-BR**

Run: `node screenshot.mjs http://localhost:3000/pt-br/ ptbr-full`
Expected: full page in Portuguese, all CTAs "Agende uma demonstração", badges Quente/Morno, pricing note mentions BRL, toggle shows "EN". Numbers/logo/colors identical to EN.

- [ ] **Step 4: Commit**

```bash
git add pt-br/index.html
git commit -m "feat: add pt-BR version of landing page"
```

---

## Task 13: Geo-redirect, Vercel config, final QA

**Files:**
- Modify: `index.html` (add geo-redirect before the lang-persistence block)
- Create: `vercel.json`

- [ ] **Step 1: Add BR geo-redirect to EN page `<script>`** (INCHAT pattern — only when no explicit choice stored)

Insert at the top of the `try` block in the EN page's language script, before the `syg_lang` check:

```js
// BR geo-redirect (only if user hasn't explicitly chosen EN)
if (!localStorage.getItem('syg_lang')) {
  const tz = Intl.DateTimeFormat().resolvedOptions().timeZone || '';
  const lang = (navigator.language || '').toLowerCase();
  if ((tz.includes('Sao_Paulo') || tz.includes('Fortaleza') || tz.includes('Recife') || tz.includes('Manaus') || lang === 'pt-br' || lang === 'pt') && !location.pathname.startsWith('/pt-br')) {
    location.replace('/pt-br/');
  }
}
```

- [ ] **Step 2: Create `vercel.json`** (house lesson: NO `trailingSlash:true` — it breaks path rewrites)

```json
{
  "cleanUrls": true,
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" }
      ]
    }
  ]
}
```

- [ ] **Step 3: Full QA pass — both pages, both viewports**

Run:
```bash
node serve.mjs &
node screenshot.mjs http://localhost:3000 qa-en
node screenshot.mjs http://localhost:3000/pt-br/ qa-pt
```
Expected — check each screenshot in `./temporary screenshots/`:
- EN + pt-BR both render all 10 sections, on-brand (black bg, cyan accent, DM Sans headings).
- Desktop: hero 2-col, features 3-col, pricing 3-col with Explorer highlighted.
- Mobile (390): everything single-column, nav links hidden, CTAs full-width, no horizontal scroll.
- No console errors in either page.
- Logo wordmark shows `s`(white)`y`(cyan)`gnals`(white) everywhere.
- All CTA buttons read "Book a demo" (EN) / "Agende uma demonstração" (pt-BR); none say trial.

- [ ] **Step 4: Verify against spec success criteria**

Confirm each §10 criterion from the spec: single files render full page ✓, CTAs → demo ✓, mobile+desktop verified ✓, pricing matches board ✓, no render-blocking heavy JS ✓, brand rules honored ✓. Fix any miss before committing.

- [ ] **Step 5: Commit**

```bash
git add index.html vercel.json
git commit -m "feat: add geo-redirect and vercel config; final QA pass"
```

---

## Self-Review Notes

- **Spec coverage:** §6 sections 1–10 → Tasks 4–11; bilingual (§4) → Task 12; geo-redirect + toggle (§4) → Tasks 4/11/13; tokens/logo/buttons (§5) → Task 3; pricing board (§8) → Task 10; motion/reveal/reduced-motion (§7) → Tasks 3/11; responsive/a11y (§8) → per-section CSS + Task 13 QA; tooling/deploy (§4) → Tasks 1/13; blog (§9) → out of scope, no task (correct). Demo CTA (§3, no trial) → Tasks 5/10/11. All covered.
- **Placeholder scan:** demo link `cal.com/sygnals/demo` is an intentional, documented placeholder (spec §11), not a plan gap. Legal/blog `href="#"` are intentional stubs. No TBD code steps.
- **Type consistency:** `.iscore` card + `.badge` classes defined Task 5, reused Tasks 8/9. `toggleFaq`/`countUp`/`data-countup` defined Task 11 and referenced in markup from Task 5 onward (JS lands in Task 11 — reveal/countup inert until then, correct order). `.pre-reveal` defined Task 3, used throughout.
