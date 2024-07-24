from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from creditONG.models import Credit
from forum.models import Category, PostagemForum
from config.models import Logo, SEOHome, GoogleAnalytics, Scripts

def context_social(request):
    return {
        'social': 'Exibir este contexto em qualquer lugar!'
        }
 
def get_logo(request):
    return {
        'logo': Logo.objects.all().first()
    }
    
def get_seo(request):
    return {
        'seo': SEOHome.objects.first()
    }
    
def get_ga_code(request):
    return {
        'ga_code': GoogleAnalytics.objects.first()
    }
    
def get_scripts(request):
    return {
        'header_scripts': Scripts.objects.filter(place='HD', is_active=True),
        'footer_scripts': Scripts.objects.filter(place='FT', is_active=True),
    }
 
def get_posts(request):
    return {
        'post_must': PostagemForum.objects.filter(ativo=True).order_by('?'),
        'categories': Category.objects.annotate(
            post_count=Count('category_posts')).filter(post_count__gt=0) 
    }
    
 
def get_user_balance(request):
    if request.user.is_authenticated:
        try:
            credit = Credit.objects.get(user=request.user)
        except ObjectDoesNotExist:
            credit = None
        return {
            'credit_user': credit,
        }
    return {
        'credit_user': None,
    }
