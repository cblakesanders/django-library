# Generated by Django 3.1.2 on 2021-01-28 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0002_book_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='users',
        ),
    ]
