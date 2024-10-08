# Generated by Django 5.0.7 on 2024-07-30 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('Image_url', models.ImageField(upload_to='coures_thumbnails/')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('intructor_name', models.CharField(max_length=200)),
                ('course_tags', models.CharField(help_text='value is seperated by commas', max_length=200)),
            ],
        ),
    ]
