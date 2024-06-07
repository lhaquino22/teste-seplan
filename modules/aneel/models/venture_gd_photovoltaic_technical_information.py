from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from modules.connectors.database import Base


class VentureGdPhotovoltaicTechnicalInformation(Base):
    __tablename__ = "VentureGdPhotovoltaicTechnicalInformation"
    __table_args__ = {"schema": "public"}
    _id = Column(Integer, primary_key=True, index=True)
    CreatedAt = Column(DateTime(timezone=True), server_default=func.now())
    UpdatedAt = Column(DateTime(timezone=True), onupdate=func.now())
    DatGeracaoConjuntoDados = Column(DateTime)
    CodGeracaoDistribuida = Column(String)
    MdaAreaArranjo = Column(String)
    MdaPotenciaInstalada = Column(String)
    NomFabricanteModulo = Column(String)
    NomFabricanteInversor = Column(String)
    DatConexao = Column(DateTime)
    MdaPotenciaModulos = Column(String)
    MdaPotenciaInversores = Column(String)
    QtdModulos = Column(Integer)
    NomModeloModulo = Column(String)
    NomModeloInversor = Column(String)
