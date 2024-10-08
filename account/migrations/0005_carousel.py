# Generated by Django 5.0.6 on 2024-06-23 04:47

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_supplier_document_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='online-shopping-background-website-mobile-app_269039-166.jpg', upload_to='carousel/')),
                ('title', django_ckeditor_5.fields.CKEditor5Field()),
                ('description', django_ckeditor_5.fields.CKEditor5Field()),
            ],
        ),
    ]
