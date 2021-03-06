# Generated by Django 3.1.6 on 2021-06-08 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0006_auto_20210608_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='technologies',
            field=models.ManyToManyField(to='startScan.Ip'),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='ip_addresses',
            field=models.ManyToManyField(related_name='ip', to='startScan.Ip'),
        ),
    ]
