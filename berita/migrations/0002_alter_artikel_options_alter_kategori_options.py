# Generated by Django 5.1.6 on 2025-03-15 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artikel',
            options={'verbose_name_plural': '2. Artikel'},
        ),
        migrations.AlterModelOptions(
            name='kategori',
            options={'verbose_name_plural': '1. Kategori'},
        ),
    ]
