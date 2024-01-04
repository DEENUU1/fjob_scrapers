from abc import abstractmethod, ABC
from typing import List, Optional

from schemas import ParsedOffer


class Process(ABC):
    def __init__(self):
        self.processed_data: List[ParsedOffer] = []

    @abstractmethod
    def parse_html(self) -> None:
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
            "Assistant": ["asystent", "asystentka", "assistant"],
            "Junior": ["młodszy", "junior", "młodszy specjalista"],
            "Mid": ["mid", "regular", "specjalista (mid / regular)"],
            "Senior": ["senior", "starszy"],
            "C-level": ["c-level", "clevel"],
            "Expert": ["expert", "ekspert"],
            "Manager": ["manager", "menadżer"],
        }

        for p, f in data.items():
            for x in f:
                if x in text and x not in result:
                    result.append(p)

        return result

    @staticmethod
    def get_employment_type(text: str) -> List[Optional[str]]:
        result = []
        if not text:
            return result

        text = text.lower()

        data = {
            "B2B": ["B2B", "contract", "kontrakt"],
            "Permanent": ["umowa o pracę", "umowa o prace"],
            "Mandate contact": [],
            "Specific-task contact": ["umowa o dzieło", "umowa o dzielo"]
        }

        for p, f in data.items():
            for x in f:
                if x in text and x not in result:
                    result.append(p)

        return result

    @staticmethod
    def get_work_type(text: str) -> List[Optional[str]]:
        result = []
        if not text:
            return result

        text = text.lower()

        data = {
            "Full-time": ["full-time", "full-time", "pełny etat", "pelny etat"],
            "Part-time": ["part-time", "part-time", "pół etatu", "pol etatu"],
            "Freelance": ["freelance", "freelance"],
        }

        for p, f in data.items():
            for x in f:
                if x in text and x not in result:
                    result.append(p)

        return result

