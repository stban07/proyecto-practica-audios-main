# Generated by Django 4.1.5 on 2023-02-10 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_preregistro'),
    ]

    operations = [
        migrations.AddField(
            model_name='preregistro',
            name='comuna',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.comuna'),
        ),
    ]
