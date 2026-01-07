# 🔧 Commandes de Maintenance

Ce fichier contient toutes les commandes utiles pour gérer votre site en production.

## 📊 Sauvegarder les données

### Exporter toutes les données
```bash
python manage.py dumpdata > backup_$(date +%Y%m%d).json
```

### Exporter seulement les produits
```bash
python manage.py dumpdata products > products_backup.json
```

### Exporter seulement les commandes
```bash
python manage.py dumpdata orders > orders_backup.json
```

## 📥 Restaurer les données

### Importer les données
```bash
python manage.py loaddata backup.json
```

## 🗄️ Gestion de la base de données

### Créer des migrations
```bash
python manage.py makemigrations
```

### Appliquer les migrations
```bash
python manage.py migrate
```

### Voir l'état des migrations
```bash
python manage.py showmigrations
```

### Revenir en arrière (migration précédente)
```bash
python manage.py migrate nom_app numero_migration
```

## 👤 Gestion des utilisateurs

### Créer un superutilisateur
```bash
python manage.py createsuperuser
```

### Changer le mot de passe d'un utilisateur
```bash
python manage.py changepassword nom_utilisateur
```

## 🎨 Fichiers statiques

### Collecter les fichiers statiques
```bash
python manage.py collectstatic --no-input
```

### Supprimer les anciens fichiers statiques
```bash
python manage.py collectstatic --clear --no-input
```

## 🧹 Nettoyage

### Supprimer les sessions expirées
```bash
python manage.py clearsessions
```

### Supprimer les fichiers média orphelins
```bash
python manage.py cleanup_unused_media
```

## 🔍 Debugging

### Ouvrir le shell Django
```bash
python manage.py shell
```

### Vérifier la configuration
```bash
python manage.py check
```

### Voir les requêtes SQL
```bash
python manage.py sqlmigrate nom_app numero_migration
```

## 📦 Render - Commandes spécifiques

### Se connecter au shell Render
1. Allez sur render.com
2. Sélectionnez votre service
3. Cliquez sur "Shell" en haut à droite

### Voir les logs en temps réel
1. Allez sur render.com
2. Sélectionnez votre service
3. Cliquez sur "Logs"

### Redémarrer le service
1. Allez sur render.com
2. Sélectionnez votre service
3. Cliquez sur "Manual Deploy" → "Clear build cache & deploy"

## 🔄 Mise à jour du site

### Workflow complet
```bash
# 1. Modifier le code localement
# 2. Tester localement
python manage.py runserver

# 3. Créer les migrations si nécessaire
python manage.py makemigrations

# 4. Commiter les changements
git add .
git commit -m "Description des modifications"

# 5. Pousser sur GitHub
git push origin main

# 6. Render va automatiquement redéployer
```

## 🗃️ Gestion de la base de données PostgreSQL

### Sauvegarder la base de données (depuis Render Shell)
```bash
pg_dump $DATABASE_URL > backup.sql
```

### Voir la taille de la base de données
```bash
python manage.py dbshell
\l+
\q
```

## 📸 Cloudinary - Gestion des médias

### Lister tous les fichiers
```python
import cloudinary.api
result = cloudinary.api.resources()
print(result)
```

### Supprimer un fichier
```python
import cloudinary.uploader
cloudinary.uploader.destroy('public_id_du_fichier')
```

## ⚙️ Variables d'environnement

### Voir toutes les variables (local)
```bash
cat .env
```

### Mettre à jour une variable sur Render
1. Allez sur render.com
2. Sélectionnez votre service
3. Allez dans "Environment"
4. Modifiez la variable
5. Sauvegardez (le service redémarrera automatiquement)

## 🚨 En cas de problème

### Le site ne répond pas
```bash
# 1. Vérifier les logs Render
# 2. Vérifier que DATABASE_URL est correct
# 3. Redémarrer le service
```

### Erreur 500
```bash
# 1. Mettre DEBUG=True temporairement pour voir l'erreur
# 2. Vérifier les logs
# 3. Vérifier les migrations
python manage.py migrate
```

### Base de données corrompue
```bash
# 1. Exporter les données si possible
python manage.py dumpdata > backup.json

# 2. Réinitialiser les migrations
python manage.py migrate --fake nom_app zero
python manage.py migrate nom_app

# 3. Réimporter les données
python manage.py loaddata backup.json
```

## 📅 Maintenance régulière

### Hebdomadaire
- [ ] Vérifier les logs pour les erreurs
- [ ] Sauvegarder la base de données
- [ ] Vérifier l'espace Cloudinary utilisé

### Mensuel
- [ ] Nettoyer les sessions expirées
- [ ] Vérifier les mises à jour de sécurité Django
- [ ] Exporter une sauvegarde complète

### Tous les 90 jours (IMPORTANT)
- [ ] **Sauvegarder la base de données** (elle va expirer !)
- [ ] Créer une nouvelle base PostgreSQL sur Render
- [ ] Mettre à jour DATABASE_URL
- [ ] Restaurer les données

## 🔐 Sécurité

### Générer une nouvelle SECRET_KEY
```bash
python generate_secret_key.py
```

### Mettre à jour SECRET_KEY sur Render
1. Générer une nouvelle clé
2. Aller dans Render → Environment
3. Modifier SECRET_KEY
4. Sauvegarder (redémarrage automatique)

## 📞 Ressources utiles

- Documentation Django : https://docs.djangoproject.com
- Documentation Render : https://render.com/docs
- Documentation Cloudinary : https://cloudinary.com/documentation
- Support Render : https://render.com/docs/support
