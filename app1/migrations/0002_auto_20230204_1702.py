# Generated by Django 3.2.5 on 2023-02-04 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pid',
        ),
        migrations.AddField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
