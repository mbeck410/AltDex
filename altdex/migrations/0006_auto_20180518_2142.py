# Generated by Django 2.0.5 on 2018-05-19 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('altdex', '0005_indexprice_change_24h'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='change_24h',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coin',
            name='market_cap',
            field=models.DecimalField(decimal_places=25, default=0, max_digits=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coin',
            name='percent_weight',
            field=models.DecimalField(decimal_places=25, default=0, max_digits=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coin',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coin',
            name='price_percent_change',
            field=models.DecimalField(decimal_places=25, default=0, max_digits=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coin',
            name='volume',
            field=models.DecimalField(decimal_places=25, default=0, max_digits=50),
            preserve_default=False,
        ),
    ]
