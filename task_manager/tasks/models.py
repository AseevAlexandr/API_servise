from django.db import models


class Tasks(models.Model):
    task_title = models.CharField(max_length=100)
    task_content = models.TextField()

    STATUS_CHOICES = [
        ('новая', 'Новая'),
        ('в процессе', 'В процессе'),
        ('завершена', 'Завершена'),
    ]

    task_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Новая')
    # task_user =

    def __str__(self):
        return self.task_title


# 0. Модели данных:
#    - Пользователь:
#      - ID (целое число, автоинкремент)
#      - Имя (строка)
#      - Электронная почта (строка)
#      - Пароль (строка)
#    - Задача:
#      - ID (целое число, автоинкремент)
#      - Название (строка)
#      - Описание (строка)
#      - Статус (строка, возможные значения: "новая", "в процессе", "завершена")
#      - Пользователь_ID (внешний ключ на модель Пользователь)