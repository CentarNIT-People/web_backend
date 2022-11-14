from pymongo import ReturnDocument
from database.db import connect_to_db

db = connect_to_db("coworking")


class CoworkingLayer:

    @staticmethod
    def get_all() -> list[dict]:
        return list(db.find({}))

    def get_floor_by_number(self, floor_number: int):
        return db.find_one({"floor_number": floor_number})

    def create_floor(self, item: dict) -> dict:
        db.insert_one(item)
        return item

    def delete_floor(self, floor_number: str):
        return db.delete_one({"floor_number": int(floor_number)})

    def create_table(self, floor_number: str, item: dict):
        floor = self.get_floor_by_number(int(floor_number))
        floor["tables"].append(item)
        db.update_one({"floor_number": int(floor_number)}, {"$set": floor})
        return "Floor has been created on floor number " + str(floor_number)

    def delete_table(self, floor_number: str, table_number: str):
        floor = self.get_floor_by_number(int(floor_number))
        for x in floor["tables"]:
            if x["table_number"] == table_number:
                floor["tables"].remove(x)
        db.update_one({"floor_number": floor_number}, {"$set": floor})
        return "Table has been deleted on floor number " + str(floor_number)

    def update_table(self, floor_number: int, item: dict):
        floor = self.get_floor_by_number(floor_number)
        for x in floor["tables"]:
            if x["table_number"] == item["table_number"]:
                x.update(item)
        db.update_one({"name": floor_number}, {"$set": floor})
        return "Table has been updated on floor number " + str(floor_number)

    def get_table_by_number(self, floor_number: int, table_number: int):
        floor = self.get_floor_by_number(floor_number)
        for x in floor["tables"]:
            if x["table_number"] == table_number:
                return x
        return None

    def get_people_in_table(self, floor_number: int, table_number: int):
        floor = self.get_floor_by_number(floor_number)
        for x in floor["tables"]:
            if x["table_number"] == table_number:
                return x["people_in_table"]
        return None

    def action_to_table(self, item: dict, action: str):
        floor = self.get_floor_by_number(item["floor_number"])
        for x in floor["tables"]:
            if x["table_number"] == item["table_number"]:
                if action == "assign":
                    x["people_in_table"].append(item["username"])
                    floor["people"].append(item["username"])
                elif action == "remove":
                    x["people_in_table"].remove(item["username"])
                    floor["people"].remove(item["username"])
                else:
                    return None
                return db.find_one_and_update(
                    {"floor_number": item["floor_number"]}, {"$set": floor},
                    return_document=ReturnDocument.AFTER)
        return None
