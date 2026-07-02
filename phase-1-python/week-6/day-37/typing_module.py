from typing import List, Dict, Optional

def process_price(prices: List[float],discount: Optional[str] = None) -> Dict[str, float]:
    total = sum(prices)

    if discount == "SAVE10":
        total = total -10
    return {"final_amount": total}
result = process_price([100.0, 50.0], discount="SAVE10")
print(result)

from typing import Union
def process_id(item_id: Union[int, str]) -> str:
    if isinstance(item_id, int):
        return f"Processing item with ID: {item_id}"
    else:
        return f"Processing item with name: {item_id}"

print(process_id(123))
print(process_id("Laptop"))

from typing import Tuple, Dict
def get_location(city_name: str, city_database: Dict[str, Tuple[float, float]]) -> Tuple[float, float]:
    return city_database.get(city_name, (0.0, 0.0))
city_db = {
    "Indore": (22.7196, 75.8577),
    "Bhopal": (23.2599, 77.4126,500.0)
}
location = get_location("Bhopal", city_db)
print(location)

from typing import Tuple

def get_red() -> Tuple[int, int, int]:
    return (255, 0, 0)
red_color = get_red()
print(red_color)

from typing import Union

def double_it(val: Union[int, str]) -> str:
    return val * 2

print(double_it(3))