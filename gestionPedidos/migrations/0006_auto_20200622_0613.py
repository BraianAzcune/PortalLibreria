# Generated by Django 3.0.7 on 2020-06-22 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0005_auto_20200622_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libroinstancias',
            name='libro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='libroInstancia', to='gestionPedidos.Libros'),
        ),
    ]
