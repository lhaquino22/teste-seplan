from modules.common.database import DataBase
from modules.connectors.aneel import AneelAPIConnector
from settings import ENTERPRISE_GD_TECHNICAL_INFORMATION_HYDROELECTRIC_RESOURCE_ID
from .models import EnterpriseGdTechnicalInformationHydroelectric


def run():
    database = DataBase()
    aneel_api_connector = AneelAPIConnector()
    params = {
        "limit": 30000,
        "resource_id": ENTERPRISE_GD_TECHNICAL_INFORMATION_HYDROELECTRIC_RESOURCE_ID,
    }
    for records in aneel_api_connector.consult_dataset(params=params):
        print(
            f"Inserting {len(records)} records into the database EnterpriseGdTechnicalInformationHydroelectric"
        )
        database.batch_insert(
            model=EnterpriseGdTechnicalInformationHydroelectric, records=records
        )
