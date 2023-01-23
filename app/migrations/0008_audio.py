# Generated by Django 4.1.5 on 2023-01-23 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_profesional_paciente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id_audio', models.BigAutoField(primary_key=True, serialize=False)),
                ('url_audio', models.FileField(upload_to='media')),
                ('timestamp', models.CharField(max_length=100)),
                ('idPaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.paciente')),
            ],
        ),
    ]
