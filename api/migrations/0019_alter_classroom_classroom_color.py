# Generated by Django 3.2.6 on 2021-08-29 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_classroom_classroom_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='classroom_color',
            field=models.CharField(default='blue', max_length=255),
        ),
    ]
