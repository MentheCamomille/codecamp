# Groupe de rosine_l 1034574

**intégration avec sous traitants EMS**

- scripts Py pour importer + fusionner les données exportées des DB MongoDB
- synchronoisation quotidienne des données via des tĉhes planifiées ( Cron ? )

**Logistique**

- endpoints ds l'API ( FastAPI ) -> assoccier les objets IoT à des clients/ transporteurs 
- enregistrements de l'historique des mouvements des IoT ( livraison, prise en charge...)

**Utilisation finale**

- app react native/expo 
- intégration scanner QRcode ( suivre les IoT + gérer les abonnements )
- récupérer données sur l'api et les afficher sur l'app

**Facturation**
- endpoints pour activer/désactiver les objets et gérer les abonnements
- StripeAPI -> pour gérer les paiements / abonnements

**Maj/ sav**
- scripts pour faire des maj à distance du firmware des obj IoT ( via MQTT )
- gestion des demandes sav via endpoints api

**CMS **
- importer les données EMS 
- gérer les utilisateurs, obj, clients,
- interface adaptée pour la gestion des données, des factures, notifs...

**reporting**
- visualisation de l'exportation des données 
- utilisation d'une librairie de visualisation de données ( Chart.js ?) pour créer des rapports et des tableaux de bord 

**évolutivité**
- Docker pour la conteunerisation, K8s pour l'orchestration 

**Test et maintenance**
- test unitaires python avec Pytest
- Jest pour react
- CI/CD avec Gitlab pour automatisation des tests et déploiements
