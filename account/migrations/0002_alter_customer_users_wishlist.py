# Generated by Django 5.0.3 on 2024-05-19 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('product', '0004_brand_category_remove_product_category_product_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='users_wishlist',
            field=models.ManyToManyField(blank=True, through='account.Wishlist', to='product.product'),
        ),
    ]
