# Generated by Django 4.2.4 on 2023-08-23 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_chathistory_chat_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chathistory',
            name='chat_answer',
            field=models.TextField(auto_created=True),
        ),
    ]