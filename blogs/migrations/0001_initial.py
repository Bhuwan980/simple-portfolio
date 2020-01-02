# Generated by Django 3.0.1 on 2020-01-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=900)),
                ('image', models.ImageField(upload_to='images/')),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField(max_length=200)),
            ],
        ),
    ]
