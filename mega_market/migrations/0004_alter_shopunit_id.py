# Generated by Django 4.0.6 on 2022-07-31 13:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mega_market', '0003_alter_shopunit_parentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopunit',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
