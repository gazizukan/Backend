# Generated by Django 2.2.1 on 2019-05-04 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.CharField(max_length=130)),
                ('company_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('price_for_92', models.FloatField()),
                ('price_for_95', models.FloatField()),
                ('price_for_98', models.FloatField()),
                ('price_for_dt', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_first_name', models.CharField(max_length=50)),
                ('member_second_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('mark', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.CharField(max_length=130)),
                ('address', models.CharField(max_length=200)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('has_market', models.BooleanField()),
                ('has_atm', models.BooleanField()),
                ('has_wc', models.BooleanField()),
                ('has_cafe', models.BooleanField()),
                ('has_carwash', models.BooleanField()),
                ('has_cto', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
