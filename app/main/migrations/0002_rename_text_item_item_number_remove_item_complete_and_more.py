# Generated by Django 4.0 on 2022-05-19 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='text',
            new_name='item_number',
        ),
        migrations.RemoveField(
            model_name='item',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='item',
            name='todolist',
        ),
        migrations.AddField(
            model_name='item',
            name='item_name',
            field=models.CharField(default='item', max_length=200),
        ),
        migrations.DeleteModel(
            name='ToDoList',
        ),
    ]
