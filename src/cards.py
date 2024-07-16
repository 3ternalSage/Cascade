import datetime as dt
from datetime import date, time, datetime

class CardInformation:
    def __init__(self) -> None:
        self.front: str = None
        self.back: str = None

class Card:
    def __init__(self) -> None:
        self.card_info: CardInformation = CardInformation()

        self.card_added: date = None
        self.first_review: date = None
        self.latest_review: date = None
        
        self.status: str = 'new'
        self.difficulty: int = 100
        self.interval_factor: int = 100

        self.next_review: datetime = None

        self.num_reviews: int = 0
        self.average_review_time: time = None
        self.total_review_time: time = None


