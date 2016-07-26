# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 18:48
from __future__ import unicode_literals

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0026_round_is_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('content', ckeditor.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LeagueDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('faq', 'FAQ')], max_length=255)),
                ('tag', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z-_]*$', 'Only alphanumeric characters, hyphens, and underscores are allowed.')])),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Document')),
            ],
        ),
        migrations.AlterField(
            model_name='league',
            name='tag',
            field=models.CharField(max_length=31, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z-_]*$', 'Only alphanumeric characters, hyphens, and underscores are allowed.')]),
        ),
        migrations.AddField(
            model_name='leaguedocument',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.League'),
        ),
        migrations.AlterUniqueTogether(
            name='leaguedocument',
            unique_together=set([('league', 'tag')]),
        ),
    ]
