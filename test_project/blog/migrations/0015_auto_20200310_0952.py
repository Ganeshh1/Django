# Generated by Django 3.0.3 on 2020-03-10 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_student_mark_obtained'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Mark_Obtained',
            field=models.IntegerField(),
        ),
    ]
