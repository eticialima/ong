from django.core.management.base import BaseCommand
from contas.models import MyUser
from forum.models import PostagemForum, Category, Tag 
from django.utils.text import slugify
from forum.models import PostagemForum


class Command(BaseCommand):
    help = "Cria Postagens Aleatoriamente (Teste)"

    def handle(self, *args, **options):  
        categories = [
            {"name": "Educação", "description": "ONGs focadas em educação e alfabetização."},
            {"name": "Saúde", "description": "ONGs que promovem a saúde e bem-estar."},
            {"name": "Meio Ambiente", "description": "ONGs dedicadas à conservação ambiental."},
            {"name": "Direitos Humanos", "description": "ONGs que defendem os direitos humanos."},
            {"name": "Animais", "description": "ONGs que protegem e resgatam animais."},
            {"name": "Cultura", "description": "ONGs que promovem cultura e artes."},
            {"name": "Assistência Social", "description": "ONGs que oferecem suporte social."},
            {"name": "Desenvolvimento Comunitário", "description": "ONGs que fortalecem comunidades."},
            {"name": "Crianças", "description": "ONGs que trabalham com crianças e jovens."},
            {"name": "Empoderamento Feminino", "description": "ONGs que promovem a igualdade de gênero."},
            {"name": "Esportes", "description": "ONGs que incentivam a prática de esportes."},
            {"name": "Tecnologia", "description": "ONGs que utilizam tecnologia para o bem social."},
        ]

        tags = [
            {"name": "Voluntariado"},
            {"name": "Doações"},
            {"name": "Sustentabilidade"},
            {"name": "Inclusão"},
            {"name": "Igualdade"},
            {"name": "Educação"},
            {"name": "Saúde"},
            {"name": "Cultura"},
            {"name": "Ambiente"},
            {"name": "Direitos"},
        ]

        postagens = [
            {"titulo": "aaNovo Programa de Alfabetização", "descricao": "A ONG Educa+ lançou um novo programa de alfabetização para crianças em comunidades carentes.", "categoria": "Educação", "tags": ["Educação", "Inclusão"]},
            {"titulo": "Campanha de Vacinação", "descricao": "A ONG Saúde para Todos está organizando uma campanha de vacinação contra a gripe.", "categoria": "Saúde", "tags": ["Saúde", "Voluntariado"]},
            {"titulo": "Plantio de Árvores", "descricao": "A ONG Verde Vida realiza um evento de plantio de árvores no próximo fim de semana.", "categoria": "Meio Ambiente", "tags": ["Sustentabilidade", "Ambiente"]},
            {"titulo": "Defesa dos Direitos Humanos", "descricao": "A ONG Direitos Humanos Já promove uma palestra sobre os direitos das mulheres.", "categoria": "Direitos Humanos", "tags": ["Direitos", "Igualdade"]},
            {"titulo": "Adoção de Animais", "descricao": "A ONG Amigo Fiel organiza uma feira de adoção de cães e gatos.", "categoria": "Animais", "tags": ["Animais", "Voluntariado"]},
            {"titulo": "Oficina de Arte para Crianças", "descricao": "A ONG Cultura Viva oferece oficinas de arte para crianças em situação de vulnerabilidade.", "categoria": "Cultura", "tags": ["Cultura", "Educação"]},
            {"titulo": "Doações de Alimentos", "descricao": "A ONG Mãos que Ajudam arrecada e distribui alimentos para famílias necessitadas.", "categoria": "Assistência Social", "tags": ["Doações", "Voluntariado"]},
            {"titulo": "Melhoria de Infraestrutura Comunitária", "descricao": "A ONG Comunidade Forte trabalha na melhoria da infraestrutura de bairros carentes.", "categoria": "Desenvolvimento Comunitário", "tags": ["Sustentabilidade", "Inclusão"]},
            {"titulo": "Atividades Recreativas para Crianças", "descricao": "A ONG Criança Feliz organiza atividades recreativas para crianças em abrigos.", "categoria": "Crianças", "tags": ["Crianças", "Voluntariado"]},
            {"titulo": "Workshop sobre Empoderamento Feminino", "descricao": "A ONG Mulheres Unidas promove um workshop sobre empoderamento feminino.", "categoria": "Empoderamento Feminino", "tags": ["Igualdade", "Direitos"]},
            {"titulo": "Torneio Esportivo Comunitário", "descricao": "A ONG Esporte e Vida realiza um torneio esportivo para jovens da comunidade.", "categoria": "Esportes", "tags": ["Esportes", "Saúde"]},
            {"titulo": "Curso de Programação Gratuito", "descricao": "A ONG Tech4Good oferece um curso gratuito de programação para jovens.", "categoria": "Tecnologia", "tags": ["Educação", "Tecnologia"]},
            {"titulo": "Educação Ambiental nas Escolas", "descricao": "A ONG Verde Escola desenvolve um projeto de educação ambiental em escolas públicas.", "categoria": "Meio Ambiente", "tags": ["Ambiente", "Educação"]},
            {"titulo": "Treinamento de Primeiros Socorros", "descricao": "A ONG Salvavidas oferece treinamento de primeiros socorros para a comunidade.", "categoria": "Saúde", "tags": ["Saúde", "Voluntariado"]},
            {"titulo": "Palestra sobre Direitos Civis", "descricao": "A ONG Vozes Ativas organiza uma palestra sobre direitos civis e cidadania.", "categoria": "Direitos Humanos", "tags": ["Direitos", "Igualdade"]},
            {"titulo": "Resgate de Animais em Situação de Risco", "descricao": "A ONG Protetores em Ação realiza resgates de animais em situação de risco.", "categoria": "Animais", "tags": ["Animais", "Voluntariado"]},
            {"titulo": "Festival de Cultura Local", "descricao": "A ONG Raízes Culturais promove um festival para celebrar a cultura local.", "categoria": "Cultura", "tags": ["Cultura", "Inclusão"]},
            {"titulo": "Assistência a Moradores de Rua", "descricao": "A ONG Cuidar de Todos oferece assistência a moradores de rua com doações e suporte psicológico.", "categoria": "Assistência Social", "tags": ["Doações", "Voluntariado"]},
            {"titulo": "Projeto de Reurbanização", "descricao": "A ONG Novo Amanhã trabalha em um projeto de reurbanização em favelas.", "categoria": "Desenvolvimento Comunitário", "tags": ["Sustentabilidade", "Inclusão"]},
            {"titulo": "Apoio Psicológico para Crianças", "descricao": "A ONG Criança Segura oferece apoio psicológico para crianças vítimas de violência.", "categoria": "Crianças", "tags": ["Crianças", "Saúde"]},
            {"titulo": "Grupo de Apoio a Mulheres", "descricao": "A ONG Mulheres de Coragem cria um grupo de apoio para mulheres vítimas de violência doméstica.", "categoria": "Empoderamento Feminino", "tags": ["Igualdade", "Direitos"]},
            {"titulo": "Clínica de Saúde Gratuita", "descricao": "A ONG Saúde na Comunidade abre uma clínica gratuita para atendimento básico de saúde.", "categoria": "Saúde", "tags": ["Saúde", "Inclusão"]},
            {"titulo": "Campanha de Conscientização Ambiental", "descricao": "A ONG Terra Viva lança uma campanha de conscientização ambiental nas redes sociais.", "categoria": "Meio Ambiente", "tags": ["Sustentabilidade", "Ambiente"]},
            {"titulo": "Curso de Teatro para Jovens", "descricao": "A ONG Arte Jovem oferece um curso de teatro gratuito para jovens da periferia.", "categoria": "Cultura", "tags": ["Cultura", "Educação"]},
            {"titulo": "Distribuição de Kits de Higiene", "descricao": "A ONG Solidariedade em Ação distribui kits de higiene para famílias afetadas pela pandemia.", "categoria": "Assistência Social", "tags": ["Doações", "Voluntariado"]},
            {"titulo": "Reforma de Espaços Públicos", "descricao": "A ONG Comunidade Renovada trabalha na reforma de praças e parques públicos.", "categoria": "Desenvolvimento Comunitário", "tags": ["Sustentabilidade", "Inclusão"]},
            {"titulo": "Brinquedoteca Itinerante", "descricao": "A ONG Alegria Criança leva uma brinquedoteca itinerante para áreas rurais.", "categoria": "Crianças", "tags": ["Crianças", "Voluntariado"]},
            {"titulo": "Ciclo de Palestras sobre Igualdade de Gênero", "descricao": "A ONG Gênero em Foco promove um ciclo de palestras sobre igualdade de gênero.", "categoria": "Empoderamento Feminino", "tags": ["Igualdade", "Direitos"]},
            {"titulo": "Apoio a Pacientes com Doenças Crônicas", "descricao": "A ONG Vida Plena oferece apoio a pacientes com doenças crônicas e seus familiares.", "categoria": "Saúde", "tags": ["Saúde", "Inclusão"]},
            {"titulo": "Limpeza de Praias", "descricao": "A ONG Oceanos Limpos organiza mutirões de limpeza de praias em todo o país.", "categoria": "Meio Ambiente", "tags": ["Sustentabilidade", "Ambiente"]},
            {"titulo": "Projeto de Música para Jovens", "descricao": "A ONG Som do Futuro oferece aulas de música para jovens de baixa renda.", "categoria": "Cultura", "tags": ["Cultura", "Educação"]},
            {"titulo": "Doação de Roupas para Necessitados", "descricao": "A ONG Aquecer promove campanhas de doação de roupas para pessoas em situação de rua.", "categoria": "Assistência Social", "tags": ["Doações", "Voluntariado"]},
            {"titulo": "Capacitação Profissional para Comunidades Carentes", "descricao": "A ONG Futuro Melhor oferece cursos de capacitação profissional para moradores de comunidades carentes.", "categoria": "Desenvolvimento Comunitário", "tags": ["Educação", "Inclusão"]},
            {"titulo": "Biblioteca Comunitária", "descricao": "A ONG Ler e Crescer inaugura uma biblioteca comunitária com livros doados.", "categoria": "Educação", "tags": ["Educação", "Voluntariado"]},
            {"titulo": "Grupo de Apoio para Crianças com Necessidades Especiais", "descricao": "A ONG Inclusão Já cria um grupo de apoio para famílias de crianças com necessidades especiais.", "categoria": "Crianças", "tags": ["Crianças", "Inclusão"]},
            {"titulo": "Incentivo ao Empreendedorismo Feminino", "descricao": "A ONG Mulheres Empreendedoras promove cursos de empreendedorismo para mulheres.", "categoria": "Empoderamento Feminino", "tags": ["Igualdade", "Direitos"]},
            {"titulo": "Ação de Saúde Bucal", "descricao": "A ONG Sorriso Saudável oferece atendimentos gratuitos de saúde bucal em escolas públicas.", "categoria": "Saúde", "tags": ["Saúde", "Voluntariado"]},
            {"titulo": "Projeto de Reflorestamento", "descricao": "A ONG Floresta Viva lança um projeto de reflorestamento em áreas degradadas.", "categoria": "Meio Ambiente", "tags": ["Sustentabilidade", "Ambiente"]},
        ] 
 
        categories_dict = {}
        for cat in categories:
            # category = Category.objects.create(
            #     name=cat["name"],
            #     description=cat["description"],
            #     slug=slugify(cat["name"])
            # )
            categories_dict[cat["name"]] = cat["name"]

        # Criação das tags
        tags_dict = {}
        for tg in tags:
            # tag = Tag.objects.create(name=tg["name"])
            tags_dict[tg["name"]] = tg["name"]

        # Usuário padrão
        usuario = MyUser.objects.get(id=1)

        # Criação das postagens
        for post in postagens:
            postagem = PostagemForum.objects.create(
                usuario=usuario,
                titulo=post["titulo"],
                descricao=post["descricao"],
                ativo=True,
                slug=slugify(post["titulo"])
            )
            postagem.categories.add(Category.objects.get(name=post["categoria"]).id)
            for tag_name in post["tags"]:
                postagem.tags.add(Tag.objects.get(name=tags_dict[tag_name]).id)
            postagem.save()

