# Generated by Django 4.2.7 on 2023-11-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_delete_profilebio_product_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='resume',
        ),
    ]
