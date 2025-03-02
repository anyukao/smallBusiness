# Generated by Django 4.1.6 on 2023-05-24 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onoxo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.IntegerField(null=True, verbose_name='sum')),
                ('dateOfPayment', models.DateField(blank=True, null=True, verbose_name='data of payment')),
                ('percentOfCredit', models.FloatField(blank=True, null=True, verbose_name='percent')),
                ('term', models.FloatField(null=True, verbose_name='term')),
                ('penalties', models.FloatField(blank=True, null=True, verbose_name='percent')),
            ],
        ),
        migrations.CreateModel(
            name='CreditForEveryMonth_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SumForMonth', models.FloatField(null=True, verbose_name='sum for month')),
                ('SumWithPercent', models.FloatField(null=True, verbose_name='amount of month')),
                ('SumRemains', models.FloatField(null=True, verbose_name='Remains of month')),
                ('percent', models.FloatField(null=True, verbose_name='percent')),
                ('penalties', models.FloatField(null=True, verbose_name='percent')),
                ('dateOfPayment', models.DateField(blank=True, null=True, verbose_name='data of payment')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name='Status')),
                ('credit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit', to='onoxo.credit_model', verbose_name='Credit')),
            ],
            options={
                'ordering': ['dateOfPayment'],
            },
        ),
    ]
