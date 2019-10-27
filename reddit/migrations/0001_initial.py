# Generated by Django 2.1.7 on 2019-03-01 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subreddit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subreddit', models.CharField(max_length=100)),
                ('submission_type', models.CharField(choices=[('track', 'track'), ('album', 'album'), ('playlist', 'playlist')], max_length=100)),
                ('spotify_id', models.CharField(max_length=100)),
            ],
        ),
    ]
