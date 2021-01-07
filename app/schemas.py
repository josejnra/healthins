from datetime import datetime
from enum import Enum
from typing import List

from pydantic import validator, BaseModel, Field


class GeographyLevelEnum(str, Enum):
    us = 'us'
    state = 'state'
    county = 'county'


class Healthins(BaseModel):

    # get
    headers: List[str] = Field(description="Colunas de interesse dos dados a serem extraidos.", example=["NIC_PT", "NUI_PT", "NAME"])

    # for
    geography_level: GeographyLevelEnum = Field(description="Nivel geografico.", example="county")
    places: str = Field(description="Estados ou municipios. Dependendo do nivel geografico definido.", example="*")

    # in
    for_states: str = Field(default=None, description="Caso o nivel geografico seja county, pode-se definir para quais estados.", example="48")

    # time
    year: int = Field(description="Ano de referencia dos dados", example=2017)

    class Config:
        schema_extra = {
            "examples": [
                {
                    "headers": ["NIC_PT", "NUI_PT", "NAME"],
                    "geography_level": "us",
                    "places": "*",
                    "year": 2017
                },
                {
                    "headers": ["NIC_PT", "NUI_PT", "NAME"],
                    "geography_level": "state",
                    "places": "*",
                    "year": 2010
                },
                {
                    "headers": ["NIC_PT", "NUI_PT", "NAME"],
                    "geography_level": "county",
                    "places": "*",
                    "year": 2011
                },
                {
                    "headers": ["NIC_PT", "NUI_PT", "NAME"],
                    "geography_level": "county",
                    "places": "195",
                    "for_states": "02",
                    "year": 2011
                },
                {
                    "headers": ["NIC_PT", "NUI_PT", "NAME"],
                    "geography_level": "county",
                    "places": "*",
                    "for_states": "*",
                    "year": 2014
                }
            ]
        }

    @validator('year')
    def year_format(cls, v):
        try:
            datetime.strptime(str(v), '%Y')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY")

        return v
