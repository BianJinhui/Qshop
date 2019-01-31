# Generated by Django 2.1.5 on 2019-01-11 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=32)),
                ('bankAddress', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=32)),
                ('idCard', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.CharField(max_length=32)),
                ('goods_name', models.CharField(max_length=32)),
                ('goods_price', models.FloatField()),
                ('goods_now_price', models.FloatField()),
                ('goods_num', models.IntegerField()),
                ('goods_description', models.TextField()),
                ('goods_content', models.TextField()),
                ('goods_show_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_adress', models.ImageField(upload_to='image')),
                ('img_label', models.CharField(max_length=32)),
                ('img_description', models.TextField()),
                ('goods', models.ForeignKey(on_delete=True, to='Seller.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('nickname', models.CharField(max_length=32)),
                ('photo', models.ImageField(upload_to='image')),
                ('phone', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('id_number', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=32)),
                ('parent_id', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='seller',
            field=models.ForeignKey(on_delete=True, to='Seller.Seller'),
        ),
        migrations.AddField(
            model_name='goods',
            name='types',
            field=models.ForeignKey(on_delete=True, to='Seller.Types'),
        ),
        migrations.AddField(
            model_name='bankcard',
            name='seller',
            field=models.ForeignKey(on_delete=True, to='Seller.Seller'),
        ),
    ]
