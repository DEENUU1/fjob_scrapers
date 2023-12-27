from abc import abstractmethod, ABC
from typing import List, Optional, Dict, Any
from scraper import ParsedOffer
# from offers.models import (
#     Website,
#     ExperienceLevel,
#     Salaries,
#     Localization,
#     Offers,
#     ContractType,
#     WorkSchedule,
# )
from datetime import datetime


class Process(ABC):
    def __init__(self):
        self.processed_data: List[ParsedOffer] = []

    @abstractmethod
    def parse_html(
        self, html: List[Optional[str]] | Optional[str] | Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    @abstractmethod
    def process(self) -> ParsedOffer | List[Optional[ParsedOffer]]:
        pass

    @staticmethod
    def get_currency(text: str) -> Optional[str]:
        currencies = ["PLN", "EUR", "USD"]
        for occurrence in currencies:
            if occurrence in text:
                return occurrence

    @staticmethod
    def is_hybrid(text: str) -> bool:
        text.lower()
        if "hybrid" in text or "hybrydowa" in text:
            return True
        return False

    @staticmethod
    def is_remote(text: str) -> bool:
        text.lower()
        if "remote" in text or "zdalnie" in text:
            return True
        return False

    @staticmethod
    def get_experience_level(text: str) -> List[Optional[str]]:
        result = []
        if not text:
            return result

        text = text.lower()

        data = {
            "Intern": [
                "intern",
                "stażysta",
                "staż",
                "praktykant",
                "stażysta",
                "praktykant/stażysta",
                "praktykant / stażysta",
            ],
            "Junior": ["młodszy", "junior", "młodszy specjalista"],
            "Expert": ["ekspert", "expert"],
            "Assistant": ["asystent", "asystentka"],
            "Mid": ["mid", "regular", "specjalista (mid / regular)"],
            "Senior": ["senior", "starszy"],
            "Lead": ["lead", "kierownik", "kierownik/koordynator", "koordynator"],
            "Director": ["dyrektor", "director"],
            "Manager": ["manager", "menadżer"],
            "Worker": ["pracownik fizyczny", "worker"],
            "CEO": [
                "prezes",
            ],
        }

        for p, f in data.items():
            for x in f:
                if x in text:
                    result.append(p)

        return result
