from datetime import datetime
from enum import Enum
from typing import List

from pydantic import validator, BaseModel, Field


class HeadersEnum(str, Enum):
    age_desc = "AGE_DESC"
    agecat = "AGECAT"
    county = "COUNTY"
    geocat = "GEOCAT"
    geoid = "GEOID"
    ipr_desc = "IPR_DESC"
    iprcat = "IPRCAT"
    name = "NAME"
    nic_lb90 = "NIC_LB90"
    nic_moe = "NIC_MOE"
    nic_pt = "NIC_PT"
    nic_ub90 = "NIC_UB90"
    nipr_lb90 = "NIPR_LB90"
    nipr_moe = "NIPR_MOE"
    nipr_pt = "NIPR_PT"
    nipr_ub90 = "NIPR_UB90"
    nui_lb90 = "NUI_LB90"
    nui_moe = "NUI_MOE"
    nui_pt = "NUI_PT"
    nui_ub90 = "NUI_UB90"
    pctic_lb90 = "PCTIC_LB90"
    pctic_moe = "PCTIC_MOE"
    pctic_pt = "PCTIC_PT"
    pctic_ub90 = "PCTIC_UB90"
    pctui_lb90 = "PCTUI_LB90"
    pctui_moe = "PCTUI_MOE"
    pctui_pt = "PCTUI_PT"
    pctui_ub90 = "PCTUI_UB90"
    race_desc = "RACE_DESC"
    racecat = "RACECAT"
    sex_desc = "SEX_DESC"
    sexcat = "SEXCAT"
    stabrev = "STABREV"
    state = "STATE"
    us = "US"
    year = "YEAR"


class GeographyLevelEnum(str, Enum):
    us = 'us'
    state = 'state'
    county = 'county'


class Healthins(BaseModel):

    # get
    headers: List[HeadersEnum] = Field(description="Colunas de interesse dos dados a serem extraidos.", example=["NIC_PT", "NUI_PT", "NAME"])

    # for
    geography_level: GeographyLevelEnum = Field(description="Nivel geografico.", example="county")
    places: str = Field(description="Estados ou municipios. Dependendo do nivel geografico definido. Podendo ser um codigo ou '*'", example="*")

    # in
    for_states: str = Field(default=None, description="Caso o nivel geografico seja county, pode-se definir para quais estados. Podendo ser um codigo ou '*'", example="48")

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
