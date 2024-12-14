import os
import json

DEFAULT_DB_PATH = os.getenv("DB_PEOPLE_PATH", "data/people.json") 

class PeopleDB:
    path: str

    def __init__(self, path: str = DEFAULT_DB_PATH):
        self.path = path

    def all(self) -> list[str]:
        with open(self.path) as f:
            content = json.loads(f.read())
            return content
