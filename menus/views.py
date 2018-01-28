from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Resturant, MenuItem

class IndexView(generic.ListView):
    model = Resturant
    template_name = 'menus/index.html'
    context_object_name = 'resturant_list'


class DetailView(generic.DetailView):
    model = Resturant
    template_name = 'menus/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_item'] = MenuItem.objects.filter(menusection__name='Drinks')
        return context