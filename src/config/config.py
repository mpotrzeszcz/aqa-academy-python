import os


class Config:
    TIMEOUT_UI_ELEMENTS_SECONDS = 10


def __init__(self) -> None:
    if os.getenv("ENV") == "DEV":
        self.BASE_URL = "google.com"
