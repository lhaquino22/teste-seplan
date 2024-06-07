# ENTERPRISE_GD_TECHNICAL_INFORMATION_HYDROELECTRIC_RESOURCE_ID

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from modules.connectors.database import Base


class EnterpriseGdTechnicalInformationHydroelectric(Base):
    __tablename__ = "EnterpriseGdTechnicalInformationHydroelectric"
    __table_args__ = {"schema": "public"}
    _id = Column(Integer, primary_key=True, index=True)
    CreatedAt = Column(DateTime(timezone=True), server_default=func.now())
    UpdatedAt = Column(DateTime(timezone=True), onupdate=func.now())
    DatGeracaoConjuntoDados = Column(String)
    CodGeracaoDistribuida = Column(String)
    NomRio = Column(String)
    MdaPotenciaInstalada = Column(String)
    DatConexao = Column(String)
    MdaPotenciaAparente = Column(String)
    MdaFatorPotencia = Column(String)
    MdaTensao = Column(String)
    MdaNivelOperacionalMontante = Column(String)
    MdaNivelOperacionalJusante = Column(String)