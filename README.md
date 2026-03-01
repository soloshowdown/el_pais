## El País Selenium Automation Project

### Features
- Scrapes Opinion articles
- Verifies Spanish language
- Downloads article images
- Translates titles to English
- Identifies repeated words
- Runs locally and on BrowserStack

## Tech Stack Used

- **Programming Language:** Python 3  
- **Web Automation / Scraping:** Selenium WebDriver  
- **Browser Drivers:** ChromeDriver (local), BrowserStack Remote WebDriver  
- **HTTP Requests:** requests (for downloading images)  
- **Translation API:** Google Translate (via `googletrans` library)  
- **Text Analysis:** Python standard libraries (`re`, `collections.Counter`)  

### Local Execution
```bash
pip install -r requirements.txt
python main.py --articles 5
```

## Notes

- Generated files (JSON outputs, logs) are excluded from version control using `.gitignore`.
- A small set of scraped images and screenshots are included only for assignment review and verification purposes.
  
### Screenshots

![Screenshot 1](screenshots/img1.png)
![Screenshot 2](screenshots/img2.png)
![Screenshot 3](screenshots/img3.png)
![Screenshot 4](screenshots/img4.png)
![Screenshot 5](screenshots/img5.png)

## Scraped Article Images

![Article Image](screenshots/article_2.jpg)
![Article Image](screenshots/article_4.jpg)
![Article Image](screenshots/article_5.jpg)

## Issues Faced During Implementation

1. **Cookie Consent Popups**  
   While scraping El País, cookie consent banners sometimes blocked access to page content.  
   This was handled by allowing page load completion and interacting with visible elements only after cookies were accepted or bypassed.

2. **Inconsistent Article Heading Structure (H1 / H2)**  
   Some Opinion articles used a generic `H1` tag such as *"Opinión"* instead of the actual headline.  
   In such cases, the scraper correctly extracted the main `H1` element as per DOM structure, which resulted in repeated titles.(Screenshot 5).  
   This behavior was expected and handled during repeated-word analysis.
