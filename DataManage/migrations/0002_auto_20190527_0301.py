# Generated by Django 2.2.1 on 2019-05-26 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataManage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yueke',
            name='id',
        ),
        migrations.AlterField(
            model_name='yueke',
            name='orderNum',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='订单号'),
        ),
    ]