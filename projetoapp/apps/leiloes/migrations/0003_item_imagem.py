# Generated by Django 5.2 on 2025-06-17 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leiloes', '0002_item_lance_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='itens/'),
        ),
    ]
