# Generated by Django 3.2.3 on 2021-05-30 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='text',
            field=models.ImageField(upload_to=''),
        ),
    ]