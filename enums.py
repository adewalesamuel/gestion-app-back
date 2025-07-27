from enum import Enum, auto

class NotificationType(Enum):
    alerte = auto()
    info = auto()
    urgence = auto()
    

class TypeEnginCategorie(Enum):
    navigation = auto()
    peche = auto()
    commerce = auto()
    plaisance = auto()
    service = auto()
    

class ActeurType(Enum):
    morale = auto()
    physique = auto()
    

class CertificatType(Enum):
    securite = auto()
    pollution = auto()
    navire = auto()
    autre = auto()
    

class HistoriqueProprieteTypeTransaction(Enum):
    achat = auto()
    vente = auto()
    don = auto()
    heritage = auto()
    

class TransactionStatut(Enum):
    initiee = auto()
    completee = auto()
    echouee = auto()
    remboursee = auto()
    

class HistoriqueAction(Enum):
    creation = auto()
    modification = auto()
    validation = auto()
    rejet = auto()
    

class TypeControleGraviteMin(Enum):
    mineure = auto()
    majeure = auto()
    critique = auto()
    

class NonConformiteGravite(Enum):
    mineure = auto()
    majeure = auto()
    critique = auto()
    

class NonConformiteStatut(Enum):
    ouverte = auto()
    en_cours = auto()
    resolue = auto()
    fermee = auto()
    

class InspectionStatut(Enum):
    planifiee = auto()
    realisee = auto()
    annulee = auto()
    reportee = auto()
    

class InspectionResultat(Enum):
    conforme = auto()
    non_conforme = auto()
    avec_reserves = auto()
    

class TarifFrequence(Enum):
    unique = auto()
    annuelle = auto()
    mensuelle = auto()
    ponctuelle = auto()
    

class OrdreRecetteStatut(Enum):
    emis = auto()
    paye = auto()
    partiel = auto()
    en_retard = auto()
    annule = auto()
    

class RelanceMode(Enum):
    email = auto()
    courrier = auto()
    sms = auto()
    appelle = auto()
    

class RelanceStatut(Enum):
    envoyee = auto()
    recue = auto()
    ouverte = auto()
    

class HistoriqueRelanceMode(Enum):
    email = auto()
    courrier = auto()
    sms = auto()
    appelle = auto()
    

class SchemaDonneesStatut(Enum):
    brouillon = auto()
    valide = auto()
    deprecie = auto()
    

class ApiStatut(Enum):
    actif = auto()
    inactif = auto()
    maintenance = auto()
    

class LogEchangeTypeRequete(Enum):
    GET = auto()
    POST = auto()
    PUT = auto()
    DELETE = auto()
    PATCH = auto()
    