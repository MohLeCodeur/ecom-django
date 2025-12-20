from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    """Formulaire pour créer une commande"""
    
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 
                  'address', 'city', 'postal_code', 'country', 'notes']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse complète'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ville'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code postal'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pays'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Notes supplémentaires (optionnel)'}),
        }
