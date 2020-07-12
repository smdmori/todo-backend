from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Publication, Article
# Create your views here.
class MyView(TemplateView):
    model = Publication
    p1 = Publication(title='The Python Journal')
    p1.save()
    p2 = Publication(title='Science News')
    p2.save()
    p3 = Publication(title='Science Weekly')
    p3.save()
    
    a1 = Article(headline='Django lets you build Web apps easily')
    a1.save()
    
    a1.publications.add(p1)
    
    a2 = Article(headline='NASA uses Python')
    a2.save()
    a2.publications.add(p1, p2)
    a2.publications.add(p3)
    a2.publications.add(p3)
    
    new_publication = a2.publications.create(title='Highlights for Children')
    
    a1.publications.all()
    
    a2.publications.all()
    
    p2.article_set.all()
    p1.article_set.all()
    Publication.objects.get(id=4).article_set.all()
    
    Article.objects.filter(publications__id=1)
    