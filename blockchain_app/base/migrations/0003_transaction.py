# Generated by Django 4.1.7 on 2023-04-03 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_users_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tranasction_id', models.CharField(max_length=100)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.member')),
            ],
        ),
    ]
