from schemas.coworking import Table, Floor
from database.data_access.coworking import CoworkingLayer

data_layer = CoworkingLayer()


class CoworkingLogic:

    @staticmethod
    def _parse_item(item: Floor or Table, id_name: str):
        item = dict(item)
        item["_id"] = item[id_name]
        return item

    @staticmethod
    def get_all() -> list[dict]:
        return data_layer.get_all()

    def get_floor_by_number(self, floor_number: int):
        return data_layer.get_floor_by_number(floor_number)

    def create_floor(self, item: Floor):
        item = self._parse_item(item, "floor_number")
        return data_layer.create_floor(item)
    
    def delete_floor(self, floor_number: int):
        return data_layer.delete_floor(floor_number)

    def create_table(self, floor_number: int, item: Table):
        parsed_item = self._parse_item(item, "table_number")
        return data_layer.create_table(floor_number, parsed_item)

    def get_table(self, floor_number: int, table_number: int):
        return data_layer.get_table_by_number(floor_number, table_number)

    def update_table(self, floor_number: int, request: Table):
        return data_layer.update_table(floor_number, dict(request))

    def delete_table(self, floor_number: int, table_number: int):
        return data_layer.delete_table(floor_number, table_number)

    def get_people_in_table(self, floor_number: int, table_number: int):
        return data_layer.get_people_in_table(floor_number, table_number)

    def add_person_to_table(self, item: dict, action: str):
        return data_layer.action_to_table(item, action)

    def remove_person_from_table(self, item: dict, action: str):
        return data_layer.action_to_table(item, action)
