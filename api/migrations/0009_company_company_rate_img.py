# Generated by Django 2.2.1 on 2019-05-16 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190512_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_rate_img',
            field=models.CharField(default='https://ibb.co/G2LHm2P', max_length=400),
        ),
    ]
