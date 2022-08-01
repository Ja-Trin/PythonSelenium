import json
from typing import List


class JsonUtil:
    @staticmethod
    def read_json_from_resources(json_name: str) -> List[str]:
        with open(json_name, 'r') as f:
            file = json.load(f)
        return file
