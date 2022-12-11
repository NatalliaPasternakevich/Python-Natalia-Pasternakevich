# Generated by Django 4.1.2 on 2022-12-08 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_card', '0002_alter_book_price'),
        ('basket', '0003_alter_goodsinbasket_book_alter_goodsinbasket_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('in_process', 'In Process'), ('done', 'Processed and delivered')], default='created', max_length=50, verbose_name='Stasuses'),
        ),
        migrations.AlterField(
            model_name='goodsinbasket',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product_card.book', verbose_name='Book in basket'),
        ),
    ]