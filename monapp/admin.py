from django.contrib import admin
from .models import Produit, Categorie, Article, Commentaire

admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(Article)
admin.site.register(Commentaire)