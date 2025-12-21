# -*- coding: utf-8 -*-
"""
Script pour appliquer automatiquement le filtre price_filters à tous les templates
"""

import os
import re

# Chemin vers le dossier templates
BASE_DIR = r"C:\Users\Mohxl\Documents\Project\Ecommerce Django\templates"

# Liste des fichiers à modifier
files_to_update = [
    os.path.join(BASE_DIR, "products", "product_detail.html"),
    os.path.join(BASE_DIR, "cart", "cart_detail.html"),
    os.path.join(BASE_DIR, "orders", "order_create.html"),
    os.path.join(BASE_DIR, "orders", "order_detail.html"),
    os.path.join(BASE_DIR, "orders", "order_list.html"),
]

def add_load_filter(content):
    """Ajoute {% load price_filters %} après {% extends %}"""
    if "{% load price_filters %}" in content:
        return content
    
    # Chercher {% extends 'base.html' %}
    pattern = r"({% extends ['\"]base\.html['\"] %})"
    replacement = r"\1\n{% load price_filters %}"
    return re.sub(pattern, replacement, content, count=1)

def replace_prices(content):
    """Remplace {{ prix }} FCFA par {{ prix|fcfa }}"""
    # Pattern pour capturer {{ variable }} FCFA
    patterns = [
        (r'\{\{\s*([^}|]+?)\s*\}\}\s*FCFA', r'{{ \1|fcfa }}'),
    ]
    
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    
    return content

def process_file(filepath):
    """Traite un fichier template"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Ajouter le load
        content = add_load_filter(content)
        
        # Remplacer les prix
        content = replace_prices(content)
        
        # Sauvegarder
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"OK - {os.path.basename(filepath)} - Modifie")
        return True
    except Exception as e:
        print(f"ERREUR - {os.path.basename(filepath)} - {e}")
        return False

if __name__ == "__main__":
    print("Application du filtre price_filters...\n")
    
    success_count = 0
    for filepath in files_to_update:
        if os.path.exists(filepath):
            if process_file(filepath):
                success_count += 1
        else:
            print(f"ATTENTION - {os.path.basename(filepath)} - Fichier introuvable")
    
    print(f"\nTermine ! {success_count}/{len(files_to_update)} fichiers modifies")
    print("\nRafraichissez votre navigateur pour voir les changements !")
