#!/usr/bin/env node

const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function convertHtmlToPdf() {
    const scriptDir = __dirname;
    const htmlFile = path.join(scriptDir, 'index.html');
    const pdfFile = path.join(scriptDir, 'Koorosh_Komeili_Zadeh_CV.pdf');

    if (!fs.existsSync(htmlFile)) {
        console.error(`Error: HTML file not found at ${htmlFile}`);
        process.exit(1);
    }

    console.log(`Converting ${htmlFile} to PDF...`);

    const browser = await puppeteer.launch({
        headless: 'new',
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    const page = await browser.newPage();
    
    await page.setViewport({
        width: 794,
        height: 1123,
        deviceScaleFactor: 2
    });

    await page.goto(`file://${htmlFile}`, {
        waitUntil: 'networkidle0'
    });

    await new Promise(resolve => setTimeout(resolve, 2000));

    await page.pdf({
        path: pdfFile,
        format: 'A4',
        margin: {
            top: '5mm',
            bottom: '5mm',
            left: '5mm',
            right: '5mm'
        },
        printBackground: true,
        preferCSSPageSize: false,
        displayHeaderFooter: false,
        scale: 1.0
    });

    await browser.close();

    console.log(`PDF created: ${pdfFile}`);
}

(async () => {
    try {
        await convertHtmlToPdf();
    } catch (error) {
        console.error(`Error: ${error.message}`);
        process.exit(1);
    }
})();
