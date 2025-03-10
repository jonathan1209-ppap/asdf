# Generated by Django 2.2.7 on 2019-11-10 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0096_profile_language_set_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestparticipation',
            name='is_disqualified',
            field=models.BooleanField(default=False, help_text='Whether this participation is disqualified.', verbose_name='is disqualified'),
        ),
        migrations.AlterField(
            model_name='contestparticipation',
            name='virtual',
            field=models.IntegerField(default=0, help_text='0 means non-virtual, otherwise the n-th virtual participation.', verbose_name='virtual participation id'),
        ),
    ]
