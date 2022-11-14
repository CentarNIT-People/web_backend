from pydantic import BaseModel


class Floor(BaseModel):
    floor_number: int
    tables: list


class Table(BaseModel):
    table_number: int
    section: int  # 1, 2, 3
    price: int
    seats: int
    people_in_table: list  # list of people in table
    with_monitor: bool
    is_available: bool
    orientation: str  # "vertical", "horizontal"
    is_booked: bool


class UserInTable(BaseModel):
    floor_number: int
    table_number: int
    username: str
