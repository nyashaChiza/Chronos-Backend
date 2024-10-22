# Generated by Django 4.2.2 on 2023-07-01 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("evaluation", "0010_alter_answer_question"),
    ]

    operations = [
        migrations.AddField(
            model_name="participant",
            name="evaluation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="evaluation",
                to="evaluation.evaluation",
            ),
        ),
    ]
