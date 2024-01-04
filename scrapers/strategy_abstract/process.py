from abc import abstractmethod, ABC
from typing import List, Optional

from schemas import ParsedOffer


class Process(ABC):
    def __init__(self):
        self.processed_data: List[ParsedOffer] = []

    @abstractmethod
    def parse_html(self) -> None:
        """ Abstract method to parse HTML code """
        pass

    @abstractmethod
    def process(self) -> ParsedOffer | List[Optional[ParsedOffer]]:
        """ Abstract method to process data """
        pass

    @staticmethod
    def get_currency(text: str) -> Optional[str]:
        """ Get currency from text """
        currencies = ["PLN", "EUR", "USD"]
        for occurrence in currencies:
            if occurrence.lower() in text.lower():
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
            "Intern": ["intern", "stażysta", "staż", "praktykant", "praktykant/stażysta", "praktykant / stażysta"],
            "Assistant": ["asystent", "asystentka", "assistant"],
            "Junior": ["młodszy", "junior", "młodszy specjalista"],
            "Mid": ["mid", "regular", "specjalista (mid / regular)"],
            "Senior": ["senior", "starszy"],
            "C-level": ["c-level", "clevel"],
            "Expert": ["expert", "ekspert"],
            "Manager": ["manager", "menadżer"],
        }

        for p, f in data.items():
            if any(x in text for x in f):
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
            if any(x in text for x in f):
                result.append(p)

        return result

    @staticmethod
    def get_work_type(text: str) -> List[Optional[str]]:
        result = []
        if not text:
            return result

        text = text.lower()

        data = {
            "Full-time": ["full-time", "pełny etat", "pelny etat"],
            "Part-time": ["part-time", "pół etatu", "pol etatu"],
            "Freelance": ["freelance"],
        }

        for p, f in data.items():
            if any(x in text for x in f):
                result.append(p)

        return result
