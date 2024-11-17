from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Tasks(models.Model):
    task_title = models.CharField(max_length=100)
    task_content = models.TextField()

    STATUS_CHOICES = [
        ('новая', 'Новая'),
        ('в процессе', 'В процессе'),
        ('завершена', 'Завершена'),
    ]

    task_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Новая')
    task_user = models.ForeignKey(User, verbose_name='Пользователь ', on_delete=models.CASCADE)

    def __str__(self):
        return self.task_title



"""log-UserA
pass-fghj1234"""