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
            '56'
        ]
        return sources

    @classmethod
    def get_mapping_configuration(cls):
        config = [
            {
                "field": "required.list_type_id",
                "MappersProvider": 6,
                "Metadata": "SpecialListingConditions",
                "Rules": 410
            },
            {
                "field": "required.sa_source_id",
                "MappersProvider": 6,
                "Metadata": "SpecialListingConditions",
                "Rules": 412
            },
            {
                "field": "required.mls_id",
                "MappersProvider": 6,
                "Metadata": "SpecialListingConditions",
                "Rules": 411
            },
        ]
        return config
