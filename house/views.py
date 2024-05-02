from django.shortcuts import render
from typing import Any
from django.db.models.query import QuerySet
from house.models import House
from house.form import HouseModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class HouseListView(ListView):
    model = House
    template_name = 'house.html'
    context_object_name = 'house'

    def get_queryset(self):
        house = super().get_queryset().order_by('address')

        search = self.request.GET.get('search')
        if search:
            house = house.filter(address__icontains=search)
        return house
    
class HouseDetail(DetailView):
    model = House
    template_name = 'house_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewHouseView(CreateView):
    model = House
    form_class = HouseModelForm
    template_name = 'new_house.html'
    success_url = '/house/'

method_decorator(login_required(login_url='login'), name='dispatch')
class HouseUpdateView(UpdateView):
    model = House
    form_class = HouseModelForm
    template_name = 'house_update.html'
    
    def get_success_url(self):
        return reverse_lazy('house_detail', kwargs={'pk': self.object.pk})
    
method_decorator(login_required(login_url='login'), name='dispatch')
class HouseDeleteView(DeleteView):
    model = House
    template_name = 'house_delete.html'
    success_url = '/house/'