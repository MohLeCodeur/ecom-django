# 🛒 InnovAfrique E-Commerce

Site e-commerce Django déployé sur Render avec plan gratuit.

## 🌟 Fonctionnalités

- ✅ Catalogue de produits
- ✅ Panier d'achat
- ✅ Système de commandes
- ✅ Gestion des comptes utilisateurs
- ✅ Paiement Stripe
- ✅ Interface d'administration Django
- ✅ Stockage des images sur Cloudinary

## 🚀 Technologies

- **Backend** : Django 5.0.1
- **Base de données** : PostgreSQL (production) / SQLite (développement)
- **Stockage média** : Cloudinary
- **Serveur** : Gunicorn
- **Hébergement** : Render (plan gratuit)

## 📦 Installation locale

### Prérequis
- Python 3.11+
- pip

### Étapes

1. **Cloner le repository**
   ```bash
   git clone https://github.com/VOTRE-USERNAME/ecommerce-innovafrique.git
   cd ecommerce-innovafrique
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # ou
   source venv/bin/activate  # Linux/Mac
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer les variables d'environnement**
   - Copiez `.env.example` vers `.env`
   - Remplissez les valeurs nécessaires

5. **Appliquer les migrations**
   ```bash
   python manage.py migrate
   ```

6. **Créer un superutilisateur**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collecter les fichiers statiques**
   ```bash
   python manage.py collectstatic
   ```

8. **Lancer le serveur de développement**
   ```bash
   python manage.py runserver
   ```

9. **Accéder au site**
   - Site : http://localhost:8000
   - Admin : http://localhost:8000/admin

## 🌐 Déploiement sur Render

Consultez le guide détaillé : [DEPLOIEMENT_RENDER.md](DEPLOIEMENT_RENDER.md)

### Résumé rapide

1. Créer un compte Cloudinary (gratuit)
2. Pousser le code sur GitHub (repository public)
3. Créer une base PostgreSQL sur Render (plan gratuit)
4. Créer un Web Service sur Render
5. Configurer les variables d'environnement
6. Déployer ! 🚀

## ⚙️ Variables d'environnement

Voir `.env.example` pour la liste complète.

### Variables essentielles :
- `SECRET_KEY` - Clé secrète Django
- `DEBUG` - Mode debug (False en production)
- `DATABASE_URL` - URL de connexion PostgreSQL
- `ALLOWED_HOSTS` - Domaines autorisés
- `CLOUDINARY_CLOUD_NAME` - Nom cloud Cloudinary
- `CLOUDINARY_API_KEY` - Clé API Cloudinary
- `CLOUDINARY_API_SECRET` - Secret API Cloudinary

## 📁 Structure du projet

```
ecommerce-innovafrique/
├── accounts/          # Gestion des comptes utilisateurs
├── cart/              # Panier d'achat
├── orders/            # Gestion des commandes
├── payments/          # Intégration Stripe
├── products/          # Catalogue produits
├── innovafrique/      # Configuration Django
├── static/            # Fichiers statiques (CSS, JS, images)
├── templates/         # Templates HTML
├── media/             # Fichiers uploadés (local uniquement)
├── requirements.txt   # Dépendances Python
├── build.sh           # Script de build Render
└── manage.py          # Script de gestion Django
```

## 🔧 Commandes utiles

### Développement
```bash
# Créer une nouvelle app
python manage.py startapp nom_app

# Créer des migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Lancer le serveur
python manage.py runserver
```

### Production
```bash
# Collecter les fichiers statiques
python manage.py collectstatic --no-input

# Créer un superutilisateur
python manage.py createsuperuser

# Exporter les données
python manage.py dumpdata > backup.json

# Importer les données
python manage.py loaddata backup.json
```

## ⚠️ Limitations du plan gratuit Render

- Service s'endort après 15 min d'inactivité (démarrage lent au réveil)
- Base de données expire après 90 jours
- 750 heures/mois maximum
- Pas de stockage persistant (d'où Cloudinary)

## 📝 License

Ce projet est sous licence MIT.

## 👨‍💻 Auteur

InnovAfrique Team

## 🆘 Support

Pour toute question, consultez :
- [Guide de déploiement](DEPLOIEMENT_RENDER.md)
- [Documentation Django](https://docs.djangoproject.com)
- [Documentation Render](https://render.com/docs)
