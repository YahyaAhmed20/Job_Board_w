# Generated by Django 5.0.2 on 2024-04-03 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='file',
            field=models.FileField(upload_to='apply/'),
        ),
    ]
