-- Script SQL pour créer la base de données MySQL pour InnovAfrique

-- 1. Créer la base de données
CREATE DATABASE IF NOT EXISTS innovafrique CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 2. Créer l'utilisateur
CREATE USER IF NOT EXISTS 'innovafrique_user'@'localhost' IDENTIFIED BY 'innovafrique2024';

-- 3. Accorder tous les privilèges
GRANT ALL PRIVILEGES ON innovafrique.* TO 'innovafrique_user'@'localhost';

-- 4. Appliquer les changements
FLUSH PRIVILEGES;

-- 5. Utiliser la base de données
USE innovafrique;

-- Afficher les tables (après les migrations Django)
-- SHOW TABLES;
