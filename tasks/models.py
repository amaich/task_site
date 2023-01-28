from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import datetime


class Tasks(models.Model):
    task_name = models.CharField(max_length=100,
                                 verbose_name="Название задачи",)
    task_description = models.TextField(null=True,
                                        blank=True,
                                        verbose_name="Описание задачи",)
    task_reporter = models.ForeignKey(User,
                                      on_delete=models.CASCADE,
                                      related_name="task_reporter",
                                      verbose_name="Автор задачи",)
    task_executor = models.ForeignKey(User,
                                      on_delete=models.SET_NULL,
                                      null=True,
                                      blank=True,
                                      related_name='task_executor',
                                      verbose_name="Исполнитель задачи",)
    task_status = models.CharField(max_length=50,
                                   default='Created',
                                   verbose_name='Статус',)

    def __str__(self):
        return self.task_name