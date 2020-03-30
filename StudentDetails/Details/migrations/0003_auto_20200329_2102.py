# Generated by Django 3.0.4 on 2020-03-29 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Details', '0002_auto_20200320_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mark', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='subjects_name',
            name='english',
        ),
        migrations.RemoveField(
            model_name='subjects_name',
            name='math',
        ),
        migrations.RemoveField(
            model_name='subjects_name',
            name='science',
        ),
        migrations.RemoveField(
            model_name='subjects_name',
            name='social',
        ),
        migrations.RemoveField(
            model_name='studentdetails',
            name='Sub_mark',
        ),
        migrations.DeleteModel(
            name='English_mark',
        ),
        migrations.DeleteModel(
            name='Maths_mark',
        ),
        migrations.DeleteModel(
            name='Science_mark',
        ),
        migrations.DeleteModel(
            name='Social_mark',
        ),
        migrations.DeleteModel(
            name='Subjects_name',
        ),
        migrations.AddField(
            model_name='studentdetails',
            name='Sub_1',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Subject_one', to='Details.Sub_name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentdetails',
            name='Sub_2',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Subject_2', to='Details.Sub_name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentdetails',
            name='Sub_3',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Subject_3', to='Details.Sub_name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentdetails',
            name='Sub_4',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Subject_4', to='Details.Sub_name'),
            preserve_default=False,
        ),
    ]
