# Generated by Django 2.2.4 on 2019-08-05 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20190805_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='itemSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=15)),
                ('pct_of_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping_type', models.CharField(max_length=10)),
                ('topping', models.CharField(max_length=50)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='price',
            new_name='base_price',
        ),
        migrations.AlterField(
            model_name='menu',
            name='size',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.itemSize'),
        ),
    ]
