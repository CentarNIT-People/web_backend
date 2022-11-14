from schemas.coworking import Floor, Table
from logic.coworking import CoworkingLogic

coworking_logic = CoworkingLogic()


def get_all():
    return coworking_logic.get_all()


def create_floor(item: Floor):
    return coworking_logic.create_floor(item)


def delete_floor(floor_number: int):
    return coworking_logic.delete_floor(floor_number)


def get_floor_by_number(floor_number: int):
    return coworking_logic.get_floor_by_number(floor_number)


def create_table(floor_number: int, item: Table):
    return coworking_logic.create_table(floor_number, item)


def get_table(floor_number: int, table_number: int):
    return coworking_logic.get_table(floor_number, table_number)


def update_table(floor_number: int, request: Table):
    return coworking_logic.update_table(floor_number, request)


def delete_table(floor_number: int, table_number: int):
    return coworking_logic.delete_table(floor_number, table_number)


def get_people_in_table(floor_number: int, table_number: int):
    return coworking_logic.get_people_in_table(floor_number, table_number)


def add_person_to_table(item: dict, action: str):
    return coworking_logic.add_person_to_table(item, action)


def remove_person_from_table(item: dict, action: str):
    return coworking_logic.remove_person_from_table(item, action)
