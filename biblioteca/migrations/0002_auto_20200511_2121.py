# Generated by Django 3.0.6 on 2020-05-12 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='serie',
            field=models.CharField(choices=[('Pré II', 'Pré II'), ('1 Ano', '1 Ano'), ('2 Ano', '2 Ano'), ('3 Ano', '3 Ano'), ('4 Ano', '4 Ano'), ('5 Ano', '5 Ano'), ('6 Ano', '6 Ano'), ('7 Ano', '7 Ano'), ('8 Ano', '8 Ano'), ('9 Ano', '9 Ano')], default='Pré II', max_length=15),
        ),
    ]