# Generated by Django 4.0.4 on 2022-06-01 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quality', '0004_remove_block_image_1_remove_block_image_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='block_relation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quality.block'),
        ),
    ]