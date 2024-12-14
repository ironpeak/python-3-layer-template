from . import UiState
from .people_table import PeopleTable
from logic.people_logic import PeopleLogic
from db.people_db import PeopleDB

class MainMenu(UiState):
    def __init__(self):
        pass

    def render(self):
        print("Main Menu")
        print("-----------")
        print("1. People Table")
        print("q. Exit")

    def input(self) -> UiState | None:
        val = input("Option: ")
        if val == "1":
            return PeopleTable(PeopleLogic(PeopleDB()))
        elif val == "q":
            return None
