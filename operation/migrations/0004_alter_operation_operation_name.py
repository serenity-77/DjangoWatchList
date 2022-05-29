# Generated by Django 3.2.13 on 2022-05-30 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_alter_operationdetail_operation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='operation_name',
            field=models.CharField(choices=[('add', 'Read'), ('edit', 'Edit'), ('delete', 'Delete'), ('read', 'Read')], default='add', max_length=6, unique=True),
        ),
    ]
