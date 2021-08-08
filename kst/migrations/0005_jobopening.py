# Generated by Django 3.2.6 on 2021-08-06 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kst', '0004_career'),
    ]

    operations = [
        migrations.CreateModel(
            name='jobopening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=500)),
                ('phone', models.CharField(max_length=500)),
                ('position', models.CharField(max_length=500)),
                ('date', models.DateTimeField(max_length=500)),
                ('status', models.TextField(max_length=500)),
                ('resume', models.FileField(max_length=500, upload_to='')),
            ],
        ),
    ]
