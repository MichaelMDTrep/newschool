# Generated by Django 4.1.10 on 2023-09-05 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0002_coursecompletedmodel_courselinkmodel_coursemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecompletedmodel',
            name='CourseModel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='curriculum.coursemodel'),
        ),
    ]