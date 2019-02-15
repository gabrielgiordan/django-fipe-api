import re
from decimal import Decimal

import requests
import json
from django.http import HttpResponse
from FipeAPI.models import TipoVeiculo, TabelaReferencia, Marca, Modelo, AnoModelo, Valor

api = 'http://veiculos.fipe.org.br/api/veiculos/'


def index(request):
    return HttpResponse('')


def consultar_mes(request):
    return HttpResponse(teste(f)['obj2'])

def f(i):
    print('kkk:' + str(i))

def teste(fun=None):
    o = TabelaReferencia.objects.get(pk=231)
    c = TabelaReferencia.objects.get(pk=230)

    if (callable(fun)):
        for i in range(0, 10):
            fun(i)

    return {'obj': o, 'obj2':c}


def __consultar_mes(request):
    response = __consultar('ConsultarTabelaDeReferencia', {})

    objs = json.loads(response)

    for obj in objs:
        o, created = TabelaReferencia.objects.get_or_create(id=obj['Codigo'], mes=obj['Mes'])
        print(str(created) + ' ' + str(o.id) + ' ' + o.mes)

    return response, objs


def consultar_marcas_de_carros(request, referencia_id):
    return __consultar_marcas(request, 1, referencia_id)


def consultar_modelos_de_carros(request, referencia_id, marca_id):
    return __consultar_modelos(request, 1, referencia_id, marca_id)


def consultar_anos_de_modelo_de_carro(request, referencia_id, marca_id, modelo_id):
    return __consultar_anos_de_modelo(request, 1, referencia_id, marca_id, modelo_id)


def consultar_modelos_de_ano_de_carro(request, referencia_id, marca_id, ano):
    return __consultar_modelos_de_ano(request, 1, referencia_id, marca_id, ano)


def consultar_valor_de_carro(request, referencia_id, marca_id, modelo_id, ano):
    return __consultar_valor(request, 1, referencia_id, marca_id, modelo_id, ano)


def __consultar_valor(request, tipo_veiculo_id, referencia_id, marca_id, modelo_id, ano):
    response = __consultar('ConsultarValorComTodosParametros',
                           __dados(tipo_veiculo_id, referencia_id, marca_id, modelo_id, ano))

    modelo = Modelo.objects.get(pk=modelo_id)
    mes = TabelaReferencia.objects.get(pk=referencia_id)

    obj = json.loads(response)
    valor = re.search(r'\d+[.,]?\d+[.,]?\d+', obj['Valor']).group()
    valor = Decimal(valor.replace('.', '').replace(',', '.'))

    o, created = Valor.objects.get_or_create(codigo_fipe=obj['CodigoFipe'], modelo=modelo, valor=valor, mes_referencia=mes)
    print(str(created) + ' ' + str(o.codigo_fipe) + ' ' + str(o.valor) + ' ' + o.modelo.modelo)

    return HttpResponse(response)


def __consultar_modelos_de_ano(request, tipo_veiculo_id, referencia_id, marca_id, ano):
    response = __consultar('ConsultarModelosAtravesDoAno', __dados(tipo_veiculo_id, referencia_id, marca_id, ano=ano))
    return HttpResponse(response)


def __consultar_anos_de_modelo(request, tipo_veiculo_id, referencia_id, marca_id, modelo_id):
    response = __consultar('ConsultarAnoModelo', __dados(tipo_veiculo_id, referencia_id, marca_id, modelo_id))

    modelo = Modelo.objects.get(pk=modelo_id)

    objs = json.loads(response)

    for obj in objs:
        o, created = AnoModelo.objects.get_or_create(id=obj['Value'], ano=obj['Label'])
        modelo.ano_modelo.add(o)
        print(str(created) + ' ' + str(o.id) + ' ' + o.ano)

    return HttpResponse(response)


def __consultar_modelos(request, tipo_veiculo_id, referencia_id, marca_id):
    response = __consultar('ConsultarModelos', __dados(tipo_veiculo_id, referencia_id, marca_id))

    marca = Marca.objects.get(pk=marca_id)
    tipo_veiculo = TipoVeiculo.objects.get(pk=tipo_veiculo_id)

    objs = json.loads(response)

    for obj in objs['Modelos']:
        o, created = Modelo.objects.get_or_create(id=obj['Value'], modelo=obj['Label'], marca=marca,
                                                  tipo_veiculo=tipo_veiculo)
        print(str(created) + ' ' + str(o.id) + ' ' + o.modelo)

    return HttpResponse(response)


def __consultar_marcas(request, tipo_veiculo_id, referencia_id):
    response = __consultar('ConsultarMarcas', __dados(tipo_veiculo_id, referencia_id))

    objs = json.loads(response)

    for obj in objs:
        o, created = Marca.objects.get_or_create(id=obj['Value'], marca=obj['Label'])
        print(str(created) + ' ' + str(o.id) + ' ' + o.marca)

    return HttpResponse(response)


def __dados(tipo_veiculo_id, referencia_id, marca_id='', modelo_id='', ano=''):
    tipo_veiculo = ''

    for obj in TipoVeiculo.objects.all():
        if obj.id == tipo_veiculo_id:
            tipo_veiculo = obj.veiculo
            break

    dados = {'codigoTipoVeiculo': tipo_veiculo_id,
             'codigoTabelaReferencia': referencia_id,
             'codigoMarca': marca_id,
             'codigoModelo': modelo_id,
             'tipoVeiculo': tipo_veiculo,
             'tipoConsulta': 'tradicional'}

    if ano:
        if '-' in ano:
            split = ano.split('-')
            ano_modelo = split[0]
            tipo_combustivel = split[1]
        else:
            ano_modelo = ano
            tipo_combustivel = ''

        dados = {**dados, **{
            "ano": ano,
            "anoModelo": ano_modelo,
            "codigoTipoCombustivel": tipo_combustivel
        }}

    print(dados)

    return dados


def __consultar(url, json):
    headers = {"Host": "veiculos.fipe.org.br",
               "Referer": "http://veiculos.fipe.org.br",
               "Content-Type": "application/json"}
    req = requests.post(api + url, json=json, headers=headers)
    return req.text


def __consultar_valores(url, json):
    headers = {"Host": "veiculos.fipe.org.br",
               "Referer": "http://veiculos.fipe.org.br",
               "Content-Type": "application/json"}
    req = requests.post(api + url, json=json, headers=headers)
    return req.text


def armazenar(request):
    response = consultar_mes(request)


    return HttpResponse(response)
