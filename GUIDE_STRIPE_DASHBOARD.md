# 💳 Guide Stripe + Dashboard - InnovAfrique

## 🎯 Ce qui a été implémenté

### 1. **Paiement Stripe (Mode Test)**
- ✅ Intégration complète de Stripe Checkout
- ✅ Page de paiement sécurisée
- ✅ Gestion des succès/annulations
- ✅ Webhooks pour automatisation
- ✅ Bouton "Payer maintenant" sur les commandes

### 2. **Dashboard Admin Personnalisé**
- ✅ Statistiques de ventes en temps réel
- ✅ Chiffre d'affaires total, mensuel, hebdomadaire
- ✅ Nombre de commandes et clients
- ✅ Top 5 produits les plus vendus
- ✅ Commandes récentes
- ✅ Taux de conversion
- ✅ Panier moyen

---

## 🚀 Comment utiliser

### A. Tester les paiements Stripe

#### 1. **Obtenir les clés de test Stripe** (GRATUIT)

1. Allez sur https://dashboard.stripe.com/register
2. Créez un compte gratuit
3. Activez le **mode test** (toggle en haut à droite)
4. Allez dans **Developers** → **API keys**
5. Copiez :
   - **Publishable key** (commence par `pk_test_...`)
   - **Secret key** (commence par `sk_test_...`)

#### 2. **Configurer les clés dans votre projet**

Modifiez le fichier `.env` :
```env
STRIPE_PUBLIC_KEY=pk_test_VOTRE_CLE_PUBLIQUE
STRIPE_SECRET_KEY=sk_test_VOTRE_CLE_SECRETE
```

#### 3. **Tester un paiement**

1. Passez une commande sur le site
2. Sur la page de détail de commande, cliquez sur **"Payer maintenant"**
3. Utilisez une carte de test :
   - **Numéro** : `4242 4242 4242 4242`
   - **Date** : N'importe quelle date future (ex: 12/25)
   - **CVV** : N'importe quel 3 chiffres (ex: 123)
   - **Nom** : N'importe quel nom

4. Le paiement sera traité et vous serez redirigé vers la page de succès

#### 4. **Autres cartes de test**

- **Paiement réussi** : `4242 4242 4242 4242`
- **Carte refusée** : `4000 0000 0000 0002`
- **Authentification requise** : `4000 0025 0000 3155`
- **Fonds insuffisants** : `4000 0000 0000 9995`

---

### B. Accéder au Dashboard Admin

#### 1. **Accéder au dashboard**

1. Connectez-vous à l'admin : http://127.0.0.1:8000/admin/
2. Cliquez sur **"Dashboard"** dans le menu (ou allez directement sur http://127.0.0.1:8000/admin/dashboard/)

#### 2. **Ce que vous verrez**

**Statistiques principales** (4 cartes colorées) :
- 💰 **Chiffre d'affaires total** - Somme de toutes les commandes payées
- 📦 **Commandes totales** - Nombre total de commandes
- 👥 **Clients** - Nombre de clients uniques
- 🛍️ **Produits** - Nombre de produits en catalogue

**Statistiques secondaires** (4 cartes) :
- 💰 **CA Mensuel** - Revenus des 30 derniers jours
- 📅 **CA Hebdomadaire** - Revenus des 7 derniers jours
- 🎯 **Taux de conversion** - % de commandes payées
- 🛒 **Panier moyen** - Montant moyen par commande

**Tableaux** :
- 🏆 **Top 5 Produits** - Produits les plus vendus
- 📦 **Commandes récentes** - 10 dernières commandes

---

## 📊 Voir les statistiques Stripe

### Dashboard Stripe (Mode Test)

1. Allez sur https://dashboard.stripe.com/test/dashboard
2. Vous verrez :
   - Graphiques de paiements
   - Liste des transactions
   - Détails des clients
   - Rapports détaillés

### Webhooks (Optionnel)

Pour recevoir les événements Stripe en temps réel :

1. Allez dans **Developers** → **Webhooks**
2. Cliquez sur **Add endpoint**
3. URL : `http://127.0.0.1:8000/payments/webhook/`
4. Sélectionnez les événements : `checkout.session.completed`
5. Copiez le **Signing secret** et ajoutez-le dans `.env` :
   ```env
   STRIPE_WEBHOOK_SECRET=whsec_VOTRE_SECRET
   ```

---

## 🎨 URLs disponibles

### Paiements
- **Page de paiement** : `/payments/process/<order_id>/`
- **Succès** : `/payments/success/<order_id>/`
- **Annulation** : `/payments/cancel/<order_id>/`
- **Webhook** : `/payments/webhook/`

### Admin
- **Dashboard** : `/admin/dashboard/`
- **Commandes** : `/admin/orders/order/`
- **Produits** : `/admin/products/product/`
- **Paiements** : `/admin/payments/payment/`

---

## 💡 Conseils

### Pour tester complètement :

1. **Créez des produits** dans l'admin
2. **Passez plusieurs commandes** avec différents montants
3. **Payez certaines commandes** avec Stripe
4. **Laissez d'autres non payées** pour voir la différence
5. **Consultez le dashboard** pour voir les statistiques

### Données de démonstration :

Pour avoir des statistiques intéressantes :
- Créez au moins 10 commandes
- Payez 7-8 d'entre elles
- Variez les montants (50 000, 100 000, 200 000 FCFA)
- Créez des commandes sur plusieurs jours

---

## 🔒 Sécurité

### Mode Test vs Production

**Mode Test** (actuel) :
- ✅ Gratuit
- ✅ Cartes de test
- ✅ Aucun vrai argent
- ✅ Parfait pour développement

**Mode Production** (futur) :
- ⚠️ Vrais paiements
- ⚠️ Frais Stripe (2.9% + 0.30€)
- ⚠️ Nécessite vérification d'identité
- ⚠️ Changez les clés dans `.env`

---

## 📈 Prochaines étapes

### Améliorations possibles :

1. **Graphiques** - Ajouter des graphiques avec Chart.js
2. **Export** - Exporter les statistiques en PDF/Excel
3. **Notifications** - Emails de confirmation de paiement
4. **Factures** - Génération automatique de factures PDF
5. **Rapports** - Rapports mensuels automatiques

---

## 🆘 Dépannage

### Erreur "No module named 'stripe'"
```bash
.\venv\Scripts\activate
pip install stripe
```

### Paiement ne fonctionne pas
1. Vérifiez que les clés Stripe sont correctes dans `.env`
2. Vérifiez que le serveur Django est lancé
3. Consultez les logs dans le terminal

### Dashboard vide
- Créez des commandes et marquez-les comme payées
- Rafraîchissez la page

---

## ✅ Checklist

- [ ] Compte Stripe créé (mode test)
- [ ] Clés Stripe ajoutées dans `.env`
- [ ] Serveur Django lancé
- [ ] Commande créée
- [ ] Paiement testé avec carte `4242 4242 4242 4242`
- [ ] Dashboard consulté
- [ ] Statistiques visibles

---

**Félicitations ! Vous avez maintenant un système de paiement complet et un dashboard professionnel ! 🎉**
