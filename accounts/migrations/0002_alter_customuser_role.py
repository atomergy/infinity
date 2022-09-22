# Generated by Django 4.1.1 on 2022-09-21 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('1', 'CEO'), ('2', 'Admin'), ('3', 'Seller'), ('4', 'The User')], default='4', max_length=1, verbose_name='Role'),
        ),
    ]
