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

            "105",
            "109",
            "175",

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
