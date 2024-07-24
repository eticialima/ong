from django.db.models import Q
from django.db import models

class PostagemForumManager(models.Manager):

    def search(self, query=None):   
        qs = self.get_queryset().distinct()
        if query is not None:
            or_lookup = (Q(titulo__icontains=query) | Q(descricao__icontains=query) | Q(categories__name__icontains=query))
            qs = qs.filter(or_lookup).distinct()
        return qs
