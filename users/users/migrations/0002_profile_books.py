# Generated by Django 3.1.2 on 2021-01-28 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0003_remove_book_users'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='books',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booklist.book'),
        ),
    ]
