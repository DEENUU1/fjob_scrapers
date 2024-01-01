from abc import abstractmethod, ABC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

SERVICE = Service(executable_path=ChromeDriverManager().install())


class GetContentStrategy(ABC):
    def __init__(self, base_url: str):
        self.data = []
        self.base_url = base_url
        self.service = SERVICE

    @abstractmethod
    def fetch_content(self):
        pass

    def __len__(self):
        return len(self.data)
