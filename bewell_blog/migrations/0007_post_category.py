# Generated by Django 4.2.11 on 2024-03-28 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bewell_blog', '0006_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.PROTECT, to='bewell_blog.category'),
        ),
    ]
