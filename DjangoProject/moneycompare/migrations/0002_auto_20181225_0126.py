# Generated by Django 2.1.4 on 2018-12-25 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moneycompare', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endpoint',
            name='id',
        ),
        migrations.RemoveField(
            model_name='quoteparameter',
            name='id',
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='vendor_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='moneycompare.Vendor'),
        ),
        migrations.AlterField(
            model_name='quoteparameter',
            name='vendor_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='moneycompare.Vendor'),
        ),
    ]
