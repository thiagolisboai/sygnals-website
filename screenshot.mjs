import puppeteer from 'puppeteer';

const url = process.argv[2] || 'http://localhost:3000';
const label = process.argv[3] || 'shot';
const CHROME = 'C:/Users/tlisb/.cache/puppeteer/chrome/win64-145.0.7632.77/chrome-win64/chrome.exe';

const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new' });
for (const [w, tag] of [[1440, 'desktop'], [390, 'mobile']]) {
  const page = await browser.newPage();
  await page.setViewport({ width: w, height: 900 });
  await page.goto(url, { waitUntil: 'domcontentloaded' });
  await new Promise(r => setTimeout(r, 1000));
  // A fullPage screenshot resizes/paints beyond the viewport without physically
  // scrolling, so scroll-triggered reveal (IntersectionObserver) never fires for
  // below-the-fold .pre-reveal content and it stays invisible in the PNG even
  // though real users scrolling the page see it normally. Force the same
  // end-state the reveal JS produces so the capture reflects real content.
  await page.evaluate(() => {
    document.querySelectorAll('.pre-reveal').forEach(el => {
      el.classList.remove('pre-reveal');
      el.classList.add('revealed');
      if (el.dataset && el.dataset.countup) el.textContent = el.dataset.countup;
    });
  });
  await new Promise(r => setTimeout(r, 300));
  await page.screenshot({ path: `./temporary screenshots/${label}-${tag}.png`, fullPage: true });
  await page.close();
}
await browser.close();
console.log('done');
