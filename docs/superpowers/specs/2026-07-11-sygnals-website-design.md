# Sygnals Marketing Website — Design Spec

**Date:** 2026-07-11
**Status:** Approved (structure), pending spec review
**Owner:** thiago@tracquisition.com

## 1. Purpose

Public marketing landing page for **Sygnals** — a B2B SaaS that monitors LinkedIn
engagement, scores buying intent in real time, and delivers warm/qualified leads.
Goal of the page: convert **B2B founders and sales-led SMBs** into **booked demos**
(no self-serve free trial at launch).

Product is launching soon; this is the acquisition front door.

## 2. Positioning

- **ICP:** B2B founders and small sales teams doing outbound on LinkedIn. Pain: wasting
  time and reputation on cold leads with no timing signal.
- **Core promise (hero hook):** *timing / intent* — "Reach out the moment they show
  buying intent."
- **Mechanism:** Sygnals watches LinkedIn activity of people you choose to monitor,
  computes an **Intent Score** (frequency, seniority, engagement type, recency), and
  surfaces **Hot (80–100)** and **Warm (60–79)** leads before competitors notice.

## 3. Scope

**In scope (this build):** ONE static long-form landing page, bilingual (EN + pt-BR).

**Out of scope (documented, not built now):**
- Blog (see §9 — recommended as a separate Next.js project, CHATTIE pattern).
- App/dashboard itself (lives in `SYGNALS APP`).
- Auth, billing, self-serve signup — **no free trial at launch.** Every primary CTA is
  **"Book a demo" / "Agende uma demonstração"** pointing to a demo-booking flow
  (Cal.com embed, TRA pattern — link TBD in §11).

## 4. Tech & Output

- **Single `index.html`** (EN) + **`pt-br/index.html`** (pt-BR), each self-contained:
  inline `<style>`, inline SVG logo, minimal inline/vanilla JS. Matches the
  TAISA/CHATTIE/TRA/INCHAT house pattern — fast, PSI-friendly, trivial to deploy on
  Vercel as a static site.
- **Fonts:** DM Sans (700 — headings/CTAs/logo wordmark) + Inter (400/500/600 —
  body/UI/labels) via Google Fonts `<link>` with preconnect. `ui-monospace` for data.
- **No build step, no framework** for the landing page.
- **Language routing:** English is the default (`/`); pt-BR at `/pt-br/`. A geo-redirect
  script sends BR visitors to `/pt-br/` (INCHAT pattern), with a manual EN/pt-BR toggle
  in the footer that overrides via `localStorage` so the choice sticks.
- **Assets:** brand SVG logo inlined (spec below). `brand_assets/` already present.

## 5. Visual Design System (locked to brand guidelines)

| Token | Value | Use |
|-------|-------|-----|
| `--cyan` | `#00d4f5` | Primary accent (dark bg) |
| `--cyan-lt` | `#0094b3` | Accent on light surfaces only |
| `--black` | `#000000` | Page background base |
| `--surf` | `#0a0a0a` | Panels / alternating sections |
| `--elev` | `#181818` | Cards / dropdowns |
| `--border` | `#1a1a1a` | Hairlines |
| `--border2` | `#262626` | Stronger borders / secondary btn |
| `--text` | `#edf2f5` | Body text |
| `--muted` | `#9f9f9f` | Secondary text |
| `--green` | `#00c758` | Success / Active status |
| `--red` | `#ff2323` | Hot intent |
| `--amber` | `#edb200` | Warm intent / warnings |
| `--blue` | `#47a8ff` | Partial status |

**Rules from brand guidelines (must honor):**
- Logo: inline SVG only, `dominant-baseline="middle"`, stroke 3.2, `butt`/`miter`,
  dot `cx=18 cy=5.5 r=3.6`. Never rotate/distort, never swap DM Sans, never
  `stroke-linecap="round"`. `#00d4f5` on dark, `#0094b3` on light. Min full logo 172px.
- Wordmark: `s` white · `y` cyan · `gnals` white.
- Buttons: pill (`border-radius:999px`), DM Sans 700. Primary = cyan bg / black text.
  Secondary = transparent / `#262626` border. Focus ring
  `box-shadow: 0 0 0 2px #000, 0 0 0 4px #00d4f5`.
- Intent badges: Hot (red tint), Warm (amber tint). Status: Active/New/Partial/Paused.
- Aesthetic: dark throughout (approved "Match app — dark"). Subtle cyan radial glow
  behind hero; hairline-bordered sections; monospace for numbers/data. Restrained,
  premium, "instrument panel" feel — not a gradient-heavy generic SaaS page.

## 6. Page Structure (approved spine)

Each section is an independent, self-contained block. Reveal-on-scroll via
IntersectionObserver (house pattern: `.pre-reveal` opacity/translateY removed in view).

1. **Navbar (sticky)** — inline logo left; anchor links (How it works, Features,
   Pricing, FAQ); language toggle; "Start free" primary CTA. Condenses on scroll.
2. **Hero** — eyebrow "LinkedIn intent signals"; H1 "Reach out the **moment** they show
   buying intent."; subcopy; dual CTA (**Book a demo** [primary] / See how it works
   [secondary, scrolls to §4]); supporting visual = a live **Intent Score** card + mini
   signal list (built from brand UI components). Cyan radial glow, faint animated
   waveform accent.
3. **Problem** — "Cold outreach is a numbers game you lose." 2–3 concise pain points
   (no timing, no signal, wasted credits & reputation). Muted, tight.
4. **How it works — 3 steps** — (1) Choose who to monitor · (2) Sygnals watches LinkedIn
   engagement · (3) Intent Score surfaces Hot/Warm leads. Numbered, waveform connector.
5. **Intent Score showcase** — signature section. Animated score-breakdown card
   (Frequência +30, Seniority +40, Tipo +20, Recência −17 → **73 Warm**) exactly per
   brand guideline component, with a short explainer of each factor. This is the
   product's "wow".
6. **Features grid** — 6 cards: Signal monitoring, Intent scoring, LinkedIn account
   connect, Credit-based usage, CSV/Clay export & webhooks, Real-time alerts. Icons via
   inline SVG (cyan line style consistent with the mark).
7. **Product / dashboard preview** — framed mock of signal list (Active/Partial/
   Updating/Paused rows) + credit-usage meter, straight from brand components. Sells the
   real UI without a screenshot dependency.
8. **Pricing** — 3 cards (Explorer highlighted as recommended):

   | Plan | $/mo | Credits/mo | Signals | LI accounts |
   |------|------|-----------|---------|-------------|
   | Starter | $99 | 10,000 | 10 | 1 |
   | Explorer | $179 | 25,000 | 20 | 3 |
   | Pro | $349 | 50,000 | 40 | 10 |

   **No free-trial callout** (no self-serve at launch). Each plan card's CTA = **Book a
   demo**. Note: overage $12–15/1k, LI-account add-on $15/mo. USD shown by default;
   pt-BR page notes BR billing is in BRL. (Numbers sourced from the owner-locked pricing
   board — the single source of truth.)
9. **FAQ** — accordion: Is it LinkedIn-compliant? · What is a credit? · Which LinkedIn
   accounts can I connect? · How is Intent Score calculated? · Can I cancel anytime? ·
   EN/pt-BR billing. First item open by default.
10. **Final CTA + Footer** — dark waveform band, repeat "Book a demo" CTA, footer with
    product/legal/social links, inline logo, EN/pt-BR toggle, copyright.

## 7. Interaction & Motion

- Reveal-on-scroll (IntersectionObserver) — subtle opacity + 12px translateY.
- Hero waveform: gentle CSS animation on the mark path (respect
  `prefers-reduced-motion`).
- Intent Score card: numbers count up / bar fills when scrolled into view.
- FAQ accordion: `toggleFaq()`, closes siblings on open.
- Sticky nav condense on scroll.
- Sub-desktop: single-column stacking; all animations gated to keep mobile PSI high
  (house lesson from CHATTIE PSI work — no heavy JS on mobile).

## 8. Responsiveness & Accessibility

- Fluid type with `clamp()`. Breakpoints at 900px (tablet) and 600px (mobile).
- Body scroll never horizontal; wide tables/mocks scroll inside their own container.
- Contrast: cyan `#00d4f5` on black passes; never cyan on white (use `#0094b3`).
- Keyboard focus rings on all interactive elements (brand focus-ring spec).
- `prefers-reduced-motion` disables non-essential animation.
- Semantic landmarks, alt text, `lang` attribute per page.

## 9. Blog decision (evaluated per user request)

**Recommendation: YES — keep the blog as a separate Next.js project**, do not fold it
into this static landing page. Rationale:

- The landing page benefits from being a zero-build static file (max PSI, trivial
  deploy) — no reason to drag a framework in for it.
- A content blog benefits from MDX, layouts, and tooling — exactly the CHATTIE BLOG
  pattern already in use (Next.js 15, MDX posts, rewrites from the main site's
  `vercel.json` so the blog serves under `/blog`).
- Two concerns, two deploys, one shared brand token set (copy the CSS variables from §5
  into the blog theme). This isolates PSI-sensitive marketing from content churn.

**Not built in this task.** Tracked as the next sub-project: `SYGNALS BLOG` (Next.js 15,
MDX), wired via `vercel.json` rewrites to `/blog` once the landing page is live. Its own
spec → plan cycle.

## 10. Success Criteria

- Single `index.html` (EN) + `pt-br/index.html` render the full 10-section page, on-brand,
  no console errors.
- All primary CTAs open the "Book a demo" flow (Cal.com embed / link, §11).
- Mobile + desktop layouts verified via screenshot (Puppeteer house tooling).
- Pricing numbers match the owner-locked board exactly.
- Lighthouse/PSI: green performance on mobile (no render-blocking heavy JS).
- Brand rules in §5 honored (logo, fonts, colors, buttons).

## 11. Open Items (confirm during/after build)

- **Demo-booking link** for all CTAs — Cal.com embed (TRA pattern). Which Cal handle/
  event? Placeholder `cal.com/sygnals/demo` until confirmed.
- **Domain** for the marketing site (e.g. `sygnals.com`) — affects geo-redirect + canonical.
- **Currency display** on pt-BR: show BRL prices or USD-with-note? (Spec assumes
  USD + note; can localize to BRL if prices are known.)
- Social/legal link targets (privacy, terms) — stub pages or external.
