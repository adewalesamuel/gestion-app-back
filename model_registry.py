from sqlalchemy.orm import relationship
from .db import mapper_registry

from .common_features.role.model import Role
from .common_features.audit_log.model import AuditLog
from .common_features.notification.model import Notification
from .common_features.user.model import User

from .RC.rc_acteur.model import RCActeur
from .RC.rc_engin_flottant.model import RCEnginFlottant
from .RC.rc_pays.model import RCPays
from .RC.rc_type_engin.model import RCTypeEngin
from .RC.rc_certificat.model import RCCertificat
from .RC.rc_equipement.model import RCEquipement
from .RC.rc_historique_propriete.model import RCHistoriquePropriete
from .RC.rc_port.model import RCPort

from .RE.re_mode_paiement.model import REModePaiement
from .RE.re_historique_relance.model import REHistoriqueRelance
from .RE.re_paiement.model import REPaiement
from .RE.re_remise.model import RERemise

from .GU.gu_demande.model import GUDemande
from .GU.gu_type_demande.model import GUTypeDemande
from .GU.gu_statut_demande.model import GUStatutDemande
from .GU.gu_commentaire.model import GUCommentaire
from .GU.gu_historique.model import GUHistorique
from .GU.gu_transaction.model import GUTransaction
from .GU.gu_workflow.model import GUWorkflow

from .IN.in_inspection.model import INInspection
from .IN.in_checklist.model import INChecklist
from .IN.in_type_controle.model import INTypeControle
from .IN.in_equipe_inspection.model import INEquipeInspection
from .IN.in_non_conformite.model import INNonConformite
from .IN.in_planification.model import INPlanification
from .IN.in_resultat_item.model import INResultatItem

from .RE.re_ordre_recette.model import REOrdreRecette
from .RE.re_relance.model import RERelance
from .RE.re_ordre_recette.model import REOrdreRecette

from .ED.ed_api.model import EDApi

from .ED.ed_abonnement.model import EDAbonnement
from .ED.ed_log_echange.model import EDLogEchange
from .ED.ed_politique_acces.model import EDPolitiqueAcces



Role.users = relationship('User', order_by = User.id, back_populates = 'role')

RCActeur.users = relationship('User', order_by = User.id, back_populates = 'rc_acteur')

User.notifications = relationship('Notification', order_by = Notification.id, back_populates = 'user')

User.audit_logs = relationship('AuditLog', order_by = AuditLog.id, back_populates = 'user')

RCEnginFlottant.rc_equipements = relationship('RCEquipement', order_by = RCEquipement.id, back_populates = 'rc_engin_flottant')

RCPays.rc_ports = relationship('RCPort', order_by = RCPort.id, back_populates = 'rc_pays')

RCEnginFlottant.rc_certificats = relationship('RCCertificat', order_by = RCCertificat.id, back_populates = 'rc_engin_flottant')

RCActeur.rc_historique_proprietes = relationship('RCHistoriquePropriete', order_by = RCHistoriquePropriete.id, back_populates = 'rc_acteur')

RCEnginFlottant.rc_historique_proprietes = relationship('RCHistoriquePropriete', order_by = RCHistoriquePropriete.id, back_populates = 'rc_engin_flottant')

RCTypeEngin.rc_engin_flottants = relationship('RCEnginFlottant', order_by = RCEnginFlottant.id, back_populates = 'rc_type_engin')

RCPays.rc_engin_flottants = relationship('RCEnginFlottant', order_by = RCEnginFlottant.id, back_populates = 'rc_pays')

RCActeur.rc_engin_flottants = relationship('RCEnginFlottant', order_by = RCEnginFlottant.id, back_populates = 'rc_acteur')

REModePaiement.gu_transactions = relationship('GUTransaction', order_by = GUTransaction.id, back_populates = 're_mode_paiement')

GUDemande.gu_transactions = relationship('GUTransaction', order_by = GUTransaction.id, back_populates = 'gu_demande')

User.gu_transactions = relationship('GUTransaction', order_by = GUTransaction.id, back_populates = 'user')

Role.gu_workflows = relationship('GUWorkflow', order_by = GUWorkflow.id, back_populates = 'role')

GUTypeDemande.gu_workflows = relationship('GUWorkflow', order_by = GUWorkflow.id, back_populates = 'gu_type_demande')

User.gu_commentaires = relationship('GUCommentaire', order_by = GUCommentaire.id, back_populates = 'user')

GUDemande.gu_commentaires = relationship('GUCommentaire', order_by = GUCommentaire.id, back_populates = 'gu_demande')

User.gu_historiques = relationship('GUHistorique', order_by = GUHistorique.id, back_populates = 'user')

GUDemande.gu_historiques = relationship('GUHistorique', order_by = GUHistorique.id, back_populates = 'gu_demande')

GUTypeDemande.gu_demandes = relationship('GUDemande', order_by = GUDemande.id, back_populates = 'gu_type_demande')

GUStatutDemande.gu_demandes = relationship('GUDemande', order_by = GUDemande.id, back_populates = 'gu_statut_demande')

RCActeur.gu_demandes = relationship('GUDemande', order_by = GUDemande.id, back_populates = 'rc_acteur')

RCEnginFlottant.gu_demandes = relationship('GUDemande', order_by = GUDemande.id, back_populates = 'rc_engin_flottant')

INInspection.in_resultat_items = relationship('INResultatItem', order_by = INResultatItem.id, back_populates = 'in_inspection')

RCTypeEngin.in_checklists = relationship('INChecklist', order_by = INChecklist.id, back_populates = 'rc_type_engin')

INInspection.in_non_conformites = relationship('INNonConformite', order_by = INNonConformite.id, back_populates = 'in_inspection')

User.in_non_conformites = relationship('INNonConformite', order_by = INNonConformite.id, back_populates = 'user')

RCEnginFlottant.in_planifications = relationship('INPlanification', order_by = INPlanification.id, back_populates = 'rc_engin_flottant')

INChecklist.in_planifications = relationship('INPlanification', order_by = INPlanification.id, back_populates = 'in_checklist')

User.in_equipe_inspections = relationship('INEquipeInspection', order_by = INEquipeInspection.id, back_populates = 'user')

INTypeControle.in_inspections = relationship('INInspection', order_by = INInspection.id, back_populates = 'in_type_controle')

INEquipeInspection.in_inspections = relationship('INInspection', order_by = INInspection.id, back_populates = 'in_equipe_inspection')

RCEnginFlottant.in_inspections = relationship('INInspection', order_by = INInspection.id, back_populates = 'rc_engin_flottant')

User.in_inspections = relationship('INInspection', order_by = INInspection.id, back_populates = 'user')

RCActeur.re_ordre_recettes = relationship('REOrdreRecette', order_by = REOrdreRecette.id, back_populates = 'rc_acteur')

REOrdreRecette.re_relances = relationship('RERelance', order_by = RERelance.id, back_populates = 're_ordre_recette')

User.re_relances = relationship('RERelance', order_by = RERelance.id, back_populates = 'user')

REOrdreRecette.re_remises = relationship('RERemise', order_by = RERemise.id, back_populates = 're_ordre_recette')

User.re_remises = relationship('RERemise', order_by = RERemise.id, back_populates = 'user')

RERelance.re_historique_relances = relationship('REHistoriqueRelance', order_by = REHistoriqueRelance.id, back_populates = 're_relance')

User.re_historique_relances = relationship('REHistoriqueRelance', order_by = REHistoriqueRelance.id, back_populates = 'user')

REOrdreRecette.re_paiements = relationship('REPaiement', order_by = REPaiement.id, back_populates = 're_ordre_recette')

User.re_paiements = relationship('REPaiement', order_by = REPaiement.id, back_populates = 'user')

REModePaiement.re_paiements = relationship('REPaiement', order_by = REPaiement.id, back_populates = 're_mode_paiement')

EDApi.ed_log_echanges = relationship('EDLogEchange', order_by = EDLogEchange.id, back_populates = 'ed_api')

User.ed_log_echanges = relationship('EDLogEchange', order_by = EDLogEchange.id, back_populates = 'user')

EDApi.ed_abonnements = relationship('EDAbonnement', order_by = EDAbonnement.id, back_populates = 'ed_api')

RCActeur.ed_abonnements = relationship('EDAbonnement', order_by = EDAbonnement.id, back_populates = 'rc_acteur')

EDApi.ed_politique_access = relationship('EDPolitiqueAcces', order_by = EDPolitiqueAcces.id, back_populates = 'ed_api')

Role.ed_politique_access = relationship('EDPolitiqueAcces', order_by = EDPolitiqueAcces.id, back_populates = 'role')

mapper_registry.configure()