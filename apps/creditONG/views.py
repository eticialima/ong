from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum  
from django.contrib import messages 
from django.core.paginator import Paginator 
from .models import Item, Credit, Purchase
 
 
def item_list(request):
    items = Item.objects.all()
    # Aplicar a paginação à lista de tuplas
    paginacao = Paginator(items, 10) # '3' é numero de registro por pagina
    
    # Obter o número da página a partir dos parâmetros da URL
    pagina_numero = request.GET.get("page") # 2 3 4 5 
    page_obj = paginacao.get_page(pagina_numero)
    
    return render(request, 'item_list.html', {'page_obj': page_obj})
  
@login_required
def purchase_item(request, item_id):
    item = Item.objects.get(id=item_id)
    
    try:
        credit = Credit.objects.get(user=request.user)
    except ObjectDoesNotExist:
        messages.error(request, 'Você não tem um registro de crédito.')
        return redirect('item_list')
    
    if credit.balance >= item.price:
        credit.balance -= item.price
        credit.save()

        # Cria uma entrada de compra
        Purchase.objects.create(user=request.user, item=item)

        messages.success(request, 'Compra realizada com sucesso!')
        return redirect('item_list')
    else:
        messages.error(request, 'Saldo de crédito insuficiente.')
        return redirect('item_list')



@login_required
def user_purchases(request):
    user = request.user 
    lista_grupos = ['administrador', 'colaborador'] 
    if any(grupo.name in lista_grupos for grupo in user.groups.all()) or user.is_superuser:
        # Usuário é administrador ou colaborador, pode ver todas as postagens
        purchases = Purchase.objects.all()
    else:
        # Usuário é do grupo usuário, pode ver apenas suas próprias postagens
        purchases = Purchase.objects.filter(user=request.user) 
        
    total_spent = purchases.aggregate(total=Sum('item__price'))['total'] or 0.00 

    paginacao = Paginator(purchases, 10) # '3' é numero de registro por pagina
    
    # Obter o número da página a partir dos parâmetros da URL
    pagina_numero = request.GET.get("page") # 2 3 4 5 
    page_obj = paginacao.get_page(pagina_numero)
    
    return render(request, 'user_purchases.html', {'page_obj': page_obj, 'total_purchases': total_spent})


@login_required
def user_credits(request):
    user = request.user 
    lista_grupos = ['administrador', 'colaborador'] 
    if any(grupo.name in lista_grupos for grupo in user.groups.all()) or user.is_superuser:
        # Usuário é administrador ou colaborador, pode ver todas as postagens
        credits_all = Credit.objects.all()
    else:
        # Usuário é do grupo usuário, pode ver apenas suas próprias postagens
        credits_all = Credit.objects.filter(user=user)
    
    paginacao = Paginator(credits_all, 10) # '3' é numero de registro por pagina
    
    # Obter o número da página a partir dos parâmetros da URL
    pagina_numero = request.GET.get("page") # 2 3 4 5 
    page_obj = paginacao.get_page(pagina_numero)
    
    return render(request, 'user_credits.html', {'page_obj': page_obj})