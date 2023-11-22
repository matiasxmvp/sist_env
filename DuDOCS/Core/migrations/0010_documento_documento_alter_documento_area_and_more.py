# Generated by Django 4.2.4 on 2023-09-07 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0009_alter_newuser_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='documento',
            field=models.BinaryField(null=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='area',
            field=models.CharField(choices=[('Financiamiento', 'Financiamiento'), ('I+D+I', 'I+D+I'), ('CoordinacionDocente', 'CoordinacionDocente'), ('AsusntosEstudiantiles', 'AsusntosEstudiantiles'), ('Dara', 'Dara')], max_length=255),
        ),
        migrations.AlterField(
            model_name='documento',
            name='descripcion',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='documento',
            name='nombre',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='sede',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Core.sede'),
        ),
    ]
