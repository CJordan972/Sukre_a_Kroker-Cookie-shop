# Maison Miette — Mon premier Cookie Shop 🍪

Bienvenue dans ton premier projet de développement web ! Maison Miette est une **boutique fictive** de cookies inspirée par les codes de la pâtisserie haut de gamme. Elle ne reproduit pas le site, le nom ou les visuels de Pierre Hermé.

## 1. Ouvrir le site sur ton ordinateur

1. Télécharge et décompresse le dossier `atelier-cookie-projet.zip`.
2. Ouvre le dossier `atelier-cookie-projet`.
3. Double-clique sur le fichier `index.html` : le site s'ouvrira dans ton navigateur.
4. Clique sur « Ajouter au panier » pour tester son fonctionnement.

Pour modifier le site, installe **Visual Studio Code** (gratuit), puis ouvre ce dossier avec **Fichier > Ouvrir un dossier**.

## 2. Comprendre les fichiers

```text
atelier-cookie-projet/
├── index.html            ← les textes et la structure des pages
├── styles.css            ← les couleurs, typographies, mises en page
├── script.js             ← les boutons et le panier de démonstration
├── assets/
│   ├── cookie-chocolat.svg
│   ├── cookie-pistache.svg
│   ├── cookie-caramel.svg
│   └── cookie-framboise.svg
└── README.md             ← ce guide
```

Le fichier `generate_art.py` est un petit outil facultatif qui a servi à créer les illustrations originales de cookies. Tu n'as pas besoin de Python pour utiliser le site.

## 3. Premier exercice : personnaliser un produit

1. Dans `index.html`, cherche `L'Intense` et remplace-le par `Le Cacao Royal`.
2. Enregistre le fichier (Ctrl+S, ou Cmd+S sur Mac).
3. Recharge la page dans ton navigateur : le nom aura changé.
4. Dans `script.js`, remplace aussi `L'Intense` par `Le Cacao Royal`, pour que le panier utilise le nouveau nom.

Autres exercices :
- Dans `styles.css`, change `--cocoa: #39261f;` pour modifier la couleur principale.
- Dans `index.html`, change le slogan « Le bonheur a du croquant. ».
- Dans `script.js`, modifie `price: 490` pour changer le prix du chocolat (en centimes).

## 4. Mettre le site sur GitHub

1. Crée un compte sur https://github.com si besoin.
2. Clique sur **New repository** (nouveau dépôt).
3. Nomme-le `mon-cookie-shop` et choisis **Public** (nécessaire pour publier gratuitement sur GitHub Pages avec GitHub Free).
4. Clique sur **Create repository**.
5. Dans le dépôt, clique sur **Add file > Upload files** (ou le lien d'ajout de fichiers affiché si le dépôt est vide).
6. Envoie **`index.html`, `styles.css`, `script.js`, `README.md` et le dossier `assets` avec ses SVG**. Le fichier `generate_art.py` est facultatif.
7. Clique sur **Commit changes** pour enregistrer les fichiers.

**Important :** `index.html` doit se trouver directement à la racine du dépôt, et non dans un sous-dossier.

## 5. Publier avec GitHub Pages

1. Dans le dépôt GitHub, ouvre **Settings**.
2. Dans le menu latéral, ouvre **Pages**.
3. Sous **Build and deployment > Source**, choisis **Deploy from a branch**.
4. Sous **Branch**, choisis **main**, le dossier **/(root)** puis clique sur **Save**.
5. Attends que GitHub affiche l'adresse de ton site, puis ouvre **Visit site**.

Ton URL aura généralement la forme : `https://TON-PSEUDO.github.io/mon-cookie-shop/`.

Référence officielle : https://docs.github.com/fr/pages/getting-started-with-github-pages/creating-a-github-pages-site

## 6. Le programme de progression

- **Étape 1 — HTML :** comprendre les titres, paragraphes, liens et images.
- **Étape 2 — CSS :** changer les couleurs, polices, espacements et formats mobiles.
- **Étape 3 — JavaScript :** comprendre comment fonctionne le panier fictif.
- **Étape 4 — GitHub :** sauvegarder chaque amélioration dans un commit.
- **Étape 5 — Pages supplémentaires :** ajouter une page « Notre histoire » et une page « Contact ».
- **Étape 6 — Vrai commerce (plus tard) :** passer à une solution e-commerce sécurisée, avec paiement, gestion des commandes et obligations légales. GitHub Pages seul ne permet pas de gérer un véritable processus de paiement.

## À savoir

- Ce projet est pédagogique. Il n'accepte **aucun paiement ni aucune commande**.
- Les produits, prix, engagements et l'identité Maison Miette sont fictifs.
- Les cookies sont des **illustrations SVG originales**, pas des photographies de produits.
- Une connexion Internet peut être nécessaire pour charger les polices Google ; le site reste lisible sans elles.
