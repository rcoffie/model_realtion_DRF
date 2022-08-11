# Generated by Django 4.1 on 2022-08-11 21:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_category_post_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['created']},
        ),
        migrations.AddField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]