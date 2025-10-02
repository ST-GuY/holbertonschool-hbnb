### Class Diagram
<img src="diagram/Class.png" alt="Schéma explicatif" width="300"/>

### Class User

Représente un utilisateur de l’application.

Attributs :

UUID id : identifiant unique de l’utilisateur

String name : nom de l’utilisateur

String email : adresse e-mail

String password : mot de passe

Date created : date de création du compte

Date updated : date de mise à jour du compte

Méthodes :

create()

update()

delete()

Relations :

Un utilisateur peut posséder plusieurs lieux (owns).

Un utilisateur peut écrire plusieurs avis (writes).

### Class Place

Représente un lieu proposé dans l’application.

Attributs :

UUID id : identifiant unique du lieu

String title : titre du lieu

String description : description du lieu

Float price : prix du lieu

Date created : date de création

Date updated : date de mise à jour

Méthodes :

create()

update()

delete()

calculate_total_price() : calcule le prix total (par exemple en fonction de la durée ou des options).

Relations :

Un lieu est possédé par un utilisateur.

Un lieu peut recevoir plusieurs avis (has).

Un lieu peut inclure plusieurs commodités (includes).

### Class Review

Représente un avis laissé par un utilisateur sur un lieu.

Attributs :

UUID id : identifiant unique de l’avis

String description : contenu de l’avis

Date created : date de création

Date updated : date de mise à jour

Méthodes :

create()

update()

delete()

Relations :

Un avis est écrit par un utilisateur.

Un avis est associé à un lieu.

### Class Amenity

Représente une commodité ou un service proposé dans un lieu (ex. Wi-Fi, piscine, parking).

Attributs :

UUID id : identifiant unique de la commodité

String name : nom de la commodité

String description : description de la commodité

Date created : date de création

Date updated : date de mise à jour

Méthodes :

create()

update()

delete()

Relations :

Une commodité peut être incluse dans plusieurs lieux.
