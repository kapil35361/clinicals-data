# Generated by Django 4.0.3 on 2022-11-26 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicalapp', '0002_alter_clinicaldata_componentvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinicaldata',
            name='componentValue',
            field=models.CharField(max_length=20),
        ),
    ]