# 🛒 Price Tracker with Alerts (Amazon & E-commerce)

A **headless browser–based price tracker** that monitors product prices on Amazon (and extendable to other e-commerce sites), stores price history in a local database, and alerts you when prices drop below your set threshold.  

This project is designed to **showcase backend engineering, automation, and system design skills**—perfect for an **SDE I role at Amazon**.  

---

## ✨ Features

- ✅ **Headless Browser Scraping** using Selenium (handles dynamic content & JavaScript).  
- ✅ **URL Normalization** (stable `/dp/ASIN` links for Amazon).  
- ✅ **SQLite Database** for persistent price history.  
- ✅ **Threshold Alerts** (console or email notifications).  
- ✅ **Modular Design** (easily extendable to Flipkart, eBay, etc.).  
- ✅ **Robust Selectors** (handles multiple Amazon layouts).  

---

## 🏗️ Tech Stack

- **Python 3**  
- **Selenium (Headless Chrome)**  
- **SQLite3**  
- **BeautifulSoup4** (optional, for lightweight scrapers)  

---

## 🚀 Setup

1. **Clone repo**  
   ```bash
   git clone https://github.com/yourusername/price-tracker.git
   cd price-tracker
   ```

2. **Install dependencies**  
   ```bash
   pip install selenium requests beautifulsoup4
   ```

3. **Install WebDriver**  
   - **Linux**:  
     ```bash
     sudo apt install chromium-driver   # Ubuntu/Debian
     sudo pacman -S chromedriver        # Arch
     ```
   - **Windows/Mac**: Download from [ChromeDriver](https://chromedriver.chromium.org/) and add to PATH.

---

## ⚡ Usage

1. Run the tracker:  
   ```bash
   python tracker.py
   ```

2. Enter product details:  
   ```
   Enter product URL: https://www.amazon.in/Apple-iPhone-14/dp/B0BDJ6ZN8T
   Enter price threshold: 60000
   ```

3. Example output:  
   ```
   [INFO] Current price: 62999.0
   ✅ Price still above threshold: 62999.0
   ```

   If the price drops:  
   ```
   🔥 ALERT! Price dropped below 60000: 58999.0
   ```

---

## 📊 Database

- SQLite database: `prices.db`  
- Table: `prices (id, url, price, timestamp)`  
- Logs all historical prices for analysis.  

---

## 📨 Email Alerts (Optional)

Enable email alerts by adding Gmail SMTP config in `tracker.py`:  

```python
send_email_alert(price, url)
```

Use **App Passwords** (not raw Gmail password).  

---

## 🛠️ Project Challenges & Solutions

| Challenge | Solution |
|-----------|----------|
| Dynamic HTML / JavaScript rendering | Used **Selenium headless browser** |
| Random `None` values in scraping | Multiple selectors (`a-price-whole`, `a-offscreen`, etc.) |
| Amazon URLs changing | **Normalized to `/dp/<ASIN>`** |
| Anti-bot measures | Added headers, headless browser, retries |

---

## 🎯 Why This Project for Amazon SDE I?

- **Customer Obsession**: Helps users save money with alerts.  
- **Dive Deep**: Handles real-world scraping issues (dynamic pages, changing URLs).  
- **Invent & Simplify**: Normalized URLs, modular scraper.  
- **Deliver Results**: Working end-to-end system with automation & persistence.  

This project demonstrates **backend engineering, system design, and automation skills**—aligned with Amazon’s bar-raising expectations.  

---

## 📌 Next Steps (Future Enhancements)

- 🔄 Multi-site support (Flipkart, eBay, etc.).  
- 📊 Web dashboard for visualization (Flask/React).  
- 🕒 Scheduled automation with CRON/Task Scheduler.  
- 📦 Dockerize for deployment.  

---

## 🗂️ Architecture Diagram

```mermaid
flowchart TD
    A[User Input: Product URL + Threshold] --> B[Headless Scraper (Selenium)]
    B --> C[Normalize URL (/dp/ASIN)]
    C --> D[Extract Price]
    D --> E[SQLite Database: Save Price History]
    E --> F[Compare with Threshold]
    F -->|Price >= Threshold| G[No Alert]
    F -->|Price < Threshold| H[Trigger Alert: Console/Email]
```