# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

TIPO_PAGAMENTO = (
    ('1','Dinheiro'),
    ('2','Cheque'),
    ('3','Cartão'),
)

TIPO_VENDA = (
    ('1', 'a vista na venda'),
    ('2', 'a vista na retirada'),
    ('3', 'a vista na entrega'),
    ('4', 'a prazo 1 vez'),
    ('5', 'a prazo 2 vezes'),
)

class Vendedor(models.Model):
    
    nome_Vendedor = models.CharField(max_length=100,unique=True)
    email_Vendedor = models.EmailField(blank=True)
    telefone_Vendedor = models.CharField(max_length=13,blank=True)
    telefone_celular_Vendedor = models.CharField(max_length=13)
    
    def __unicode__(self):
        return self.nome_Vendedor
    
    class Meta:
        verbose_name_plural = 'Vendedores'


class Entregador(models.Model):
    nome_Entregador = models.CharField(max_length=100,unique=True)
    email_Entregador = models.EmailField(blank=True)
    telefone_Entregador = models.CharField(max_length=13)
    telefone_celular_Entregador = models.CharField(max_length=13)
    cidade_Entregador = models.CharField(max_length=100,blank=True)
    logradouro_Entregador = models.CharField(max_length=100, blank=True)
    numero_Entregador = models.IntegerField(blank=True,null=True)
    bairro_Entregador = models.CharField(max_length=100,blank=True)
    cep_Entregador = models.CharField(max_length=8,blank=True)    

    def __unicode__(self):
        return self.nome_Entregador
    
    class Meta:
        verbose_name_plural = 'Entregadores'

class Roteiro(models.Model):

    entregador = models.ForeignKey(Entregador,blank=True,null=True)  
    codigo_Roteiro = models.IntegerField('Código do Roteiro',max_length=3,unique=True)
    descricao_Roteiro = models.CharField(max_length=30)

    def __unicode__(self):
        return str(self.codigo_Roteiro)

class Pedido(models.Model):
    
    vendedor = models.ForeignKey(Vendedor)
    tipo_Pagamento = models.CharField(max_length=1, choices=TIPO_PAGAMENTO)
    tipo_Venda = models.CharField(max_length=1, choices=TIPO_VENDA)
    roteiro = models.ForeignKey(Roteiro,blank=True,null=True)
    codigo_Recibo = models.IntegerField('Código do Recibo',max_length=5,unique=True)
    data_Venda = models.DateField()
    nome_Comprador = models.CharField(max_length=100)
    email_Comprador = models.EmailField(blank=True)
    telefone_Comprador = models.CharField(max_length=13)
    nome_Mae = models.CharField(max_length=100,blank=True)
    cidade_Entrega = models.CharField(max_length=100,blank=True)
    logradouro_Entrega = models.CharField(max_length=100,blank=True)
    numero_Entrega = models.IntegerField(max_length=5,blank=True,null=True)
    bairro_Entrega = models.CharField(max_length=100,blank=True)
    telefone_Entrega =  models.CharField(max_length=13,blank=True)
    apto_Entrega = models.IntegerField(blank=True,null=True)
    cep_Entrega = models.CharField(max_length=8,blank=True)
    data_Entrega = models.DateTimeField(blank=True,null=True)
    endereco_Cartao_Conferido = models.BooleanField('O endereço do cartão e o endereço do pedido original foram conferidos?')
    endereco_Cep_Conferido = models.BooleanField('O CEP e o endereço do pedido original foram conferidos?')
    ocorreu_Alteracao = models.BooleanField('Ocorreu alguma alteração no pedido original?')
    retirada_na_casa = models.BooleanField('Retirada será na FEC?')
    observacoes = models.TextField('Observações',500,blank=True)
    
#    def save(self, *args, **kwargs):
 #       from django.core.exceptions import ValidationError
  #      if self.retirada_na_casa == False:
   #         raise ValidationError('Como a cesta não será retirada na casa')
    #    else:
     #       super(Pedido, self).save(*args, **kwargs) # Call the "real" save() method.
     
   # def clean(self):
    #    from django.core.exceptions import ValidationError
     #   if self.retirada_na_casa == False:
      #      raise ValidationError('Como a cesta não será retirada na casa,'+ 
       #     ' devem ser preenchidos os campos: Nome mae, Logradouro entrega,'+
        #    ' Numero entrega, Cidade entrega, Bairro entrega, Cep entrega e Data entrega.')
        
    def __unicode__(self):
        return str(self.codigo_Recibo)
