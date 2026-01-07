# 🚀 Guide de Déploiement sur Render (Plan Gratuit)

Ce guide vous accompagne étape par étape pour déployer votre site e-commerce Django sur Render gratuitement.

## 📋 Prérequis

1. **Compte GitHub** - Pour héberger votre code
2. **Compte Render** - Créez un compte sur [render.com](https://render.com)
3. **Compte Cloudinary** - Pour stocker les images (gratuit) sur [cloudinary.com](https://cloudinary.com)

---

## 🔧 Étape 1 : Préparer Cloudinary

### 1.1 Créer un compte Cloudinary
1. Allez sur [cloudinary.com](https://cloudinary.com)
2. Cliquez sur "Sign Up" et créez un compte gratuit
3. Une fois connecté, allez sur le Dashboard

### 1.2 Récupérer vos identifiants
Sur le Dashboard Cloudinary, vous verrez :
- **Cloud Name** (ex: `dxxxxxx`)
- **API Key** (ex: `123456789012345`)
- **API Secret** (cliquez sur "Reveal" pour voir)

**⚠️ Gardez ces informations, vous en aurez besoin !**

---

## 📦 Étape 2 : Pousser votre code sur GitHub

### 2.1 Initialiser Git (si pas déjà fait)
```bash
git init
git add .
git commit -m "Prêt pour le déploiement sur Render"
```

### 2.2 Créer un dépôt GitHub
1. Allez sur [github.com](https://github.com)
2. Cliquez sur "New repository"
3. Nommez-le (ex: `ecommerce-innovafrique`)
4. Laissez-le **Public** (requis pour le plan gratuit Render)
5. Ne cochez RIEN d'autre
6. Cliquez sur "Create repository"

### 2.3 Pousser votre code
```bash
git remote add origin https://github.com/VOTRE-USERNAME/VOTRE-REPO.git
git branch -M main
git push -u origin main
```

---

## 🗄️ Étape 3 : Créer la base de données PostgreSQL sur Render

### 3.1 Créer une base de données
1. Connectez-vous sur [render.com](https://render.com)
2. Cliquez sur "New +" → "PostgreSQL"
3. Configurez :
   - **Name** : `innovafrique-db` (ou autre nom)
   - **Database** : `innovafrique`
   - **User** : `innovafrique_user`
   - **Region** : Choisissez le plus proche (ex: Frankfurt)
   - **PostgreSQL Version** : 16 (ou la plus récente)
   - **Plan** : **Free** ⚠️ IMPORTANT !

4. Cliquez sur "Create Database"

### 3.2 Récupérer l'URL de connexion
1. Une fois créée, allez dans votre base de données
2. Scrollez jusqu'à "Connections"
3. Copiez l'**Internal Database URL** (commence par `postgresql://`)

**⚠️ Gardez cette URL, vous en aurez besoin !**

**⚠️ ATTENTION** : La base de données gratuite expire après **90 jours**. Vous devrez la recréer.

---

## 🌐 Étape 4 : Déployer le Web Service sur Render

### 4.1 Créer un Web Service
1. Sur Render, cliquez sur "New +" → "Web Service"
2. Connectez votre dépôt GitHub
3. Sélectionnez votre repository `ecommerce-innovafrique`

### 4.2 Configuration du service
Remplissez les champs suivants :

- **Name** : `innovafrique-ecommerce` (ou autre nom)
- **Region** : Même région que votre base de données
- **Branch** : `main`
- **Root Directory** : (laissez vide)
- **Runtime** : `Python 3`
- **Build Command** : 
  ```bash
  bash build.sh
  ```
- **Start Command** :
  ```bash
  gunicorn innovafrique.wsgi:application
  ```
- **Plan** : **Free** ⚠️ IMPORTANT !

### 4.3 Variables d'environnement
Cliquez sur "Advanced" puis "Add Environment Variable" pour chaque variable :

#### Variables obligatoires :

1. **SECRET_KEY**
   - Générez une nouvelle clé : https://djecrety.ir/
   - Copiez-collez la clé générée

2. **DEBUG**
   - Valeur : `False`

3. **ALLOWED_HOSTS**
   - Valeur : `innovafrique-ecommerce.onrender.com` (remplacez par VOTRE nom de service)

4. **CSRF_TRUSTED_ORIGINS**
   - Valeur : `https://innovafrique-ecommerce.onrender.com` (avec https://)

5. **DATABASE_URL**
   - Collez l'**Internal Database URL** de l'étape 3.2

6. **CLOUDINARY_CLOUD_NAME**
   - Votre Cloud Name de Cloudinary (étape 1.2)

7. **CLOUDINARY_API_KEY**
   - Votre API Key de Cloudinary

8. **CLOUDINARY_API_SECRET**
   - Votre API Secret de Cloudinary

#### Variables optionnelles (Stripe) :

9. **STRIPE_PUBLIC_KEY**
   - Votre clé publique Stripe (si vous utilisez Stripe)

10. **STRIPE_SECRET_KEY**
    - Votre clé secrète Stripe

### 4.4 Lancer le déploiement
1. Cliquez sur "Create Web Service"
2. Render va commencer à déployer votre application
3. **Attendez 5-10 minutes** pour le premier déploiement

---

## ✅ Étape 5 : Vérification

### 5.1 Accéder à votre site
Une fois le déploiement terminé (statut "Live" en vert) :
1. Cliquez sur le lien de votre service (ex: `https://innovafrique-ecommerce.onrender.com`)
2. Votre site devrait s'afficher ! 🎉

### 5.2 Créer un superutilisateur
Pour accéder à l'admin Django :

1. Dans Render, allez dans votre Web Service
2. Cliquez sur "Shell" (en haut à droite)
3. Exécutez :
   ```bash
   python manage.py createsuperuser
   ```
4. Suivez les instructions pour créer votre compte admin

### 5.3 Accéder à l'admin
Allez sur : `https://votre-site.onrender.com/admin`

---

## ⚠️ Limitations du Plan Gratuit

### 1. **Service s'endort après 15 minutes d'inactivité**
- Le premier visiteur après une période d'inactivité devra attendre 30-60 secondes
- Les visites suivantes seront normales

### 2. **Base de données expire après 90 jours**
- Vous devrez recréer une nouvelle base de données
- **Solution** : Exportez régulièrement vos données
- Commande pour exporter :
  ```bash
  python manage.py dumpdata > backup.json
  ```

### 3. **Pas de stockage persistant**
- C'est pourquoi nous utilisons Cloudinary
- Toutes les images sont stockées dans le cloud

### 4. **750 heures/mois maximum**
- Suffisant pour un site qui tourne 24/7 (744 heures/mois)

---

## 🔄 Mettre à jour votre site

Après avoir modifié votre code localement :

```bash
git add .
git commit -m "Description de vos modifications"
git push origin main
```

Render détectera automatiquement les changements et redéploiera votre site.

---

## 🆘 Dépannage

### Le site ne se charge pas
1. Vérifiez les logs dans Render (onglet "Logs")
2. Vérifiez que toutes les variables d'environnement sont correctes
3. Vérifiez que `ALLOWED_HOSTS` contient votre domaine Render

### Les images ne s'affichent pas
1. Vérifiez vos identifiants Cloudinary
2. Vérifiez que `CLOUDINARY_CLOUD_NAME` est bien renseigné
3. Réuploadez vos images via l'admin Django

### Erreur de base de données
1. Vérifiez que `DATABASE_URL` est correct
2. Vérifiez que la base de données PostgreSQL est bien "Available"
3. Essayez de relancer le service

### Le site est très lent au premier chargement
- C'est normal avec le plan gratuit
- Le service s'endort après 15 minutes d'inactivité
- Solution : Utilisez un service de "ping" gratuit comme [UptimeRobot](https://uptimerobot.com)

---

## 📞 Support

Si vous rencontrez des problèmes :
1. Consultez les logs Render
2. Vérifiez la documentation Render : https://render.com/docs
3. Vérifiez la documentation Django : https://docs.djangoproject.com

---

## 🎉 Félicitations !

Votre site e-commerce est maintenant en ligne gratuitement ! 🚀

**URL de votre site** : `https://votre-nom-service.onrender.com`

---

## 📝 Checklist finale

- [ ] Code poussé sur GitHub
- [ ] Compte Cloudinary créé
- [ ] Base de données PostgreSQL créée sur Render
- [ ] Web Service créé sur Render
- [ ] Toutes les variables d'environnement configurées
- [ ] Site accessible en ligne
- [ ] Superutilisateur créé
- [ ] Admin accessible
- [ ] Images uploadées et visibles

**Bon déploiement ! 🎊**
