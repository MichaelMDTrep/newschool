# Generated by Django 4.1.10 on 2023-09-05 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("curriculum", "0004_course_coursecompleted_courselink_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="curriculum.coursecategory",
            ),
        ),
    ]