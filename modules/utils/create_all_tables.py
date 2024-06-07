from ..aneel.models import (
    DistributedGenerationEnterprise,
    EnterpriseGdInformationTechnicalWind,
    EnterpriseGdTechnicalInformationHydroelectric,
    EnterpriseGdTechnicalInformationThermoelectric,
    VentureGdPhotovoltaicTechnicalInformation,
)
from ..connectors.database import Base, engine


def create_all_tables():
    Base.metadata.create_all(engine)
    print("Tabelas criadas !")
