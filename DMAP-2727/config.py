import os
from typing import List

from dotenv import load_dotenv

load_dotenv()


class ValueConfig:

    @classmethod
    def get_email(cls) -> str:
        return os.getenv("EMAIL")

    @classmethod
    def get_password(cls) -> str:
        return os.getenv("PASSWORD")

    @classmethod
    def get_list_of_sources(cls) -> list[str]:
        sources = [
            '3',
            # '404',
            # '56',
            # '56',
            # '404'
        ]
        return sources

    @classmethod
    def mapping_config(cls):
        config = [
            {
                "field": "commissions-properties-comp_based_on",
                "MappersProvider": 6,
                "Metadata": "SpecialListingConditions",
                "Rules": 411,
                "Enhancers": 33,
                "Const": "False"
            },
            {
                "field": "geo",
                "MappersProvider": 6,
                "Metadata": "SpecialListingConditions",
                "Rules": 412,
                "Enhancers": 33,
                "Const": "False"
            },
            {
                "field": "kww_region",
                "MappersProvider": 6,
                "Metadata": "SpecialListingConditions",
                "Rules": 412,
                "Enhancers": 33,
                "Const": "False"
            },
            {
                "field": "commissions-properties-comp_based_on",
                "MappersProvider": 6,
                "Metadata": "SpecialListingConditions",
                "Rules": 411,
                "Enhancers": 33,
                "Const": "False"
            },
        ]

        return config
