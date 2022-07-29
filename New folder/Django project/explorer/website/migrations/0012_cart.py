# Generated by Django 3.0.5 on 2020-10-17 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20201011_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('cust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.customer')),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.product')),
            ],
        ),
    ]