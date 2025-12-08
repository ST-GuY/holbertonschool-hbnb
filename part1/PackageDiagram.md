### High-Level Package Diagram
<img src="diagram/Package.png" alt="Schéma explicatif" width="150"/>

### Description du diagramme

### PresentationLayer (Couche de présentation)

Contient l’API de service (+ServiceAPI).

C’est l’interface entre l’utilisateur (ou une application cliente) et le système.

Elle utilise un Facade Pattern pour simplifier l’accès aux fonctionnalités de la couche métier.

### BusinessLogicLayer (Couche métier)

Contient les classes modèles principales :

User

Place

Review

Amenity

Cette couche gère la logique métier et applique les règles de traitement.

Elle communique avec la couche de persistance pour gérer les opérations sur la base de données.

### PersistenceLayer (Couche de persistance)

Contient les mécanismes d’accès aux données (+DatabaseAccess, +Repository).

Responsable de la gestion de la base de données : lecture, écriture, mise à jour, suppression.

Fournit les données nécessaires à la couche métier.
