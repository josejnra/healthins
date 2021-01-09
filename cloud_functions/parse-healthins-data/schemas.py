from pydantic import BaseModel


class HealthinsSchema(BaseModel):

    AGE_DESC: int = None
    AGECAT: int = None
    COUNTY: int = None
    GEOCAT: int = None
    GEOID: int = None
    IPR_DESC: int = None
    IPRCAT: int = None
    NAME: str = None
    NIC_LB90: int = None
    NIC_MOE: int = None
    NIC_PT: int = None
    NIC_UB90: int = None
    NIPR_LB90: int = None
    NIPR_MOE: int = None
    NIPR_PT: int = None
    NIPR_UB90: int = None
    NUI_LB90: int = None
    NUI_MOE: int = None
    NUI_PT: int = None
    NUI_UB90: int = None
    PCTIC_LB90: int = None
    PCTIC_MOE: int = None
    PCTIC_PT: int = None
    PCTIC_UB90: int = None
    PCTUI_LB90: int = None
    PCTUI_MOE: int = None
    PCTUI_PT: int = None
    PCTUI_UB90: int = None
    RACE_DESC: int = None
    RACECAT: int = None
    SEX_DESC: int = None
    SEXCAT: int = None
    STABREV: int = None
    STATE: int = None
    US: int = None
    YEAR: int = None


def parse_name(name):
    return {
        "TIME": "YEAR"
    }.get(name, name)
