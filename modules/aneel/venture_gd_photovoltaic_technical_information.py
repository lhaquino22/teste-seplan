from .models import VentureGdPhotovoltaicTechnicalInformation
from settings import VENTURE_GD_PHOTOVOLTAIC_TECHNICAL_INFORMATION_RESOURSE_ID
from modules.common.database import DataBase
from modules.connectors.aneel import AneelAPIConnector


def run():
    database = DataBase()
    aneel_api_connector = AneelAPIConnector()
    params = {
        "limit": 30000,
        "resource_id": VENTURE_GD_PHOTOVOLTAIC_TECHNICAL_INFORMATION_RESOURSE_ID,
    }
    for records in aneel_api_connector.consult_dataset(params=params):
        print(f"Inserting {len(records)} records into the database VentureGdPhotovoltaicTechnicalInformation")
        database.batch_insert(model=VentureGdPhotovoltaicTechnicalInformation, records=records)
