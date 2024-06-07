from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from modules.connectors.database import Base


class DistributedGenerationEnterprise(Base):
    __tablename__ = "DistributedGenerationEnterprise"
    __table_args__ = {"schema": "public"}
    _id = Column(Integer, primary_key=True, index=True)
    CreatedAt = Column(DateTime(timezone=True), server_default=func.now())
    UpdatedAt = Column(DateTime(timezone=True), onupdate=func.now())
    DatGeracaoConjuntoDados = Column(String)
    AnmPeriodoReferencia = Column(String)
    NumCNPJDistribuidora = Column(String)
    SigAgente = Column(String)
    NomAgente = Column(String)
    CodClasseConsumo = Column(String)
    DscClasseConsumo = Column(String)
    CodSubGrupoTarifario = Column(String)
    DscSubGrupoTarifario = Column(String)
    CodUFibge = Column(String)
    SigUF = Column(String)
    CodRegiao = Column(String)
    NomRegiao = Column(String)
    CodMunicipioIbge = Column(String)
    NomMunicipio = Column(String)
    CodCEP = Column(String)
    SigTipoConsumidor = Column(String)
    NumCPFCNPJ = Column(String)
    NomTitularEmpreendimento = Column(String)
    CodEmpreendimento = Column(String)
    DthAtualizaCadastralEmpreend = Column(String)
    SigModalidadeEmpreendimento = Column(String)
    DscModalidadeHabilitado = Column(String)
    QtdUCRecebeCredito = Column(String)
    SigTipoGeracao = Column(String)
    DscFonteGeracao = Column(String)
    DscPorte = Column(String)
    NumCoordNEmpreendimento = Column(String)
    NumCoordEEmpreendimento = Column(String)
    MdaPotenciaInstaladaKW = Column(String)
    NomSubEstacao = Column(String)
    NumCoordESub = Column(String)
    NumCoordNSub = Column(String)
