# Generated by Django 2.1.1 on 2018-11-20 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0011_auto_20181120_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='detail',
            field=models.TextField(),
        ),
    ]
