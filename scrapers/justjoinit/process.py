from ..strategy_abstract.process import Process
from typing import List, Optional, Tuple, Dict
from bs4 import BeautifulSoup
from scraper import (
    ParsedOffer,
    Salary,
    Addresses
)
from dataclasses import asdict


class JJITProcess(Process):
    def __init__(self, html):
        super().__init__()
        self.html = html
        self.scraped_data = None
        self.parsed_data = {}
        self.parse_html()
        self.process()

    def parse_html(self) -> None:
        soup = BeautifulSoup(self.html, "html.parser")

        if not soup:
            return

        title_element = soup.find("h2", class_="css-16gpjqw")
        url_element = soup.find("a", class_="css-4lqp8g")
        salary_element = soup.find("div", class_="css-1b2ga3v")
        skill_elements = soup.find_all("div", class_="css-1u7edaj")
        skills = [skill.text for skill in skill_elements]
        localization_element = soup.find("div", class_="css-68pppj")
        company_logo_div = soup.find("div", class_="css-1hudrbb")
        company_logo = company_logo_div.find("img")
        company_name_div = soup.find("div", class_="css-ldh1c9")
        company_name = company_name_div.find("span")

        if title_element:
            self.parsed_data["title"] = title_element.text
        if url_element:
            self.parsed_data["url"] = url_element["href"]
        if salary_element:
            self.parsed_data["salary"] = salary_element.text
        if skills:
            self.parsed_data["skills"] = skills
        if localization_element:
            self.parsed_data["localization"] = localization_element.text
        if company_logo:
            self.parsed_data["company_logo"] = company_logo["src"]
        if company_name:
            self.parsed_data["company_name"] = company_name.text

    @staticmethod
    def process_salary(salary: str) -> Tuple[Optional[int], Optional[int]]:
        if "Undisclosed" in salary:
            return None, None
        salary = salary.replace("pln", "")

        if "-" in salary:
            text = salary.split("-")
            num1, num2 = text
            return int(num1.replace(" ", "")), int(num2.replace(" ", ""))
        else:
            return int(salary.replace(" ", "")), None

    @staticmethod
    def process_skills(skills: List[str]) -> Optional[str]:
        to_delete = ["New", "Fully remote"]
        if not skills:
            return None
        skills = [element for element in skills if element not in to_delete]
        return " ".join(skills)

    @staticmethod
    def process_localization(localization: Optional[str]) -> Optional[str]:
        if not localization:
            return None
        if ", " in localization:
            return localization.split(", ")[0]
        else:
            return localization

    def process(self) -> Dict:
        title = self.parsed_data.get("title")
        url = self.parsed_data.get("url")
        salary = self.parsed_data.get("salary")
        skills = self.parsed_data.get("skills")
        localization = self.parsed_data.get("localization")
        company_logo = self.parsed_data.get("company_logo")
        company_name = self.parsed_data.get("company_name")

        text_to_process = f"{title} {skills}"

        salary_from, salary_to = self.process_salary(salary)
        is_remote = self.is_remote(text_to_process)
        is_hybrid = self.is_hybrid(text_to_process)
        processed_skills = self.process_skills(skills)
        processed_localization = self.process_localization(localization)
        experiences = self.get_experience_level(title)
        localization = Addresses(city=processed_localization)

        # currency and schedule is hard coded due to the specificity of the website
        salary = Salary(
            salary_from=salary_from,
            salary_to=salary_to,
            currency="PLN",
            schedule="MONTHLY",
        )
        offer = ParsedOffer(
            title=title,
            description=None,
            addresses=[localization],
            is_remote=is_remote,
            is_hybrid=is_hybrid,
            skills=processed_skills,
            salary=[salary],
            experience=experiences,
            work_type=None,
            employment_type=None,
            company_logo=company_logo,
            url=f"https://justjoin.it{url}",
            company_name=company_name,

        )
        self.scraped_data = asdict(offer)
