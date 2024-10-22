# Generated by Django 4.2.2 on 2023-07-01 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("evaluation", "0006_answer"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="is_selected",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="response",
            name="answer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="response_answer",
                to="evaluation.answer",
            ),
        ),
        migrations.AlterField(
            model_name="response",
            name="evaluation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="response_evaluation",
                to="evaluation.evaluation",
            ),
        ),
        migrations.AlterField(
            model_name="response",
            name="participant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="response_participant",
                to="evaluation.participant",
            ),
        ),
        migrations.AlterField(
            model_name="response",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="response_question",
                to="evaluation.question",
            ),
        ),
    ]
