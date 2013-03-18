# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from models import Pedido
from models import Vendedor

urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
            queryset=Pedido.objects.order_by('-codigoRecibo')[:5],
            context_object_name='lista_pedido_por_codigoRecibo',
            template_name='sgpe/index.html')),
    (r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Pedido,
            template_name='sgpe/detail.html')),
    #url(r'^(?P<pk>\d+)/resultados/$',
     #   DetailView.as_view(
      #      model=Pedido,
       #     template_name='cestamaes/resultados.html'),
        #name='resultado_pedidos'),
    #(r'^(?P<pedido_id>\d+)/vote/$', 'cestamaes.views.vote'),
)