# Generated by Django 4.2.7 on 2023-11-28 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_remove_profilebio_bio_pic_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_image',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='product_image',
        ),
    ]