# Generated by Django 3.2.5 on 2021-08-02 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0008_alter_clientinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinfo',
            name='client_mode',
            field=models.CharField(choices=[('FULLTIME', 'Fulltime'), ('PARTTIME', 'Parttime'), ('OUTSOURCING', 'Outsourcing')], max_length=100),
        ),
    ]
