# Generated by Django 3.0.6 on 2020-05-27 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0006_aluno_emprestimo_livro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='usuario',
        ),
    ]
