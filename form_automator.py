from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError, Error as PlaywrightError
from config import ACCEPT_COOKIES_BUTTON_ID, EMAIL_INPUT_ID, CONSENTS_CHECKBOX_ID, RECIEVE_PROMO_BUTTON_NAME
from exceptions import AutomationError

class DominosSiteAutomator:

    def __init__(self):
        try:
            playwright_manager = sync_playwright()
            self.p = playwright_manager.start()
        except Exception as e:
            raise AutomationError(f"failed initializing playwright: {e}")


    def launch_dominos_site(self):
            try:
                self.browser = self.p.chromium.launch(headless=False)
                self.context = self.browser.new_context()
                self.page = self.context.new_page()
                self.page.goto("https://www.dominospizza.pl/korzysci/", timeout=10000)
            except PlaywrightTimeoutError:
                raise AutomationError("timeout: failed opening site")
            except PlaywrightError as e:
                raise AutomationError(f"browser error while opening site: {e}")
            
    def accept_cookies(self):
        try:
            self.page.locator(f"#{ACCEPT_COOKIES_BUTTON_ID}").click(timeout=10000)
        except PlaywrightTimeoutError:
            raise AutomationError("timeout: failed finding accept cookies button")

    def check_consents(self):
        try:
            self.page.locator(f'label[for="{CONSENTS_CHECKBOX_ID}"]').click(timeout=10000)
        except PlaywrightTimeoutError:
            raise AutomationError("timeout: failed finding consents checkbox")

    def submit_form(self):
        try:
            self.page.get_by_role("button", name=RECIEVE_PROMO_BUTTON_NAME).click(timeout=10000)
        except PlaywrightTimeoutError:
            raise AutomationError("timeout: failed finding submit button")

    def close_current_page(self):
        try:
            if self.page:
                self.page.close()
                self.page = None
        except PlaywrightError as e:
            raise AutomationError(f"failed closing current page: {e}")

    def fill_email(self, email):
        try:
            self.page.locator(f"#{EMAIL_INPUT_ID}").fill(email, timeout=5000)
        except PlaywrightTimeoutError:
            raise AutomationError("timeout: failed finding email input")

    def launch_activation_site(self, url):
        try:
            self.page = self.context.new_page()
            self.page.goto(url)
        except PlaywrightError as e:
            raise AutomationError(f"failed closing current page: {e}")

    def stop_playwright(self):
        try:
            if self.context:
                self.context.close()
            if self.browser:
                self.browser.close()
            self.p.stop()
        except Exception as e:
            raise AutomationError(f"failed stopping playwright: {e}")

