# Generated by Django 4.1.7 on 2023-02-21 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='user',
        ),
        migrations.DeleteModel(
            name='Bio',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
    ]
