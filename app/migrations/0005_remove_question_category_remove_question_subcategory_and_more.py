# Generated by Django 4.0 on 2022-01-15 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_subcategory_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='category',
        ),
        migrations.RemoveField(
            model_name='question',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]
