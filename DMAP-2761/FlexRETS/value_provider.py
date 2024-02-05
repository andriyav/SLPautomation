import os

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
            # "20",
            "27",
            "52",
            "62",
            "105",
            # "109",
            # "175",
            # "263",
            # "327",
            # "399",
            # "400",
            # "403",
            # "411",
            # "423",
            # "462",
            # "483",
            # "520",
            # "651"
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
                "MappersProvider": None,
                "Metadata": None,
                "Rules": 279,
                "Enhancers": None,
                "Const": None,
                "Deleter": None,

            },

            {
                "field": "lease_price",
                "MappersProvider": 2,
                "Metadata": '{"list_price":"LIST_22","prop_type":"LIST_8"}',
                "Rules": 421,
                "Enhancers": None,
                "Const": None,
                "Deleter": None,

            },

        ]

        return config
