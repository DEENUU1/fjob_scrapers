from abc import abstractmethod, ABC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


SERVICE = Service(executable_path="chromedriver")
CHROME_OPTIONS = Options()
# CHROME_OPTIONS.add_argument("--headless")


class GetContentStrategy(ABC):
    def __init__(self, base_url: str):
        self.data = []
        self.base_url = base_url
        self.service = SERVICE
        self.options = CHROME_OPTIONS

    @abstractmethod
    def fetch_content(self):
        pass

    def __len__(self):
        return len(self.data)
