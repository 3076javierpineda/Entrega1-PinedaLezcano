# Generated by Django 4.1.2 on 2022-12-20 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='informacion',
            field=models.CharField(default=True, max_length=30),
            preserve_default=False,
        ),
    ]
