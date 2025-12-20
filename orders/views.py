from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


@login_required
def order_create(request):
    """Créer une commande à partir du panier"""
    cart = Cart(request)
    
    if len(cart) == 0:
        messages.warning(request, 'Votre panier est vide.')
        return redirect('cart:cart_detail')
    
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_amount = cart.get_total_price()
            order.save()
            
            # Créer les articles de commande
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
                
                # Mettre à jour le stock
                product = item['product']
                product.stock -= item['quantity']
                product.save()
            
            # Vider le panier
            cart.clear()
            
            messages.success(request, f'Votre commande #{order.id} a été créée avec succès.')
            return redirect('orders:order_detail', order_id=order.id)
    else:
        # Pré-remplir le formulaire avec les données du profil
        initial_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        }
        
        if hasattr(request.user, 'profile'):
            profile = request.user.profile
            initial_data.update({
                'phone': profile.phone,
                'address': profile.address,
                'city': profile.city,
                'postal_code': profile.postal_code,
                'country': profile.country,
            })
        
        form = OrderCreateForm(initial=initial_data)
    
    return render(request, 'orders/order_create.html', {'cart': cart, 'form': form})


@login_required
def order_detail(request, order_id):
    """Détail d'une commande"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})


@login_required
def order_list(request):
    """Liste des commandes de l'utilisateur"""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})
