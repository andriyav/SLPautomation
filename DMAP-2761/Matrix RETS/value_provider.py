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
            "239",
            # "402" check mets,
            "518",
            # "158" check mets,,
            # "387 check mets,",
            # "525" TypeOfSale,
            # "526" TypeOfSale,
            "491",
            # "536",
            # "340 investigation",
            # "470 investigation",
            "369",
            "632"
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
                "Metadata": '{"list_price":"ListPrice","sale_rent":"TransactionType"}',
                "Rules": 421,
                "Enhancers": None,
                "Const": None,
                "Deleter": None,
                "Metadata_check": "ListPrice"

            },

        ]

        return config
