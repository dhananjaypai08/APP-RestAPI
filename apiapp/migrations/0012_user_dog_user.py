# Generated by Django 4.0.5 on 2022-12-07 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0011_alter_dog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='dog',
            name='user',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='apiapp.user'),
        ),
    ]
