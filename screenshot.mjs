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
