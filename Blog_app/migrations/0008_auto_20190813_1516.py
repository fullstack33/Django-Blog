# Generated by Django 2.2.3 on 2019-08-13 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0007_auto_20190813_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='/static/images/user.png', upload_to='profile'),
        ),
    ]