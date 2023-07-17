# Generated by Django 4.2.3 on 2023-07-17 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('event_date', models.DateField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event_date', models.DateField(null=True)),
                ('mode', models.CharField(choices=[('1X1', '1X1'), ('2X2', '2X2'), ('3X3', '3X3')], max_length=3)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='competitions.competition')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='competitions.competition')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('abbreviation', models.CharField(blank=True, max_length=3)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='competitions.competition')),
                ('player', models.ManyToManyField(to='competitions.player')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.CharField(choices=[('Free thrown', 'Free thrown'), ('1-point', 'One point shot'), ('2-point', 'Two points shot'), ('Personal foul', 'Personal foul'), ('Technical foul', 'Personal foul'), ('Shot foul', 'Shot foul'), ('Win', 'Win'), ('Tie', 'Tie')], max_length=20)),
                ('event_time', models.DateTimeField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='competitions.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='competitions.player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='competitions.team')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='game',
            name='team_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_a', to='competitions.team'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_b', to='competitions.team'),
        ),
    ]
