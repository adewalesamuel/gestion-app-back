class NotificationType:
    ALERTE = "alerte"
    INFO = "info"
    URGENCE = "urgence"

class TypeEnginCategorie:
    NAVIGATION = "navigation"
    PECHE = "peche"
    COMMERCE = "commerce"
    PLAISANCE = "plaisance"
    SERVICE = "service"

class ActeurType:
    MORALE = "morale"
    PHYSIQUE = "physique"

class CertificatType:
    SECURITE = "securite"
    POLLUTION = "pollution"
    NAVIRE = "navire"
    AUTRE = "autre"

class HistoriqueProprieteTypeTransaction:
    ACHAT = "achat"
    VENTE = "vente"
    DON = "don"
    HERITAGE = "heritage"

class TransactionStatut:
    INITIEE = "initiee"
    COMPLETEE = "completee"
    ECHOUEE = "echouee"
    REMBOURSEE = "remboursee"

class HistoriqueAction:
    CREATION = "creation"
    MODIFICATION = "modification"
    VALIDATION = "validation"
    REJET = "rejet"

class TypeControleGraviteMin:
    MINEURE = "mineure"
    MAJEURE = "majeure"
    CRITIQUE = "critique"

class NonConformiteGravite:
    MINEURE = "mineure"
    MAJEURE = "majeure"
    CRITIQUE = "critique"

class NonConformiteStatut:
    OUVERTE = "ouverte"
    EN_COURS = "en_cours"
    RESOLUE = "resolue"
    FERMEE = "fermee"

class InspectionStatut:
    PLANIFIEE = "planifiee"
    REALISEE = "realisee"
    ANNULEE = "annulee"
    REPORTEE = "reportee"

class InspectionResultat:
    CONFORME = "conforme"
    NON_CONFORME = "non_conforme"
    AVEC_RESERVES = "avec_reserves"

class TarifFrequence:
    UNIQUE = "unique"
    ANNUELLE = "annuelle"
    MENSUELLE = "mensuelle"
    PONCTUELLE = "ponctuelle"

class OrdreRecetteStatut:
    EMIS = "emis"
    PAYE = "paye"
    PARTIEL = "partiel"
    EN_RETARD = "en_retard"
    ANNULE = "annule"

class RelanceMode:
    EMAIL = "email"
    COURRIER = "courrier"
    SMS = "sms"
    APPELLE = "appelle"

class RelanceStatut:
    ENVOYEE = "envoyee"
    RECUE = "recue"
    OUVERTE = "ouverte"

class Historiqu_RelanceMode:
    EMAIL = "email"
    COURRIER = "courrier"
    SMS = "sms"
    APPELLE = "appelle"

class SchemaDonneesStatut:
    BROUILLON = "brouillon"
    VALIDE = "valide"
    DEPRECIE = "deprecie"

class ApiStatut:
    ACTIF = "actif"
    INACTIF = "inactif"
    MAINTENANCE = "maintenance"

class LogEchangeTypeRequete:
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"