# Generated by Django 5.0.2 on 2024-03-15 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='info',
            options={'verbose_name': 'Information', 'verbose_name_plural': 'Information'},
        ),
        migrations.AlterField(
            model_name='info',
            name='email',
            field=models.EmailField(max_length=300, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='info',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='info',
            name='place',
            field=models.CharField(max_length=50, verbose_name='Place'),
        ),
    ]