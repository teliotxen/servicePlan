# Generated by Django 4.0.4 on 2022-05-23 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('block_relation', models.ManyToManyField(to='quality.block')),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quality.projects')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('status', models.BooleanField(default=None, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('block_relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quality.block')),
                ('relation', models.ManyToManyField(to='quality.comments')),
                ('scenario_relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quality.scenario')),
            ],
        ),
    ]
