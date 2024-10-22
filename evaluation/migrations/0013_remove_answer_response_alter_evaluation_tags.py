# Generated by Django 4.2.2 on 2023-07-01 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("evaluation", "0012_alter_participant_evaluation"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="answer",
            name="response",
        ),
        migrations.AlterField(
            model_name="evaluation",
            name="tags",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="evaluations", to="evaluation.tag"
            ),
        ),
    ]
