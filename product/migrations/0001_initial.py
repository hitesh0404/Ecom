# Generated by Django 5.0.3 on 2024-03-30 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('size', models.DecimalField(decimal_places=2, max_digits=4)),
                ('description', models.CharField(max_length=500)),
                ('color', models.CharField(max_length=20)),
                ('category', models.CharField(choices=[('ELECTRONICS', 'Electronics'), ('CLOTHING', 'Clothing'), ('BOOKS', 'Books'), ('HOME_APPLIANCES', 'Home Appliances'), ('BEAUTY', 'Beauty'), ('SPORTS_AND_OUTDOORS', 'Sports & Outdoors'), ('TOYS_AND_GAMES', 'Toys & Games'), ('FOOD_AND_GROCERY', 'Food & Grocery'), ('OTHER', 'Other')], max_length=40)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
    ]
