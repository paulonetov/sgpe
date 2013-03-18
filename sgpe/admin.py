# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Pedido
from models import Vendedor
from models import Entregador
from models import Roteiro
from django import forms


admin.site.register(Vendedor)

class PedidoEmLinha(admin.TabularInline):
    model = Pedido
    extra = 0
    can_delete = False
    fields = ('nome_Mae','cidade_Entrega','logradouro_Entrega',
              'numero_Entrega','bairro_Entrega','telefone_Entrega',
              'apto_Entrega','cep_Entrega','data_Entrega','observacoes')
    readonly_fields = ('nome_Mae','cidade_Entrega','logradouro_Entrega',
              'numero_Entrega','bairro_Entrega','telefone_Entrega',
              'apto_Entrega','cep_Entrega','data_Entrega')

class RoteitoAdmin(admin.ModelAdmin):
    inlines = [PedidoEmLinha]
    list_display = ('codigo_Roteiro','entregador','descricao_Roteiro')
    list_filter = ['codigo_Roteiro']
    search_fields = ['codigo_Roteiro']

admin.site.register(Roteiro,RoteitoAdmin)


class EntregadorAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
     'fields': (('nome_Entregador', 'email_Entregador'),
                ('telefone_Entregador','telefone_celular_Entregador'),
                ('cidade_Entregador','logradouro_Entregador','numero_Entregador'),
                ('bairro_Entregador','cep_Entregador'))
    }),)
    list_filter = ['cep_Entregador','bairro_Entregador','logradouro_Entregador']
    search_fields = ['cep_Entregador','bairro_Entregador']

admin.site.register(Entregador,EntregadorAdmin)

class PedidoAdminForm(forms.ModelForm):
    class Meta:
        model = Pedido

    def clean(self):
        cleaned_data = super(PedidoAdminForm, self).clean()
        retirada_na_casa = self.cleaned_data['retirada_na_casa']
        nome_Mae = self.cleaned_data['nome_Mae']
        logradouro_Entrega = self.cleaned_data['logradouro_Entrega']
        numero_Entrega = self.cleaned_data['numero_Entrega']
        bairro_Entrega = self.cleaned_data['bairro_Entrega']
        telefone_Entrega = self.cleaned_data['telefone_Entrega']
        cep_Entrega = self.cleaned_data['cep_Entrega']
        data_Entrega = self.cleaned_data['data_Entrega']
        if retirada_na_casa == False:
            if nome_Mae == '':
                raise forms.ValidationError("Como a cesta não será retirada" +
                        "na casa, devem ser preenchidos os campos: Nome mae," +
                        " Logradouro entrega, Numero entrega," +
                        " Bairro entrega, Telefone entrega, Cidade entrega," +
                        " Cep entrega e Data entrega.")
            elif logradouro_Entrega == '':
                raise forms.ValidationError("Como a cesta não será retirada" +
                        "na casa, devem ser preenchidos os campos: Nome mae," +
                        " Logradouro entrega, Numero entrega," +
                        " Bairro entrega, Telefone entrega, Cidade entrega," +
                        " Cep entrega e Data entrega.")
            elif numero_Entrega == None:
                raise forms.ValidationError("Como a cesta não será retirada" +
                        "na casa, devem ser preenchidos os campos: Nome mae," +
                        " Logradouro entrega, Numero entrega," +
                        " Bairro entrega, Telefone entrega, Cidade entrega," +
                        " Cep entrega e Data entrega.")
            elif bairro_Entrega == '':
                raise forms.ValidationError("Como a cesta não será retirada" +
                        "na casa, devem ser preenchidos os campos: Nome mae," +
                        " Logradouro entrega, Numero entrega," +
                        " Bairro entrega, Telefone entrega, Cidade entrega," +
                        " Cep entrega e Data entrega.")
            elif telefone_Entrega == '':
                raise forms.ValidationError("Como a cesta não será retirada" +
                        "na casa, devem ser preenchidos os campos: Nome mae," +
                        " Logradouro entrega, Numero entrega," +
                        " Bairro entrega, Telefone entrega, Cidade entrega," +
                        " Cep entrega e Data entrega.")
            elif cep_Entrega == '':
                raise forms.ValidationError("Como a cesta não será retirada" +
                        "na casa, devem ser preenchidos os campos: Nome mae," +
                        " Logradouro entrega, Numero entrega," +
                        " Bairro entrega, Telefone entrega, Cidade entrega," +
                        " Cep entrega e Data entrega.")
            elif data_Entrega == None:
                raise forms.ValidationError("Como a cesta não será retirada" +
                        "na casa, devem ser preenchidos os campos: Nome mae," +
                        " Logradouro entrega, Numero entrega," +
                        " Bairro entrega, Telefone entrega, Cidade entrega," +
                        " Cep entrega e Data entrega.")
        return cleaned_data

class PedidoAdmin(admin.ModelAdmin):
    form = PedidoAdminForm
    fieldsets = (
        ('Associar Roteiro', {'fields': ['roteiro'], 'classes': ['collapse']}),
        (None,{'fields': ('codigo_Recibo',
                ('nome_Comprador','telefone_Comprador','email_Comprador'),
                'nome_Mae','retirada_na_casa',
                ('logradouro_Entrega','numero_Entrega'),
                ('apto_Entrega','bairro_Entrega','telefone_Entrega'),
                ('cidade_Entrega','cep_Entrega'),
                'data_Entrega',
                ('vendedor', 'data_Venda','tipo_Pagamento', 'tipo_Venda'),
                'endereco_Cartao_Conferido',
                'endereco_Cep_Conferido','ocorreu_Alteracao',
                'observacoes')
    }))
    list_display = ('codigo_Recibo',
		    'logradouro_Entrega','numero_Entrega','apto_Entrega','bairro_Entrega',
		    'data_Entrega','cep_Entrega','observacoes')
    list_filter = ['codigo_Recibo','roteiro','retirada_na_casa']
    search_fields = ['bairroEntrega','cep_Entrega']
    #radio_fields = {"roteiro": admin.HORIZONTAL}
    #raw_id_fields = ("roteiro",)

admin.site.register(Pedido,PedidoAdmin)
