# Generated by Django 3.0.4 on 2020-09-09 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0005_delete_aquisicao'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Gasto',
        ),
        migrations.RemoveField(
            model_name='material',
            name='id',
        ),
        migrations.AlterField(
            model_name='material',
            name='nome',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]