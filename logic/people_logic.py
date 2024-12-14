from db.people_db import PeopleDB

class PeopleLogic:
    db: PeopleDB

    def __init__(self, db: PeopleDB):
        self.db = db

    def all(self) -> list[str]:
        return self.db.all()
