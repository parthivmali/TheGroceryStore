# Generated by Django 4.0.5 on 2022-06-05 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_id_category_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='product_img',
            new_name='category_img',
        ),
    ]
