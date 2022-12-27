# Generated by Django 4.1.4 on 2022-12-26 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cartype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_reserve', models.BooleanField(default=False)),
                ('saled', models.BooleanField(default=False)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.bus')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.bus')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.seat')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bus',
            name='cartype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.cartype'),
        ),
    ]