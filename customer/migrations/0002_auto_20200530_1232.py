# Generated by Django 3.0.6 on 2020-05-30 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visits',
            name='zone_status',
            field=models.CharField(blank=True, choices=[('Red Zone', 'RED ZONE'), ('OrangeZone', 'ORANGE ZONE'), ('Containment Zone', 'CONTAINMENT ZONE'), ('Green Zone', 'GREEN ZONE')], max_length=100, null=True),
        ),
    ]