# Generated by Django 3.2.5 on 2021-08-02 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0007_clientinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinfo',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='client_images/'),
        ),
    ]