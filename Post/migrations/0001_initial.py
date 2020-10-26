# Generated by Django 3.0.6 on 2020-05-08 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Gallery')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='kadhai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kadhai_title', models.CharField(max_length=100)),
                ('kadhai_content', models.TextField(max_length=8000)),
                ('image', models.ImageField(upload_to='Pictures')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='katturai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('katturai_title', models.CharField(max_length=100)),
                ('katturai_content', models.TextField(max_length=3000)),
                ('image', models.ImageField(upload_to='pictures')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='kavithai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kavithai_title', models.CharField(max_length=100)),
                ('kavithai_content', models.TextField(max_length=2000)),
                ('image', models.ImageField(upload_to='Pictures')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]