# Generated by Django 4.1.5 on 2023-01-19 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_remove_courselevel_course_courselevel_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='sale_name',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
    ]
