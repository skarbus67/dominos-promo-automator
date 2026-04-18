# Domino's Promo Automator 🍕

An automated tool for generating Domino's Pizza discount codes by automating newsletter signups using temporary email addresses.
The tool supports both full browser automation and high-speed HTTP requests bypassing anti-bot protections.

## 🚀 How It Works
1. The script chooses the execution mode based on configuration (Browser via Playwright or HTTP via curl_cffi).
2. It generates a unique, temporary email address via MailSlurp API.
3. Depending on the mode:
   - **Playwright**: Automates a real browser to navigate the site, accept cookies, and fill out the form.
   - **HTTP**: Fetches the site, parses CSRF tokens (e.g., __RequestVerificationToken), solves CAPTCHA using an external API (CapMonster), and sends a direct POST request.
4. It monitors the inbox for the activation link and validates the account.
5. It monitors the inbox for the subsequent email, extracts the promotional code, and displays it in the console.

## ⚙️ Setup (Installation & Configuration)

To run the project locally, make sure you have Python version 3.10 or newer installed.

1. Clone the repository:
   git clone https://github.com/skarbus67/dominos-promo-automator.git
   cd dominos-promo-automator

2. Create and activate a virtual environment:
   python -m venv venv

   **Windows:**
   venv\Scripts\activate

   **Linux/macOS:**
   source venv/bin/activate

3. Install the required libraries:
   pip install -r requirements.txt

4. Install browser drivers (required only if using Playwright mode):
   playwright install chromium

5. Configure the .env file:
   Create a .env file in the root folder to store configuration, using .env.example as an example.
   Make sure to configure your API keys and execution preferences

## 🛠️ Technology
- Python 3.x
- Playwright (browser automation)
- curl_cffi (HTTP requests with TLS impersonation)
- BeautifulSoup4 (HTML parsing and token extraction)
- CapMonster API (automated CAPTCHA solving)
- MailSlurp API (Professional Email Testing API)
- Regex (re) (Data parsing and extraction)
- Dotenv (configuration management)

## ⚠️ Disclaimer
This project was created for educational purposes only. The author is not responsible for any misuse of the script.

## ⚖️ License
MIT - Enjoy!