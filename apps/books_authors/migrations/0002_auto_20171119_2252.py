# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books_authors',
            name='author',
        ),
        migrations.RemoveField(
            model_name='books_authors',
            name='book',
        ),
        migrations.AddField(
            model_name='authors',
            name='book',
            field=models.ManyToManyField(related_name='authors', to='books_authors.Books'),
        ),
        migrations.DeleteModel(
            name='Books_Authors',
        ),
    ]