from . import UiState
from logic.people_logic import PeopleLogic

class PeopleTable(UiState):
    logic: PeopleLogic

    def __init__(self, logic: PeopleLogic):
        self.logic = logic

    def render(self):
        print("People Table")
        print("-----------")
        for person in self.logic.all():
            print(person)
        print("-----------")
        print("q. Exit")

    def input(self) -> UiState | None:
        val = input("Option: ")
        if val == "q":
            return None
