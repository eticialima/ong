from django.contrib import admin
from pages import models

# Register your models here.
admin.site.register(models.Pagina)
admin.site.register(models.TipoBloco)  

class ConteudoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'titulo_1',)
    search_fields = ('nome', 'titulo_1',)
admin.site.register(models.Conteudo, ConteudoAdmin)


class BlocosAdmin(admin.ModelAdmin):
    list_display = ('ordem', 'titulo', 'pagina', 'bloco', 'ativo',)
    list_filter = ('pagina', 'bloco', 'ativo',)
    search_fields = ('titulo', 'descricao',)
    list_display_links = ('titulo',)
    list_editable = ('ordem','ativo',) 

admin.site.register(models.Blocos, BlocosAdmin)