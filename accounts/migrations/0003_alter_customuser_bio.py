# Generated by Django 4.1.1 on 2022-09-22 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='Bio'),
        ),
    ]