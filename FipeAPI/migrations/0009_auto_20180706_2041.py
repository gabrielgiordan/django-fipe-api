# Generated by Django 2.0.6 on 2018-07-06 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FipeAPI', '0008_modelo_tipo_veiculo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnoModelo',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('ano', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCombustivel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('combustivel', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Valor',
            fields=[
                ('codigo_fipe', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='modelo',
            name='modelo',
            field=models.CharField(max_length=64),
        ),
        migrations.AddField(
            model_name='valor',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FipeAPI.Modelo'),
        ),
        migrations.AddField(
            model_name='modelo',
            name='ano_modelo',
            field=models.ManyToManyField(to='FipeAPI.AnoModelo'),
        ),
    ]
