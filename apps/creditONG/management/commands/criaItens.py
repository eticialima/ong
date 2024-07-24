import random
from django.core.management.base import BaseCommand

from creditONG.models import Item 

class Command(BaseCommand):
    help = 'Popula a tabela de itens com exemplos'

    def handle(self, *args, **kwargs):
        items = [
            'Gas', 'Gasolina', 'Comida', 'Roupa', 'Material Escolar', 'Medicamentos',
            'Livros', 'Produtos de Higiene', 'Brinquedos', 'Alimentos não perecíveis',
            'Roupas de inverno', 'Roupas de verão', 'Sapatos', 'Móveis', 'Utensílios de cozinha',
            'Cobertores', 'Travesseiros', 'Lençóis', 'Material de limpeza', 'Artigos de papelaria',
            'Alimentos perecíveis', 'Produtos de beleza', 'Acessórios de cozinha', 'Ferramentas',
            'Equipamentos esportivos', 'Produtos de saúde', 'Itens de primeiros socorros', 
            'Eletrônicos básicos', 'Itens de jardinagem', 'Artigos de camping', 'Instrumentos musicais',
            'Cestas básicas', 'Equipamentos de segurança', 'Artigos de decoração', 'Alimentos especiais'
        ]

        # Remove itens existentes para evitar duplicados
        Item.objects.all().delete()

        for item in items:
            price = round(random.uniform(10.00, 100.00), 2)  # Gera um preço aleatório entre 10 e 100
            Item.objects.create(name=item, price=price)
            self.stdout.write(self.style.SUCCESS(f'Item "{item}" adicionado com preço R${price}'))

