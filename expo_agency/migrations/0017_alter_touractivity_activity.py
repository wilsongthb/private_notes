# Generated by Django 3.2.4 on 2021-07-31 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expo_agency', '0016_alter_touractivity_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touractivity',
            name='activity',
            field=models.TextField(max_length=500),
        ),
    ]
