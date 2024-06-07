from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from modules.connectors.database import Base


class EnterpriseGdTechnicalInformationThermoelectric(Base):
    __tablename__ = "EnterpriseGdTechnicalInformationThermoelectric"
    __table_args__ = {"schema": "public"}
    _id = Column(Integer, primary_key=True, index=True)
    CreatedAt = Column(DateTime(timezone=True), server_default=func.now())
    UpdatedAt = Column(DateTime(timezone=True), onupdate=func.now())
    DatGeracaoConjuntoDados = Column(String)
    CodGeracaoDistribuida = Column(String)
    MdaPotenciaInstalada = Column(String)
    DatConexao = Column(String)
    DscCicloTermodinamico = Column(String)
    DscMaquinaMotrizTermica = Column(String)
