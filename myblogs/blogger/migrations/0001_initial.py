# Generated by Django 3.0.5 on 2020-05-02 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('post_title', models.CharField(default='Blog post', max_length=200, primary_key=True, serialize=False, verbose_name='Title')),
                ('post_desc', models.TextField(max_length=100, verbose_name='Description')),
                ('post_text', models.TextField(verbose_name='Story')),
                ('post_date', models.DateField(verbose_name='Date published')),
                ('post_img', models.ImageField(null=True, upload_to='', verbose_name='Thumbnail')),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment_user', models.CharField(max_length=200)),
                ('Comment_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('Comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogger.Question')),
            ],
        ),
    ]
