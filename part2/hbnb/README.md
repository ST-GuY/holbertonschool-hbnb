# HBnB (Holberton BnB)

## Description
HBnB est une application de gestion de locations de vacances, avec une architecture en couches (Presentation, Business Logic, Persistence).
L’application utilise Flask pour l’API et un repository en mémoire pour stocker les objets (Users, Places, Reviews, Amenities).

## Objectif
Ce projet a pour but de mettre en pratique la programmation orientée objet, les design patterns (Facade), et la séparation des couches dans une application web.
Les objets sont identifiés par des UUIDs pour garantir l’unicité et la sécurité.

## Structure
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   └── v1/
│   │       ├── users.py
│   │       ├── places.py
│   │       └── reviews.py
│   ├── models/
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   └── amenity.py
│   ├── services/
│   │   └── facade.py
│   └── persistence/
│       └── repository.py
├── tests/
│   ├── test_user.py
│   ├── test_place.py
│   └── test_facade.py
├── run.py
├── config.py
└── requirements.txt
