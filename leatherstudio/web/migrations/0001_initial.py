# Generated by Django 4.0.6 on 2022-07-16 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('availability', models.BooleanField(default=True)),
                ('img', models.ImageField(default='no_image.jpg', upload_to='product_image')),
            ],
        ),
    ]
