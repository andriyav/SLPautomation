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
            # "410",
            # "412",
            # "414",
            # "415",
            # "416",
            # "417",
            # "418",
            # "423",
            # "424",
            # "425",
            # "426",
            # "428",
            # "429",
            # "430",
            # "431",
            # "433",
            # "434",
            # "439",
            # "440",
            # "442",
            # "450",
            # "457",
            # "459",
            # "461",
            # "463",
            # "466",
            # "472",
            # "476",
            # "477",
            # "484",
            # "485",
            # "490",
            # "493",
            # "494",
            # "500",
            # "502",
            # "503",
            # "507",
            # "513",
            # "519",
            # "522",
            # "538",
            # "539",
            # "541",
            # "546",
            # "550",
            # "551",
            # "555",
            # "557",
            # "560",
            # "563",
            # "574",
            # "576",
            # "581",
            # "586",
            # "591",
            # "592",
            # "593",
            # "625",
            # "629",
            # "633",
            # "635",
            # "644",
            # "649",
            # "655",
            # "659",
            # "663",
            # "664"
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

            # {
            #     "field": "lease_price",
            #     "MappersProvider": 6,
            #     "Metadata": '{"list_price":"ListPrice","prop_type":"PropertyType"}',
            #     "Rules": 421,
            #     "Enhancers": None,
            #     "Const": None,
            #     "Deleter": None,
            #     "Metadata_check": "L_AskingPrice"
            #
            # },
            {
                "field": "is_short_sale",
                "MappersProvider": 6,
                "Metadata": 'SpecialListingConditions',
                "Rules": 413,
                "Enhancers": None,
                "Const": None,
                "Deleter": '#listing_enhance_is_short_sale__0',


            },
            {
                "field": "is_foreclosure",
                "MappersProvider": 6,
                "Metadata": 'SpecialListingConditions',
                "Rules": 412,
                "Enhancers": None,
                "Const": None,
                "Deleter": '#listing_enhance_is_foreclosure__0',

            }
            # {
            #     "field": "lease_price",
            #     "MappersProvider": None,
            #     "Metadata": '{"list_price":"L_AskingPrice", "prop_type":"L_Class", "sale_rent":"L_SaleRent"}',
            #     "Rules": None,
            #     "Enhancers": None,
            #     "Const": None,
            #     "Deleter": "#listing_mapper_lease_price__0"
            #
            #
            # },
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
