from .models.distributed_generation_enterprise import DistributedGenerationEnterprise
from settings import DISTRIBUTED_GENERATION_ENTERPRISE_RESOURCE_ID
from modules.common.database import DataBase
from modules.connectors.aneel import AneelAPIConnector


def run():
    database = DataBase()
    aneel_api_connector = AneelAPIConnector()
    params = {
        "limit": 30000,
        "resource_id": DISTRIBUTED_GENERATION_ENTERPRISE_RESOURCE_ID,
    }
    for records in aneel_api_connector.consult_dataset(params=params):
        print(f"Inserting records into the database: {len(records)}")
        database.batch_insert(model=DistributedGenerationEnterprise, records=records)
