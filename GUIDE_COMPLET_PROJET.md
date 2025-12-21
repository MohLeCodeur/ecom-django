# 📘 Guide Complet du Projet InnovAfrique - E-commerce Django

## 📋 Table des matières

1. [Vue d'ensemble du projet](#vue-densemble-du-projet)
2. [Architecture du projet](#architecture-du-projet)
3. [Applications Django créées](#applications-django-créées)
4. [Structure des fichiers](#structure-des-fichiers)
5. [Fonctionnalités implémentées](#fonctionnalités-implémentées)
6. [Base de données](#base-de-données)
7. [Templates et design](#templates-et-design)
8. [Système de paiement](#système-de-paiement)
9. [Dashboard admin](#dashboard-admin)
10. [Déploiement](#déploiement)

---

## 🎯 Vue d'ensemble du projet

**InnovAfrique** est une plateforme e-commerce complète développée avec Django 5.0.1, permettant de vendre des produits africains innovants en ligne.

### Technologies utilisées :
- **Backend** : Django 5.0.1 (Python 3.13.5)
- **Base de données** : MySQL
- **Frontend** : Bootstrap 5, HTML5, CSS3, JavaScript
- **Paiement** : Stripe (mode test)
- **Environnement** : Python venv
- **Serveur de développement** : Django runserver

---

## 🏗️ Architecture du projet

### Structure générale :

```
Ecommerce Django/
├── innovafrique/          # Configuration principale du projet
│   ├── settings.py        # Paramètres Django
│   ├── urls.py           # URLs principales
│   └── wsgi.py           # Point d'entrée WSGI
│
├── products/             # Application produits
├── cart/                 # Application panier
├── orders/               # Application commandes
├── accounts/             # Application utilisateurs
├── payments/             # Application paiements
│
├── templates/            # Templates HTML
├── static/              # Fichiers statiques (CSS, JS, images)
├── media/               # Fichiers uploadés (images produits)
│
├── manage.py            # Script de gestion Django
├── requirements.txt     # Dépendances Python
├── .env                 # Variables d'environnement
└── venv/               # Environnement virtuel Python
```

---

## 📦 Applications Django créées

### 1. **products** - Gestion des produits

**Rôle** : Gérer les produits, catégories et affichage

**Fichiers principaux** :

#### `products/models.py`
```python
# Modèles de données
- Category : Catégories de produits
- Product : Produits avec prix, stock, images, réductions
```

**Utilité** : Définit la structure des données pour les produits et catégories

#### `products/views.py`
```python
# Vues pour afficher les pages
- home() : Page d'accueil
- product_list() : Liste des produits
- product_detail() : Détail d'un produit
- product_list_by_category() : Produits par catégorie
```

**Utilité** : Contrôle la logique d'affichage des pages produits

#### `products/admin.py`
```python
# Interface d'administration
- CategoryAdmin : Gestion des catégories
- ProductAdmin : Gestion des produits
```

**Utilité** : Configure l'interface admin Django pour gérer les produits

#### `products/urls.py`
```python
# Routes URL
- / : Page d'accueil
- /products/ : Liste des produits
- /products/<slug>/ : Détail d'un produit
- /category/<slug>/ : Produits par catégorie
```

**Utilité** : Définit les URLs accessibles pour les produits

#### `products/templatetags/price_filters.py`
```python
# Filtres personnalisés
- format_price : Formate les prix avec virgules
- fcfa : Ajoute FCFA au prix formaté
```

**Utilité** : Permet de formater les prix (ex: 1,000,000 FCFA)

---

### 2. **cart** - Gestion du panier

**Rôle** : Gérer le panier d'achat en session

**Fichiers principaux** :

#### `cart/cart.py`
```python
# Classe Cart
- add() : Ajouter un produit
- remove() : Retirer un produit
- clear() : Vider le panier
- get_total_price() : Calculer le total
```

**Utilité** : Logique métier du panier stocké en session

#### `cart/views.py`
```python
# Vues du panier
- cart_add() : Ajouter au panier
- cart_remove() : Retirer du panier
- cart_detail() : Afficher le panier
```

**Utilité** : Contrôle les actions sur le panier

#### `cart/context_processors.py`
```python
# Contexte global
- cart() : Rend le panier disponible partout
```

**Utilité** : Permet d'afficher le panier dans tous les templates

---

### 3. **orders** - Gestion des commandes

**Rôle** : Créer et gérer les commandes

**Fichiers principaux** :

#### `orders/models.py`
```python
# Modèles
- Order : Commande avec adresse, total, statut
- OrderItem : Article dans une commande
```

**Utilité** : Structure des commandes en base de données

#### `orders/views.py`
```python
# Vues des commandes
- order_create() : Créer une commande
- order_detail() : Voir une commande
- order_list() : Liste des commandes
```

**Utilité** : Gestion du cycle de vie des commandes

#### `orders/forms.py`
```python
# Formulaire de commande
- OrderCreateForm : Formulaire d'adresse de livraison
```

**Utilité** : Validation des données de commande

---

### 4. **accounts** - Gestion des utilisateurs

**Rôle** : Inscription, connexion, profil

**Fichiers principaux** :

#### `accounts/views.py`
```python
# Vues utilisateur
- register() : Inscription
- login_view() : Connexion
- logout_view() : Déconnexion
- profile() : Profil utilisateur
```

**Utilité** : Gestion de l'authentification

#### `accounts/forms.py`
```python
# Formulaires
- UserRegistrationForm : Inscription
- UserLoginForm : Connexion
- UserProfileForm : Modification profil
```

**Utilité** : Validation des données utilisateur

---

### 5. **payments** - Gestion des paiements

**Rôle** : Intégration Stripe et suivi des paiements

**Fichiers principaux** :

#### `payments/models.py`
```python
# Modèle Payment
- order : Lien vers la commande
- payment_method : Méthode (Stripe, etc.)
- amount : Montant
- status : Statut du paiement
- transaction_id : ID de transaction
```

**Utilité** : Historique des paiements

#### `payments/views.py`
```python
# Vues de paiement
- payment_process() : Page de paiement Stripe
- payment_success() : Paiement réussi
- payment_cancel() : Paiement annulé
- stripe_webhook() : Webhook Stripe
- admin_dashboard() : Dashboard admin
```

**Utilité** : Traitement des paiements et statistiques

#### `payments/admin.py`
```python
# Admin personnalisé
- PaymentAdmin : Gestion des paiements
- admin_dashboard() : Dashboard avec stats
```

**Utilité** : Interface admin pour les paiements

---

## 📁 Structure des fichiers

### Configuration principale

#### `innovafrique/settings.py`
**Utilité** : Configuration globale du projet
- Base de données MySQL
- Applications installées
- Middleware
- Templates
- Fichiers statiques et média
- Internationalisation (français)
- Variables d'environnement

#### `innovafrique/urls.py`
**Utilité** : Routes principales
```python
urlpatterns = [
    path("admin/dashboard/", admin_dashboard),
    path("admin/", admin.site.urls),
    path("", include("products.urls")),
    path("cart/", include("cart.urls")),
    path("orders/", include("orders.urls")),
    path("accounts/", include("accounts.urls")),
    path("payments/", include("payments.urls")),
]
```

#### `.env`
**Utilité** : Variables d'environnement sensibles
```env
SECRET_KEY=...
DEBUG=True
DB_NAME=innovafrique
DB_USER=innovafrique_user
DB_PASSWORD=...
STRIPE_PUBLIC_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
```

#### `requirements.txt`
**Utilité** : Liste des dépendances Python
```
Django==5.0.1
mysqlclient==2.2.0
Pillow==10.1.0
python-decouple==3.8
stripe==7.8.0
django-crispy-forms==2.1
crispy-bootstrap5==2.0.0
django-widget-tweaks==1.5.0
```

---

## 🎨 Templates et design

### Template de base

#### `templates/base.html`
**Utilité** : Template parent pour toutes les pages
- Navigation responsive
- Messages flash
- Footer
- Chargement des CSS/JS
- Favicon SVG

### Templates produits

#### `templates/products/home.html`
**Utilité** : Page d'accueil
- Hero section
- Statistiques
- Produits vedettes
- Catégories
- Nouveautés
- Call-to-action

#### `templates/products/product_list.html`
**Utilité** : Liste des produits
- Barre de recherche
- Filtres (catégorie, prix)
- Tri (prix, nom, date)
- Pagination
- Cartes produits

#### `templates/products/product_detail.html`
**Utilité** : Détail d'un produit
- Breadcrumb
- Galerie d'images
- Informations produit
- Prix et réduction
- Formulaire d'ajout au panier
- Produits similaires

### Templates panier

#### `templates/cart/cart_detail.html`
**Utilité** : Page du panier
- Liste des articles
- Quantités modifiables
- Sous-totaux
- Total
- Bouton de commande

### Templates commandes

#### `templates/orders/order_create.html`
**Utilité** : Formulaire de commande
- Récapitulatif du panier
- Formulaire d'adresse
- Validation

#### `templates/orders/order_detail.html`
**Utilité** : Détail d'une commande
- Informations de commande
- Articles commandés
- Adresse de livraison
- Statut de paiement
- Bouton "Payer maintenant"

#### `templates/orders/order_list.html`
**Utilité** : Liste des commandes
- Historique des commandes
- Statuts
- Montants

### Templates paiements

#### `templates/payments/process.html`
**Utilité** : Page de paiement Stripe
- Résumé de commande
- Instructions cartes de test
- Bouton de paiement

#### `templates/payments/success.html`
**Utilité** : Confirmation de paiement
- Message de succès
- Lien vers la commande

#### `templates/payments/cancel.html`
**Utilité** : Annulation de paiement
- Message d'annulation
- Bouton pour réessayer

### Templates admin

#### `templates/admin/dashboard.html`
**Utilité** : Dashboard administrateur
- Chiffre d'affaires (total, mensuel, hebdomadaire)
- Nombre de commandes, clients, produits
- Taux de conversion
- Panier moyen
- Top 5 produits
- Commandes récentes
- Liens rapides

### Templates utilisateurs

#### `templates/accounts/register.html`
**Utilité** : Inscription
- Formulaire d'inscription
- Validation

#### `templates/accounts/login.html`
**Utilité** : Connexion
- Formulaire de connexion

#### `templates/accounts/profile.html`
**Utilité** : Profil utilisateur
- Informations personnelles
- Modification du profil

---

## 🗄️ Base de données

### Configuration MySQL

**Fichier** : `innovafrique/settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='3306'),
    }
}
```

### Modèles de données

#### Table `products_category`
- id (PK)
- name (varchar)
- slug (varchar, unique)
- image (varchar, nullable)
- created_at (datetime)

#### Table `products_product`
- id (PK)
- category_id (FK → products_category)
- name (varchar)
- slug (varchar, unique)
- description (text)
- price (decimal)
- discount_percentage (decimal)
- stock (int)
- available (boolean)
- image (varchar)
- created_at (datetime)
- updated_at (datetime)

#### Table `orders_order`
- id (PK)
- user_id (FK → auth_user)
- first_name (varchar)
- last_name (varchar)
- email (varchar)
- address (varchar)
- postal_code (varchar)
- city (varchar)
- country (varchar)
- phone (varchar)
- notes (text, nullable)
- total_amount (decimal)
- paid (boolean)
- status (varchar)
- created_at (datetime)
- updated_at (datetime)

#### Table `orders_orderitem`
- id (PK)
- order_id (FK → orders_order)
- product_id (FK → products_product)
- price (decimal)
- quantity (int)

#### Table `payments_payment`
- id (PK)
- order_id (FK → orders_order)
- payment_method (varchar)
- amount (decimal)
- status (varchar)
- transaction_id (varchar)
- created_at (datetime)

### Migrations

**Commandes utilisées** :
```bash
python manage.py makemigrations
python manage.py migrate
```

**Utilité** : Créer et appliquer les modifications de structure de base de données

---

## 💳 Système de paiement Stripe

### Configuration

**Fichier** : `.env`
```env
STRIPE_PUBLIC_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
```

### Flux de paiement

1. **Utilisateur clique sur "Payer maintenant"**
   → `payments/views.py` → `payment_process()`

2. **Création d'une session Stripe Checkout**
   ```python
   stripe.checkout.Session.create(
       payment_method_types=['card'],
       line_items=[...],
       success_url='...',
       cancel_url='...',
   )
   ```

3. **Redirection vers Stripe**
   → Page de paiement Stripe hébergée

4. **Paiement réussi**
   → Redirection vers `/payments/success/<order_id>/`
   → Commande marquée comme payée
   → Création d'un enregistrement Payment

5. **Paiement annulé**
   → Redirection vers `/payments/cancel/<order_id>/`

### Cartes de test Stripe

- **Paiement réussi** : `4242 4242 4242 4242`
- **Carte refusée** : `4000 0000 0000 0002`
- **Date** : N'importe quelle date future
- **CVV** : N'importe quel 3 chiffres

---

## 📊 Dashboard admin

### Accès

**URL** : http://127.0.0.1:8000/admin/dashboard/

**Fichier** : `templates/admin/dashboard.html`

### Statistiques affichées

#### Statistiques principales
- **Chiffre d'affaires total** : Somme de toutes les commandes payées
- **Commandes totales** : Nombre total de commandes
- **Clients** : Nombre de clients uniques
- **Produits** : Nombre de produits en catalogue

#### Statistiques détaillées
- **CA mensuel** : Revenus des 30 derniers jours
- **CA hebdomadaire** : Revenus des 7 derniers jours
- **Taux de conversion** : % de commandes payées
- **Panier moyen** : Montant moyen par commande

#### Tableaux
- **Top 5 produits** : Produits les plus vendus
- **Commandes récentes** : 10 dernières commandes

### Calcul des statistiques

**Fichier** : `payments/views.py` → `admin_dashboard()`

```python
# Chiffre d'affaires
total_revenue = Order.objects.filter(paid=True).aggregate(
    total=Sum('total_amount'))['total'] or 0

# Taux de conversion
paid_orders = Order.objects.filter(paid=True).count()
conversion_rate = (paid_orders / total_orders * 100)

# Panier moyen
average_order = Order.objects.filter(paid=True).aggregate(
    avg=Avg('total_amount'))['avg'] or 0
```

---

## 🎨 Formatage des prix

### Problème initial
Les prix s'affichaient sans séparateurs : `17000000 FCFA`

### Solution implémentée

**Fichier** : `products/templatetags/price_filters.py`

```python
@register.filter(name='fcfa')
def fcfa(value):
    """Formate un prix et ajoute FCFA"""
    formatted = "{:,.0f}".format(float(value))
    return f"{formatted} FCFA"
```

### Utilisation dans les templates

```django
{% load price_filters %}
{{ product.price|fcfa }}
```

**Résultat** : `17,000,000 FCFA` ✨

### Templates modifiés
- `templates/products/home.html`
- `templates/products/product_list.html`
- `templates/products/product_detail.html`
- `templates/cart/cart_detail.html`
- `templates/orders/order_create.html`
- `templates/orders/order_detail.html`
- `templates/orders/order_list.html`
- `templates/admin/dashboard.html`

---

## 🚀 Démarrage du projet

### 1. Installation

```bash
# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Installer les dépendances
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Copier .env.example vers .env
copy .env.example .env  # Windows
cp .env.example .env    # Linux/Mac

# Modifier .env avec vos paramètres
```

### 3. Base de données

```bash
# Créer la base de données MySQL
mysql -u root -p
CREATE DATABASE innovafrique CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'innovafrique_user'@'localhost' IDENTIFIED BY 'votre_mot_de_passe';
GRANT ALL PRIVILEGES ON innovafrique.* TO 'innovafrique_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;

# Appliquer les migrations
python manage.py migrate
```

### 4. Créer un superutilisateur

```bash
python manage.py createsuperuser
```

### 5. Lancer le serveur

```bash
python manage.py runserver
```

**Accès** :
- Site : http://127.0.0.1:8000/
- Admin : http://127.0.0.1:8000/admin/
- Dashboard : http://127.0.0.1:8000/admin/dashboard/

---

## 📝 Fichiers de documentation

### Guides créés

1. **README.md** : Vue d'ensemble du projet
2. **QUICKSTART.md** : Guide de démarrage rapide
3. **GUIDE_COMPLET.md** : Guide détaillé (ce fichier)
4. **FORMATAGE_PRIX.md** : Guide du formatage des prix
5. **GUIDE_STRIPE_DASHBOARD.md** : Guide Stripe et Dashboard
6. **OPTION_C_COMPLETE.md** : Résumé de l'implémentation Stripe
7. **PRIX_ACTIF.md** : Activation du formatage des prix
8. **TEMPLATES_COMPLETS.md** : Liste des templates créés

### Scripts utiles

1. **apply_price_filter.py** : Script pour appliquer le filtre de prix automatiquement

---

## 🔧 Maintenance

### Ajouter un produit

1. Aller sur http://127.0.0.1:8000/admin/
2. Cliquer sur "Products" → "Ajouter"
3. Remplir les informations
4. Uploader une image
5. Sauvegarder

### Gérer les commandes

1. Aller sur http://127.0.0.1:8000/admin/
2. Cliquer sur "Orders"
3. Modifier le statut des commandes

### Voir les statistiques

1. Aller sur http://127.0.0.1:8000/admin/dashboard/
2. Consulter les statistiques en temps réel

---

## 🎯 Fonctionnalités complètes

### ✅ Implémenté

- [x] Gestion des produits et catégories
- [x] Panier d'achat en session
- [x] Système de commandes
- [x] Authentification utilisateurs
- [x] Paiement Stripe (mode test)
- [x] Dashboard admin avec statistiques
- [x] Formatage des prix avec virgules
- [x] Design responsive Bootstrap 5
- [x] Recherche et filtres de produits
- [x] Système de réductions
- [x] Gestion du stock
- [x] Breadcrumb navigation
- [x] Favicon personnalisé

### 🔜 Améliorations possibles

- [ ] Système d'avis clients
- [ ] Wishlist (liste de souhaits)
- [ ] Comparateur de produits
- [ ] Notifications par email
- [ ] Génération de factures PDF
- [ ] Suivi de livraison
- [ ] Programme de fidélité
- [ ] Mode production Stripe
- [ ] Déploiement sur serveur

---

## 📞 Support

Pour toute question, consultez les fichiers de documentation ou le code source.

**Bon développement ! 🚀**
