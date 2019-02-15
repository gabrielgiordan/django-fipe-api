from django.db import models


class TabelaReferencia(models.Model):
    mes = models.CharField(max_length=32)

    def __str__(self):
        return self.mes + ' (' + str(self.id) + ')'


class TipoVeiculo(models.Model):
    id = models.IntegerField(primary_key=True)
    veiculo = models.CharField(max_length=32)

    def __str__(self):
        return self.veiculo + ' (' + str(self.id) + ')'


class TipoCombustivel(models.Model):
    id = models.IntegerField(primary_key=True)
    combustivel = models.CharField(max_length=32)

    def __str__(self):
        return self.combustivel + ' (' + str(self.id) + ')'


class Marca(models.Model):
    marca = models.CharField(max_length=64)

    def __str__(self):
        return self.marca + ' (' + str(self.id) + ')'


class AnoModelo(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    ano = models.CharField(max_length=32)

    def __str__(self):
        return self.ano + ' (' + str(self.id) + ')'

class Modelo(models.Model):
    modelo = models.CharField(max_length=64)
    tipo_veiculo = models.ForeignKey(TipoVeiculo, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    ano_modelo = models.ManyToManyField(AnoModelo)

    def __str__(self):
        return self.marca.marca + ' - ' + self.modelo + ' (' + str(self.id) + ')'


class Valor(models.Model):
    codigo_fipe = models.CharField(primary_key=True, max_length=32)
    valor = models.DecimalField(max_digits=16, decimal_places=2)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    mes_referencia = models.ForeignKey(TabelaReferencia, on_delete=models.CASCADE)

    def __str__(self):
        return self.modelo.modelo + ' - ' + str(self.valor) + ' (' + str(self.codigo_fipe) + ')'


