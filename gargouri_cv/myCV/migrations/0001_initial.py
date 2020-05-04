# Generated by Django 3.0.5 on 2020-05-03 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='diplomaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameDiploma', models.CharField(blank=True, max_length=120, null=True)),
                ('yearDiploma', models.CharField(blank=True, max_length=120, null=True)),
                ('InstituteDiploma', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('periodeStart', models.CharField(blank=True, max_length=120, null=True)),
                ('periodeEnd', models.CharField(blank=True, max_length=120, null=True)),
                ('info', models.TextField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='hobbiesInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbyInfo', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='languageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=120, null=True)),
                ('languageDetails', models.CharField(blank=True, max_length=120, null=True)),
                ('percentage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='personnalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=120)),
                ('lastName', models.CharField(max_length=120)),
                ('age', models.DecimalField(decimal_places=0, max_digits=3)),
                ('email', models.EmailField(max_length=254)),
                ('littleImage', models.CharField(blank=True, max_length=120, null=True)),
                ('bigImage', models.CharField(blank=True, max_length=120, null=True)),
                ('summary', models.TextField(blank=True, max_length=200, null=True)),
                ('Address', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='phoneInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillInfo', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]