from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Avg
from django.core.paginator import Paginator
from .models import Category, Product, Review
from cart.cart import Cart


def product_list(request, category_slug=None):
    """Liste des produits avec filtres et pagination"""
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    # Filtre par catégorie
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Recherche
    search_query = request.GET.get('q', '')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Tri
    sort_by = request.GET.get('sort', '-created_at')
    if sort_by in ['price', '-price', 'name', '-name', '-created_at']:
        products = products.order_by(sort_by)
    
    # Pagination
    paginator = Paginator(products, 12)  # 12 produits par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'categories': categories,
        'products': page_obj,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, slug):
    """Détail d'un produit"""
    product = get_object_or_404(Product, slug=slug, available=True)
    reviews = product.reviews.all()
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    
    # Produits similaires
    related_products = Product.objects.filter(
        category=product.category,
        available=True
    ).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'reviews': reviews,
        'average_rating': average_rating,
        'related_products': related_products,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_review(request, product_id):
    """Ajouter un avis sur un produit"""
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        
        if rating and comment:
            # Vérifier si l'utilisateur a déjà laissé un avis
            existing_review = Review.objects.filter(
                product=product,
                user=request.user
            ).first()
            
            if existing_review:
                messages.warning(request, 'Vous avez déjà laissé un avis pour ce produit.')
            else:
                Review.objects.create(
                    product=product,
                    user=request.user,
                    rating=rating,
                    comment=comment
                )
                messages.success(request, 'Votre avis a été ajouté avec succès.')
        else:
            messages.error(request, 'Veuillez remplir tous les champs.')
    
    return redirect('products:product_detail', slug=product.slug)


def home(request):
    """Page d'accueil"""
    featured_products = Product.objects.filter(featured=True, available=True)[:8]
    categories = Category.objects.all()[:6]
    latest_products = Product.objects.filter(available=True).order_by('-created_at')[:8]
    
    context = {
        'featured_products': featured_products,
        'categories': categories,
        'latest_products': latest_products,
    }
    return render(request, 'products/home.html', context)
