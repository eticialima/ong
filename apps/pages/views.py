from django.shortcuts import render 
from pages.forms import ContactForm
from pages.models import Blocos

# Create your views here.
def index(request):
    return render(request, 'index.html')


def paginas_view(request):
    url_name = request.resolver_match.url_name 
    title_header = {'home': 'Inicio',
                'sobre': 'Sobre',
                'beneficios': 'beneficios', 
                'faq': 'Faq',
                'contato': 'Contato'}
    pagina = {
        'home': Blocos.objects.filter(pagina__nome='inicio',ativo=True).order_by('ordem'),
        'beneficios': Blocos.objects.filter(pagina__nome='beneficios',ativo=True).order_by('ordem'),
        'sobre': Blocos.objects.filter(pagina__nome='sobre',ativo=True).order_by('ordem'),
        'faq': Blocos.objects.filter(pagina__nome='faq',ativo=True).order_by('ordem'),
        'contato': Blocos.objects.filter(pagina__nome='contato',ativo=True).order_by('ordem'),
        }  
    context = {'blocos': pagina[str(url_name)],
               'title_header': title_header.get(url_name, ''),
               'form': ContactForm()}
    return render(request, 'index.html', context)