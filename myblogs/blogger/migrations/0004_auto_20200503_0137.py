# Generated by Django 3.0.5 on 2020-05-02 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0003_auto_20200503_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcontent',
            name='post_img',
            field=models.ImageField(default='hello', upload_to='blogger/static/Images', verbose_name='Thumbnail'),
        ),
    ]