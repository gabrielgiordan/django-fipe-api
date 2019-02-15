from django.contrib import admin

from .models import TabelaReferencia, TipoVeiculo, Marca, Modelo, AnoModelo, Valor

admin.site.register(TabelaReferencia)
admin.site.register(TipoVeiculo)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(AnoModelo)
admin.site.register(Valor)
