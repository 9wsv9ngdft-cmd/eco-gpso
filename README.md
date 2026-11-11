# ÉcoGPSO — v0.2 (socle cadastral)

PWA statique pour l'observation écologique des communes de Grand Paris Seine Ouest. Territoire de départ : Issy-les-Moulineaux (INSEE 92040).

## Ce qui change en v0.2

- Conservation du prototype Leaflet et des sources ouvertes déjà intégrées.
- Chargement de l'ensemble des parcelles d'Issy depuis l'API Carto IGN, source Parcellaire Express (PCI).
- Pagination conforme à la documentation du module Cadastre (`_limit` maximum 1000 et `_start`).
- Affichage des polygones cadastraux et sélection d'une parcelle.
- Fiche parcellaire avec attributs disponibles et comptage spatial des arbres/observations effectivement chargés dans la session.
- Export de la couche cadastrale chargée en GeoJSON (`parcelles_92040.geojson`).
- Mention explicite des limites : les points environnementaux chargés par le prototype sont un échantillon limité, les comptages par parcelle ne sont donc pas exhaustifs.

## Installation sur GitHub Pages

1. Remplacer `index.html` et `README.md` à la racine du dépôt par ceux de cette archive.
2. Conserver `manifest.webmanifest` et `icon.svg` déjà présents dans le dépôt.
3. Commit sur `main`.
4. Vérifier que GitHub Pages publie bien la branche `main` depuis `/ (root)`.
5. Ouvrir l'application en HTTPS sur Safari.

Aucune dépendance de build ni serveur n'est nécessaire. Leaflet est chargé depuis un CDN.

## Utilisation

1. Ouvrir l'onglet « Carte & parcelles ».
2. Appuyer sur « Charger toutes les parcelles d'Issy » et attendre la fin de la pagination.
3. Sélectionner une parcelle sur la carte pour afficher sa fiche.
4. « Exporter GeoJSON » permet de télécharger la couche obtenue pour constituer le fichier de référence `data/parcelles_92040.geojson` dans le dépôt.

Le téléchargement intégral peut prendre du temps selon le réseau et la disponibilité du service IGN. Il est relançable. La version actuelle garde les géométries en mémoire dans l'onglet ; le GeoJSON exporté doit être ajouté au dépôt pour en faire un artefact versionné.

## Sources et méthode

- Arbres GPSO : https://data.seineouest.fr/explore/dataset/arbres-v2/
- Observations participatives : https://data.seineouest.fr/explore/dataset/data-obs-dded-participatif/
- Parcs et jardins Data Issy : https://data.issy.com/explore/dataset/les-parcs-et-jardins-a-issy-les-moulineaux/
- API Carto Cadastre : https://apicarto.ign.fr/api/doc/cadastre

L'API Carto renvoie du GeoJSON en WGS84. La documentation IGN indique les paramètres `_limit` et `_start`, avec une limite de 1000 objets par appel. Le PCI Express est la source recommandée plutôt que l'ancienne BD Parcellaire.

## Limites importantes

- La version v0.2 est un socle technique : les API GPSO doivent encore être vérifiées champ par champ et paginées pour produire des inventaires environnementaux exhaustifs.
- Le comptage parcellaire dans l'interface utilise uniquement les points actuellement présents dans le navigateur (premiers enregistrements retournés par les sources). Il ne constitue pas un inventaire complet.
- Les observations participatives sont dépendantes des signalements et peuvent avoir une précision variable. Les données sensibles ne doivent pas être diffusées à une précision excessive.
- Aucun score écologique global, aucune mesure de pollution, de température, de végétalisation ou d'imperméabilisation n'est extrapolé sans source et méthode validées.
- Le cadastre représente le découpage foncier et non les limites écologiques, la propriété réelle ou l'occupation détaillée du sol.

## Prochaine étape

Constituer un pipeline de données reproductible : télécharger les parcelles, vérifier le nombre total et les géométries, puis paginer et normaliser chaque jeu environnemental, réaliser les jointures spatiales avec des bibliothèques SIG et générer des fiches accompagnées de provenance, millésime, précision et niveau de confiance. Étendre ensuite le pipeline aux 8 communes GPSO.
