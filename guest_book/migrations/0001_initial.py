# Generated by Django 4.2.2 on 2023-07-02 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Name')),
                ('email_author', models.EmailField(max_length=254, verbose_name='Email')),
                ('entry_text', models.TextField(max_length=5000, verbose_name='Entry text')),
                ('time_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Time of creations')),
                ('edit_time', models.DateTimeField(auto_now=True, verbose_name='Edit time')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=10, verbose_name='Status')),
            ],
        ),
    ]
