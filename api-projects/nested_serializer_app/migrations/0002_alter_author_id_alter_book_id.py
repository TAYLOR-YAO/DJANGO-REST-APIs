# Generated by Django 4.0 on 2021-12-24 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nested_serializer_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]