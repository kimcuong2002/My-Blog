# Generated by Django 4.1.6 on 2023-05-01 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact_alter_post_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.TextField(),
        ),
    ]