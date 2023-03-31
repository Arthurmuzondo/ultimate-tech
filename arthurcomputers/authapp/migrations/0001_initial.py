# Generated by Django 4.1.7 on 2023-03-31 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='about_images')),
                ('paragraph1', models.TextField()),
                ('paragraph2', models.TextField()),
            ],
        ),
    ]
