from ..strategy_abstract.get_content import GetContentStrategy
import logging
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service

logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

categories = [
    # "backend",
    # "frontend",
    # "fullstack",
    # "mobile",
    # "embedded",
    # "artificial-intelligence",
    # "data",
    # "data",
    # "business-intelligence",
    # "business-analyst",
    # "product-management",
    # "testing",
    # "devops",
    # "sys-administrator",
    # "security",
    # "architecture",
    # "game-dev",
    # "project-manager",
    # "agile",
    # "design",
    # "support",
    # "erp",
    # "other",
    # "hr",
    # "marketing",
    # "sales",
    # "finance",
    "office-administration",
    # "consulting",
    # "customer-service",
]


class GetNFJContent(GetContentStrategy):
    def __init__(self):
        service = Service(executable_path="chromedriver.exe")
        super().__init__(website="NFJ", base_url="https://nofluffjobs.com/pl")
        self.driver = webdriver.Chrome(service=service)

    def fetch_content(self) -> None:
        for category in categories:
            page = 1

            while True:
                url = f"{self.base_url}/{category}?page={page}"
                try:
                    self.driver.get(url)
                    content = self.driver.page_source

                    soup = BeautifulSoup(content, "html.parser")
                    jobs = soup.find("div", class_="list-container ng-star-inserted")

                    print(content)
                    self.data.append(content)
                    if page == 2:
                        break
                    page += 1

                except Exception as e:
                    print(e)

        self.driver.quit()
