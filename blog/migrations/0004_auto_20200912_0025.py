# Generated by Django 3.1 on 2020-09-11 23:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20200912_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='likes',
            field=models.ManyToManyField(default='', editable=False, related_name='blog_entry', to=settings.AUTH_USER_MODEL),
        ),
    ]
