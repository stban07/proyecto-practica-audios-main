# Generated by Django 4.1.5 on 2023-02-13 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_usuario_comuna'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='comuna',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.comuna'),
        ),
    ]
