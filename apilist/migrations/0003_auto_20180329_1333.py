# Generated by Django 2.0.2 on 2018-03-29 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apilist', '0002_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='MhlEnquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('query', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]