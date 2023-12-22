from abc import abstractmethod, ABC


class GetContentStrategy(ABC):
    """
    Abstract base class for retrieving and saving content.

    Methods:
    - fetch_content: Retrieves the content.
    - save_to_db: Saves the content to a database.
    - __len__: Returns the length of the content.
    """

    def __init__(self, website: str, base_url: str):
        self.data = []
        self.website = website
        self.base_url = base_url

    @abstractmethod
    def fetch_content(self):
        pass

    def __len__(self):
        return len(self.data)
