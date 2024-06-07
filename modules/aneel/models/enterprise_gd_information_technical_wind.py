from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from modules.connectors.database import Base


class EnterpriseGdInformationTechnicalWind(Base):
    __tablename__ = "EnterpriseGdInformationTechnicalWind"
    __table_args__ = {"schema": "public"}
    _id = Column(Integer, primary_key=True, index=True)
    CreatedAt = Column(DateTime(timezone=True), server_default=func.now())
    UpdatedAt = Column(DateTime(timezone=True), onupdate=func.now())
    DatGeracaoConjuntoDados = Column(String)
    CodGeracaoDistribuida = Column(String)
    NomFabricanteAerogerador = Column(String)
    DscModeloAerogerador = Column(String)
    MdaPotenciaInstalada = Column(String)
    MdaAlturaPa = Column(String)
    DatConexao = Column(String)
    IdcEixoRotor = Column(String)
