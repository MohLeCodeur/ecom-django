# Guide de démarrage rapide - InnovAfrique

## Étape 1 : Installer et configurer MySQL

### Installation de MySQL
1. Téléchargez MySQL depuis : https://dev.mysql.com/downloads/installer/
2. Installez MySQL Server et MySQL Workbench
3. Notez le mot de passe root que vous définissez pendant l'installation

### Créer la base de données
Ouvrez MySQL Workbench ou la ligne de commande MySQL et exécutez :

```sql
CREATE DATABASE innovafrique CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'innovafrique_user'@'localhost' IDENTIFIED BY 'innovafrique2024';
GRANT ALL PRIVILEGES ON innovafrique.* TO 'innovafrique_user'@'localhost';
FLUSH PRIVILEGES;
```

**OU** utilisez le fichier SQL fourni :
```bash
mysql -u root -p < database_setup.sql
```

## Étape 2 : Configurer le fichier .env

Le fichier `.env` est déjà créé avec les paramètres par défaut. Si vous avez utilisé un mot de passe différent pour MySQL, modifiez-le :

```env
DB_PASSWORD=votre_mot_de_passe_mysql
```

## Étape 3 : Appliquer les migrations

Les migrations sont déjà créées. Appliquez-les à la base de données :

```bash
.\venv\Scripts\activate
python manage.py migrate
```

## Étape 4 : Créer un superutilisateur

```bash
python manage.py createsuperuser
```

Suivez les instructions pour créer votre compte administrateur.

## Étape 5 : Lancer le serveur

```bash
python manage.py runserver
```

Le site sera accessible à : **http://127.0.0.1:8000/**
L'interface admin à : **http://127.0.0.1:8000/admin/**

## Étape 6 : Ajouter des données de test

1. Connectez-vous à l'admin : http://127.0.0.1:8000/admin/
2. Ajoutez des catégories
3. Ajoutez des produits avec images
4. Testez le site !

## Structure du projet

```
Ecommerce Django/
├── innovafrique/          # Configuration principale
│   ├── settings.py        # Paramètres Django
│   ├── urls.py            # URLs principales
│   └── wsgi.py
├── products/              # Gestion des produits
│   ├── models.py          # Modèles (Category, Product, Review)
│   ├── views.py           # Vues
│   ├── urls.py            # URLs
│   └── admin.py           # Configuration admin
├── cart/                  # Panier d'achat
│   ├── cart.py            # Logique du panier
│   ├── views.py           # Vues
│   └── urls.py            # URLs
├── orders/                # Gestion des commandes
│   ├── models.py          # Modèles (Order, OrderItem)
│   ├── views.py           # Vues
│   ├── forms.py           # Formulaires
│   └── urls.py            # URLs
├── accounts/              # Authentification
│   ├── models.py          # Modèle UserProfile
│   ├── views.py           # Vues
│   ├── forms.py           # Formulaires
│   └── urls.py            # URLs
├── payments/              # Paiements
│   ├── models.py          # Modèle Payment
│   └── urls.py            # URLs
├── static/                # Fichiers statiques (CSS, JS)
├── media/                 # Fichiers uploadés
├── templates/             # Templates HTML
├── manage.py              # Script de gestion Django
├── requirements.txt       # Dépendances Python
├── .env                   # Variables d'environnement
└── README.md              # Documentation

```

## Fonctionnalités implémentées

✅ **Produits**
- Catalogue avec catégories
- Recherche et filtres
- Pagination
- Système d'avis
- Images multiples par produit
- Produits vedettes
- Réductions

✅ **Panier**
- Ajout/suppression de produits
- Mise à jour des quantités
- Vérification du stock
- Persistance en session

✅ **Commandes**
- Création de commandes
- Historique des commandes
- Statuts de commande
- Mise à jour automatique du stock

✅ **Utilisateurs**
- Inscription/Connexion
- Profils utilisateurs étendus
- Gestion du profil

✅ **Administration**
- Interface admin complète
- Gestion des produits, catégories, commandes
- Statistiques

## Prochaines étapes

Pour compléter le projet, vous pouvez :

1. **Créer les templates HTML** (actuellement manquants)
2. **Ajouter les fichiers CSS/JS** pour le design
3. **Implémenter le paiement Stripe** dans l'app payments
4. **Ajouter des tests unitaires**
5. **Configurer l'envoi d'emails** pour les confirmations de commande
6. **Ajouter des images de démonstration**

## Besoin d'aide ?

- Documentation Django : https://docs.djangoproject.com/
- Documentation MySQL : https://dev.mysql.com/doc/
- Documentation Stripe : https://stripe.com/docs

Bon développement ! 🚀
