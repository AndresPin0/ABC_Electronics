# Generated by Django 4.1.13 on 2023-11-19 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('electronics', '0003_delete_test_delete_test2'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('date_of_birth', models.DateTimeField()),
                ('email', models.EmailField(max_length=100)),
                ('home_phone', models.CharField(max_length=10)),
                ('cell_phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_number', models.IntegerField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField()),
                ('shipped_date', models.DateTimeField()),
                ('payment_date', models.DateTimeField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronics.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('quantity_available', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronics.categoryproduct')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronics.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronics.product')),
            ],
            options={
                'unique_together': {('order_number', 'product_id')},
            },
        ),
    ]