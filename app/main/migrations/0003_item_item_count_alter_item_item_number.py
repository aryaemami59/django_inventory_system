# Generated by Django 4.0 on 2022-05-19 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_text_item_item_number_remove_item_complete_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_count',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_number',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
