# Generated by Django 4.2.4 on 2023-10-10 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0020_carrera_sede_mallacurricular_sede'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='cantidad',
            new_name='cantidad_disponible',
        ),
        migrations.AddField(
            model_name='prestamoproducto',
            name='cantidad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='cantidad_total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]