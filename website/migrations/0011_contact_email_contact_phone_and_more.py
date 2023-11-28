# Generated by Django 4.2.7 on 2023-11-14 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
    ]
