# Generated by Django 4.1.7 on 2023-03-27 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0004_livro_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='editora',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='livraria.editora'),
            preserve_default=False,
        ),
    ]
