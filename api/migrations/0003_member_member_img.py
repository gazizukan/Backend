# Generated by Django 2.2.1 on 2019-05-11 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_company_company_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='member_img',
            field=models.CharField(default='https://ibb.co/G2LHm2P', max_length=200),
        ),
    ]