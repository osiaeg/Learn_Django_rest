# Generated by Django 4.0.6 on 2022-08-07 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mega_market', '0012_rename_parentid_shopunit_parentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopunit',
            name='date',
            field=models.DateField(),
        ),
    ]
