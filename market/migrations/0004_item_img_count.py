# Generated by Django 3.2.3 on 2021-06-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20210614_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='img_count',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True),
        ),
    ]