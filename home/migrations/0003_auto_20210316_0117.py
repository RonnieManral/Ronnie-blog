# Generated by Django 3.1.7 on 2021-03-15 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210316_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='state',
            field=models.CharField(max_length=122),
        ),
        migrations.AlterField(
            model_name='contact',
            name='zip',
            field=models.CharField(max_length=122),
        ),
    ]
