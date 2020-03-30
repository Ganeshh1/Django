# Generated by Django 3.0.3 on 2020-03-04 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post17'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('std', models.TextField()),
                ('college_name', models.CharField(max_length=100)),
                ('reg_no', models.BigIntegerField()),
                ('Mark_Obtained', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='post11',
            old_name='age',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='post14',
            old_name='age',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='post2',
            old_name='age',
            new_name='URL',
        ),
    ]