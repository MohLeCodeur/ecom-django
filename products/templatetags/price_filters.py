from django import template

register = template.Library()


@register.filter(name='format_price')
def format_price(value):
    """
    Formate un prix avec virgules comme séparateurs de milliers et point pour les décimales.
    Exemple: 17000000.78 -> 17,000,000.78
    """
    try:
        # Convertir en float si ce n'est pas déjà le cas
        value = float(value)
        
        # Séparer la partie entière et décimale
        if value == int(value):
            # Pas de décimales
            formatted = "{:,.0f}".format(value)
        else:
            # Avec décimales
            formatted = "{:,.2f}".format(value)
        
        return formatted
    except (ValueError, TypeError):
        return value


@register.filter(name='fcfa')
def fcfa(value):
    """
    Formate un prix et ajoute FCFA.
    Exemple: 17000000 -> 17,000,000 FCFA
    """
    formatted = format_price(value)
    return f"{formatted} FCFA"
