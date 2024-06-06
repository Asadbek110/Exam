# Generated by Django 5.0.6 on 2024-06-06 12:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('billing_address', models.TextField()),
                ('phone', models.CharField(max_length=14)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='attribute',
            field=models.ManyToManyField(blank=True, null=True, related_name='attributes', to='blog.attribute'),
        ),
        migrations.DeleteModel(
            name='ProductAttribute',
        ),
    ]