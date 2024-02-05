import os
from typing import List

from dotenv import load_dotenv

load_dotenv()


class ValueProvider:

    @classmethod
    def get_email(cls) -> str:
        return os.getenv("EMAIL")

    @classmethod
    def get_password(cls) -> str:
        return os.getenv("PASSWORD")

    @classmethod
    def get_list_of_sources(cls) -> list[str]:
        sources = [
            "16",
            # "19",
            # "22",
            # "26",
            # "49",
            # "70",
            # "92",
            # "93",
            # "101",
            # "102",
            # "123",
            # "139",
            # "170",
            # "209",
            # "224",
            # "233",
            # "261",
            # "310",
            # "322",
            # "362",
            # "368",
            # "424",
            # "426",
            # "430",
            # "461",
            # "655"
                   ]

        return sources

    @classmethod
    def get_classes(cls) -> list[int]:
        classes = [
            1,

        ]
        return classes

    @classmethod
    def get_mapping_configuration(cls):
        config = [

            {
                "field": "lease_price",
                "MappersProvider": 2,
                "Metadata": '{"list_price":"ListPrice","prop_type":"PropertyType"}',
                "Rules": 421,
                "Enhancers": None,
                "Const": None,
                "Deleter": None,
                "Metadata_check": "ListPrice"

            },

        ]

        return config
