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
            "312",
            "318",
            "320",
            # "323",
            "325",
            "353",
            "355",
            "382",
            "393",
            "413",
            "421",
            "427",
            "432",
            "441",
            "447",
            "449",
            "460",
            "465",
            "478",
            # "481",
            "486",
            # "489",
            "495",
            "497",
            "501",
            "506",
            "509",
            "510",
            "511",
            # "514",
            "515",
            "517",
            "533",
            "534",
            "535",
            "552",
            "559",
            "582",
            "594",
            "626",
            "627",
            "662"
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
            # {
            #     "field": "commissions-properties-comp_based_on",
            #     "MappersProvider": None,
            #     "Metadata": "SpecialListingConditions",
            #     "Rules": 411,
            #     "Enhancers": 33,
            #     "Const": "False"
            # },

            {
                "field": "lease_price",
                "MappersProvider": 2,
                "Metadata": '{"list_price":"L_AskingPrice", "prop_type":"L_Class", "sale_rent":"L_SaleRent"}',
                "Rules": 421,
                "Enhancers": None,
                "Const": "False",
                "Deketer": "listing_rule_lease_price__0"
            },
            # {
            #     "field": "commissions-properties-comp_based_on",
            #     "MappersProvider": 6,
            #     "Metadata": "SpecialListingConditions",
            #     "Rules": 411,
            #     "Enhancers": 33,
            #     "Const": "False"
            # },
        ]

        return config
