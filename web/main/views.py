import django
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse


from .models import Object


def index(request):
    NAME_APP = "Object_buider_732"
    object_list = Object.objects.all()
    return render(request,'main/index.html',{
        "name": NAME_APP,
        "object_list": object_list,
    })



#______________________________________
# ______________old___________________
#______________________________________

#def index(request):
#    latest_articles_list = News.objects.order_by('-pub_date')
#    news_counter = len(latest_articles_list)
#    fixed_set = News.objects.filter(news_is_fixed__icontains=True)
#    return render(request, 'main/index.html', {"article_list": latest_articles_list, "count": news_counter, "range": range(news_counter), "last_four": latest_articles_list[:4], "fix": fixed_set})
