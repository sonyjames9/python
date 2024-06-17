from typing import List, Tuple, Optional

# The type annotations used for each function parameter with input and output types
def process_data(data: List[int]) -> Tuple[int, int]:
    return (min(data), max(data))


def find_max(data: Optional[List[int]] = None) -> Optional[int]:
    if data:
        return max(data)
    return None
