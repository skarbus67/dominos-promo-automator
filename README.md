# Domino's Promo Automator 🍕

An automated tool for generating Domino's Pizza discount codes by automating newsletter signups using temporary email addresses.

## 🚀 How It Works
1. The script generates a unique, temporary email address via API.
2. It automatically fills out the newsletter signup form on the Domino's website.
3. It monitors the inbox for the email containing the code.
4. It extracts the promotional code and displays it in the console.

## ⚙️ Setup (Installation & Configuration)

To run the project locally, make sure you have Python version 3.10 or newer installed.

1. Clone the repository:
   git clone https://github.com/skarbus67/dominos-promo-automator.git
   cd dominos-promo-automator

2. Create and activate a virtual environment:
   python -m venv venv
   **Windows**: venv\Scripts\activate

   **Linux/macOS**: source venv/bin/activate

3. Install the required libraries:
   pip install -r requirements.txt

4. Install browser drivers :
   playwright install chromium

5. Configure the .env file (optional):
   Create a .env file in the root folder to store configuration, using .env.example as an example.

## 🛠️ Technology
- Python 3.x
- Playwright (browser automation)
- MailSlurp API (Professional Email Testing API)
- Regex (re) (Data parsing and extraction)
- Dotenv (configuration management)

## ⚠️ Disclaimer
This project was created for educational purposes only. The author is not responsible for any misuse of the script.

## ⚖️ License
MIT - Enjoy!