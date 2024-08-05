from django.shortcuts import HttpResponse,render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Cliente, Carro
import re
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

# Create your views here.
def clientes(request):
    if request.method == 'GET':
      clientes_list = Cliente.objects.all()
      return render(request, 'clientes.html', {'clientes':clientes_list})
    elif request.method == 'POST':
       nome = request.POST.get('nome')
       sobrenome = request.POST.get('Sobrenome')
       email = request.POST.get('email')
       bi = request.POST.get('BI')
       carros = request.POST.getlist('carro')
       matriculas = request.POST.getlist('matricula')
       anos = request.POST.getlist('ano')

       cliente = Cliente.objects.filter(bi=bi)

       if cliente.exists():
          return render(request, 'clientes.html', {'nome': nome, 'sobrenome ': sobrenome, 'email': email, 'carros': zip(carros,matriculas,anos)})
       if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
          return render(request, 'clientes.html', {'nome': nome, 'sobrenome ': sobrenome, 'bi': bi, 'carros': zip(carros,matriculas,anos)})

       cliente = Cliente(
          nome = nome,
          sobrenome = sobrenome,
          email = email,
          bi = bi
       )

       cliente.save()
       
       for carro, matricula, ano in zip(carros,matriculas,anos):
          car = Carro(carro=carro, matricula=matricula, ano=ano, cliente=cliente)
          car.save()
       return HttpResponse('Teste')

def atualiza_cliente(request,):
   id_cliente = request.POST.get('id_cliente')
   
   cliente = Cliente.objects.filter(id=id_cliente)
   carros = Carro.objects.filter(cliente=cliente[0])
   print(carros)
   cliente_json = json.loads(serializers.serialize('json', cliente))[0]['fields']
   cliente_id = json.loads(serializers.serialize('json', cliente))[0]['pk']

   carros_json = json.loads(serializers.serialize('json', carros))
   carros_json = [{'fields': carro['fields'], 'id':carro['pk']} for carro in carros_json]
   data = {'cliente': cliente_json, 'carros':carros_json, 'cliente_id': cliente_id}
   return JsonResponse(data)


@csrf_exempt
def update_carro(request, id):
   nome_carro = request.POST.get('carro')
   matricula = request.POST.get('matricula')
   ano = request.POST.get('ano')
   

   carro = Carro.objects.get(id=id)
   list_carros = Carro.objects.filter(matricula=matricula).exclude(id=id)
   if list_carros.exists():
      return HttpResponse('matricula ja existente')
   carro.carro = nome_carro
   carro.matricula = matricula
   carro.ano = ano
   carro.save()
   return HttpResponse('Dados alterados com sucesso')


def excluir_carro(request, id):
   try:
      carro = Carro.objects.get(id=id)
      carro.delete()
      return redirect(reverse('clientes')+f'aba=atualizar_cliente&id_cliente={id}')
   except:
      return redirect(reverse('clientes')+f'aba=atualizar_cliente&id_cliente={id}')
   

def update_cliente(request, id):
     body = json.loads(request.body)

     nome = body['nome']
     sobrenome = body['sobrenome']
     email = body['email']
     bi = body['bi']

     cliente = get_object_or_404(Cliente, id=id)
     try:
         cliente.nome = nome
         cliente.sobrenome = sobrenome
         cliente.email = email
         cliente.bi = bi
         cliente.save() 
         return JsonResponse({'status':'200','nome': nome,'sobrenome': sobrenome, 'email': email, 'bi': bi})
       #Fazer validacoes como no Carro
     except:
         return JsonResponse({'status':'500'})
        

     


