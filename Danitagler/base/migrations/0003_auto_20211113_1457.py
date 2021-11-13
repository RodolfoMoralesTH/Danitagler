# Generated by Django 3.2.9 on 2021-11-13 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20211113_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='modules',
            field=models.ManyToManyField(blank=True, related_name='modules', to='base.Module'),
        ),
        migrations.AddField(
            model_name='module',
            name='aula',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.clase'),
        ),
        migrations.AddField(
            model_name='module',
            name='tasks',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='base.ModuleTask'),
        ),
        migrations.AddField(
            model_name='moduletask',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='moduletask',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.module'),
        ),
    ]
