# Generated by Django 4.1.8 on 2023-04-25 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]