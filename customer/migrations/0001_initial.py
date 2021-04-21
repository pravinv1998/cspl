# Generated by Django 3.0.6 on 2020-05-30 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('addr', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, default='', max_length=254, null=True)),
                ('export_to_csv', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone_status', models.CharField(blank=True, choices=[('Green Zone', 'GREEN ZONE'), ('OrangeZone', 'ORANGE ZONE'), ('Red Zone', 'RED ZONE'), ('Containment Zone', 'CONTAINMENT ZONE')], max_length=100, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('narration', models.CharField(max_length=1000)),
                ('along_with', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
    ]
