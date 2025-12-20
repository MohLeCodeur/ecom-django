from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from products.models import Product
from .cart import Cart


def cart_detail(request):
    """Afficher le panier"""
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


@require_POST
def cart_add(request, product_id):
    """Ajouter un produit au panier"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    
    # Vérifier le stock
    if product.stock < quantity:
        messages.error(request, f'Stock insuffisant pour {product.name}. Stock disponible: {product.stock}')
        return redirect('products:product_detail', slug=product.slug)
    
    cart.add(product=product, quantity=quantity)
    messages.success(request, f'{product.name} a été ajouté au panier.')
    
    # Rediriger vers le panier ou la page précédente
    next_url = request.POST.get('next', 'cart:cart_detail')
    return redirect(next_url)


@require_POST
def cart_remove(request, product_id):
    """Retirer un produit du panier"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, f'{product.name} a été retiré du panier.')
    return redirect('cart:cart_detail')


@require_POST
def cart_update(request, product_id):
    """Mettre à jour la quantité d'un produit dans le panier"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity > 0:
        # Vérifier le stock
        if product.stock < quantity:
            messages.error(request, f'Stock insuffisant. Stock disponible: {product.stock}')
        else:
            cart.add(product=product, quantity=quantity, override_quantity=True)
            messages.success(request, 'Panier mis à jour.')
    else:
        cart.remove(product)
        messages.success(request, f'{product.name} a été retiré du panier.')
    
    return redirect('cart:cart_detail')


def cart_clear(request):
    """Vider le panier"""
    cart = Cart(request)
    cart.clear()
    messages.success(request, 'Votre panier a été vidé.')
    return redirect('cart:cart_detail')
