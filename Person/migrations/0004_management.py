# Generated by Django 3.1.4 on 2020-12-24 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0003_delete_management'),
    ]

    operations = [
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]