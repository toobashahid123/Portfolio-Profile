# Generated by Django 4.2.2 on 2023-11-09 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_product_images_delete_productimage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='images',
            new_name='image',
        ),
    ]
