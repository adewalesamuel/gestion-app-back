import traceback
from flask import Flask, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException, InternalServerError
from .db import session, Base, engine
from .model_registry import *

from .common_features.user.route import route as user_blueprints
from .common_features.audit_log.route import route as audit_log_blueprints
from .common_features.auth.route import route as auth_blueprints
from .common_features.config_systeme.route import route as config_systeme_blueprints
from .common_features.notification.route import route as notification_blueprints
from .common_features.role.route import route as role_blueprints

from .ED.ed_abonnement.route import route as ed_abonnement_blueprints
from .ED.ed_api.route import route as ed_api_blueprints
from .ED.ed_format_donnees.route import route as ed_format_donnees_blueprints
from .ED.ed_log_echange.route import route as ed_log_echange_blueprints
from .ED.ed_politique_acces.route import route as ed_politique_acces_blueprints
from .ED.ed_schema_donnees.route import route as ed_schema_donnees_blueprints

from .GU.gu_commentaire.route import route as gu_commentaire_blueprints
from .GU.gu_demande.route import route as gu_demande_blueprints
from .GU.gu_historique.route import route as gu_historique
from .GU.gu_statut_demande.route import route as gu_statut_demande_blueprints
from .GU.gu_transaction.route import route as gu_transaction_blueprints
from .GU.gu_type_demande.route import route as gu_type_demande_blueprints

from .IN.in_checklist.route import route as in_checklist_blueprints
from .IN.in_equipe_inspection.route import route as in_equipe_inspection_blueprints
from .IN.in_non_conformite.route import route as in_non_conformite_blueprints
from .IN.in_planification.route import route as in_planification_blueprints
from .IN.in_resultat_item.route import route as in_resultat_item_blueprints
from .IN.in_type_controle.route import route as in_type_controle_blueprints

from .RC.rc_acteur.route import route as rc_acteur_blueprints
from .RC.rc_certificat.route import route as rc_certificat_blueprints
from .RC.rc_equipement.route import route as rc_equipement_blueprints
from .RC.rc_historique_propriete.route import route as rc_historique_propriete_blueprints
from .RC.rc_pays.route import route as rc_pays_blueprints
from .RC.rc_port.route import route as rc_port_blueprints
from .RC.rc_type_engin.route import route as rc_type_engin_blueprints

from .RE.re_historique_relance.route import route as re_historique_relance_blueprints
from .RE.re_mode_paiement.route import route as re_mode_paiement_blueprints
from .RE.re_ordre_recette.route import route as re_ordre_recette_blueprints
from .RE.re_paiement.route import route as re_paiement_blueprints
from .RE.re_relance.route import route as re_relance_blueprints
from .RE.re_tarif.route import route as re_tarif_blueprints

def create_app():
    Base.metadata.create_all(engine)
    # Initialisation de l'application FLask
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['MAIL_SERVER'] = environ['MAIL_SERVER']
    # app.config['MAIL_PORT'] = environ['MAIL_PORT']
    # app.config['MAIL_USERNAME'] = environ['MAIL_USERNAME']
    # app.config['MAIL_PASSWORD'] = environ['MAIL_PASSWORD']
    # app.config['MAIL_USE_TLS'] = environ['MAIL_USE_TLS']
    CORS(app,supports_credentials=True)

    # Definitions des routes
    app.register_blueprint(user_blueprints)
    app.register_blueprint(audit_log_blueprints)
    app.register_blueprint(auth_blueprints)
    app.register_blueprint(config_systeme_blueprints)
    app.register_blueprint(notification_blueprints)
    app.register_blueprint(role_blueprints)
    
    app.register_blueprint(ed_abonnement_blueprints)
    app.register_blueprint(ed_api_blueprints)
    app.register_blueprint(ed_format_donnees_blueprints)
    app.register_blueprint(ed_log_echange_blueprints)
    app.register_blueprint(ed_politique_acces_blueprints)
    app.register_blueprint(ed_schema_donnees_blueprints)

    app.register_blueprint(gu_commentaire_blueprints)
    app.register_blueprint(gu_demande_blueprints)
    app.register_blueprint(gu_statut_demande_blueprints)
    app.register_blueprint(gu_transaction_blueprints)
    app.register_blueprint(gu_type_demande_blueprints)

    app.register_blueprint(in_checklist_blueprints)
    app.register_blueprint(in_equipe_inspection_blueprints)
    app.register_blueprint(in_non_conformite_blueprints)
    app.register_blueprint(in_planification_blueprints)
    app.register_blueprint(in_resultat_item_blueprints)
    app.register_blueprint(in_type_controle_blueprints)

    app.register_blueprint(rc_acteur_blueprints)
    app.register_blueprint(rc_certificat_blueprints)
    app.register_blueprint(rc_equipement_blueprints)
    app.register_blueprint(rc_historique_propriete_blueprints)
    app.register_blueprint(rc_pays_blueprints)
    app.register_blueprint(rc_port_blueprints)
    app.register_blueprint(rc_type_engin_blueprints)
    app.register_blueprint(re_historique_relance_blueprints)
    app.register_blueprint(re_mode_paiement_blueprints)
    app.register_blueprint(re_ordre_recette_blueprints)
    app.register_blueprint(re_paiement_blueprints)
    app.register_blueprint(re_relance_blueprints)
    app.register_blueprint(re_tarif_blueprints)

    @app.errorhandler(Exception) # type: ignore
    def handle_error(e: Exception):
        code = InternalServerError.code
        name = str(e)
        description = None
        trace = traceback.format_exception(e)

        if isinstance(e, HTTPException):
            code = e.code
            name = e.name
            description = e.description
        
        session.close()
        return jsonify(message=name, errors=description, trace=trace), code

    @app.teardown_appcontext
    def shutdown_session(exception=None) -> None:
        session.remove()

    return app

app = create_app()