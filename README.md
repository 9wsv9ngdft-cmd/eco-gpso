# ÉcoGPSO — prototype PWA

## Lancer
Ouvrir `index.html` dans un navigateur moderne pour tester (les API publiques peuvent refuser les appels depuis `file://`). Pour un test correct, publier ce dossier sur GitHub Pages ou Cloudflare Pages, ou lancer un serveur local.

## Publication gratuite
1. Créer un dépôt GitHub public.
2. Déposer les fichiers du dossier.
3. Dans Settings > Pages, choisir `Deploy from a branch`, branche `main`, dossier `/root`.
4. Ouvrir l’URL HTTPS sur l’iPhone.
5. Safari > Partager > Sur l’écran d’accueil.

## Données connectées dans cette bêta
- GPSO `arbres-v2` : arbres gérés par GPSO.
- GPSO `data-obs-dded-participatif` : observations participatives faune/flore.
- Data Issy `les-parcs-et-jardins-a-issy-les-moulineaux`.
- API Explore v2.1 Opendatasoft.

## Limites assumées
Cette première bêta est une base fonctionnelle de consultation et de cartographie. Elle n'affiche pas encore les limites cadastrales : l'intégration parcellaire doit s'appuyer sur le module Cadastre d'API Carto IGN, avec géométrie d'intersection et pagination. Les couches environnementales ne seront rattachées à une parcelle qu'après croisement spatial vérifié. Les valeurs des jeux ne sont pas nécessairement exhaustives pour les arbres privés ou les observations non signalées.

## API et documentation
- https://data.seineouest.fr/explore/dataset/arbres-v2/
- https://data.seineouest.fr/explore/dataset/data-obs-dded-participatif/
- https://data.issy.com/explore/dataset/les-parcs-et-jardins-a-issy-les-moulineaux/
- https://apicarto.ign.fr/api/doc/cadastre
- https://www.georisques.gouv.fr/acceder-la-carte-interactive-aux-bases-de-donnees-et-lapi
- https://www.insee.fr/fr/information/8184146

## Prochaine étape technique
Ajouter la couche parcellaire IGN, la sélection d'une parcelle, puis l'intersection des arbres/observations et des couches risques/urbanisme. Ajouter ensuite un pipeline de normalisation par commune pour comparer les 8 villes sur des indicateurs homogènes.
