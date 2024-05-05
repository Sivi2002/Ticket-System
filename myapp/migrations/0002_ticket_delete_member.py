# Generated by Django 5.0 on 2024-03-16 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default=None, max_length=255)),
                ('discription', models.CharField(default=None, max_length=2000)),
            ],
        ),
        migrations.DeleteModel(
            name='member',
        ),
    ]