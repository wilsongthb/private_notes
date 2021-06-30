# Generated by Django 3.2.4 on 2021-06-28 16:46

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion del registro')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Fecha de modificacion')),
                ('deleted_at', models.DateTimeField(editable=False, help_text='Fecha de eliminacion, nulo en caso aun no esta eliminado', null=True)),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('dni', models.CharField(max_length=8, null=True)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion del registro')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Fecha de modificacion')),
                ('deleted_at', models.DateTimeField(editable=False, help_text='Fecha de eliminacion, nulo en caso aun no esta eliminado', null=True)),
                ('text', models.TextField(max_length=750)),
                ('amount', models.DecimalField(decimal_places=2, default=0, help_text='Monto a pagar', max_digits=10)),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0, help_text='Monto pagado', max_digits=10)),
                ('init_at', models.DateTimeField(default=datetime.datetime.now, help_text='Fecha y hora de inicio programado')),
                ('ends_at', models.DateTimeField(help_text='Fecha y hora de finalizacion programada', null=True)),
                ('done_at', models.DateTimeField(help_text='Tiempo en donde se marca como finalizado', null=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Nota'), (2, 'Actividad'), (3, 'Recordatorio')], default=1, help_text='Tipo de nota')),
                ('patern_note_id', models.PositiveBigIntegerField(help_text='Nota origen', null=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='notes.contact')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion del registro')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Fecha de modificacion')),
                ('deleted_at', models.DateTimeField(editable=False, help_text='Fecha de eliminacion, nulo en caso aun no esta eliminado', null=True)),
                ('slug', models.CharField(help_text='Nombre en clave', max_length=15, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')])),
                ('name', models.CharField(help_text='Nombre decriptivo', max_length=255)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProgramActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion del registro')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Fecha de modificacion')),
                ('deleted_at', models.DateTimeField(editable=False, help_text='Fecha de eliminacion, nulo en caso aun no esta eliminado', null=True)),
                ('activity', models.CharField(max_length=255, null=True)),
                ('days', models.IntegerField(null=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='notes.program')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion del registro')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Fecha de modificacion')),
                ('deleted_at', models.DateTimeField(editable=False, help_text='Fecha de eliminacion, nulo en caso aun no esta eliminado', null=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('description', models.CharField(max_length=255, null=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='notes.contact')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='notes.note')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='note',
            name='program',
            field=models.ForeignKey(default=None, help_text='El programa del cual se programa las actividades como notas futuras', null=True, on_delete=django.db.models.deletion.PROTECT, to='notes.program'),
        ),
    ]
