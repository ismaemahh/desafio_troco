# Generated by Django 3.0.4 on 2020-03-13 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('troco', '0002_auto_20200312_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moeda',
            name='moeda_1',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='moeda',
            name='moeda_10',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='moeda',
            name='moeda_5',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='moeda',
            name='moeda_50',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='nota',
            name='nota_1',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='nota',
            name='nota_10',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='nota',
            name='nota_100',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='nota',
            name='nota_5',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='nota',
            name='nota_50',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
