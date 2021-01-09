from typing import List
import json

from fastapi import APIRouter, HTTPException
from google.api_core.exceptions import NotFound

from app.common.api_request import APIRequest
from app.common.publisher import PublisherMessage, GCPPubSub
from app.config import settings
from app.healthins_api.health_insurance_statistics import HealthInsuranceStatistics
from app.healthins_api.params_builder import ParamsBuilder
from app.schemas import Healthins

router = APIRouter()


@router.post('/healthins/')
def healthins_data(healthins_params: Healthins):
    params = ParamsBuilder(str(healthins_params.year)) \
        .set_header_params(healthins_params.headers) \
        .set_for_param(healthins_params.geography_level, healthins_params.places, healthins_params.for_states) \
        .build_params()

    data_retrieved_from_api = HealthInsuranceStatistics(APIRequest()).get_data(settings.base_url + params)

    try:
        save_retrieved_data(data_retrieved_from_api).result()
    except NotFound:
        raise HTTPException(status_code=502, detail="Erro de conexão com serviço interno!")

    return data_retrieved_from_api


def save_retrieved_data(retrieved_data: List[List[str]]):
    formatted_data = dict(columns=retrieved_data[0], rows=retrieved_data[1:])
    message = json.dumps(formatted_data)

    publisher = PublisherMessage(GCPPubSub(settings.project_id, settings.google_credentials))

    return publisher.publish(settings.pubsub_topic, message)
