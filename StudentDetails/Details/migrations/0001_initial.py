# Generated by Django 3.0.4 on 2020-03-20 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='English_mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Maths_mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100)),
                ('school_no', models.IntegerField()),
                ('school_location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Science_mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Social_mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subjects_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Details.English_mark')),
                ('math', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Details.Maths_mark')),
                ('science', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Details.Social_mark')),
                ('social', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Details.Science_mark')),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('reg_no', models.BigIntegerField()),
                ('phone_no', models.IntegerField()),
                ('Sub_mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Details.Subjects_name')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Details.School')),
            ],
        ),
    ]
