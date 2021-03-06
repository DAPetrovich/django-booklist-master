# Generated by Django 3.0.6 on 2020-05-27 19:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Время создания записи"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Время обновления записи"
                    ),
                ),
                ("lastname", models.CharField(max_length=50, verbose_name="Фамилия")),
                ("firstname", models.CharField(max_length=50, verbose_name="Имя")),
                (
                    "patronymic",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=50,
                        null=True,
                        verbose_name="Отчество",
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(
                        blank=True,
                        default=None,
                        null=True,
                        verbose_name="Дата рождения",
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=50,
                        null=True,
                        verbose_name="Email",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=30,
                        null=True,
                        verbose_name="Телефон",
                    ),
                ),
            ],
            options={"verbose_name": "Автор", "verbose_name_plural": "Авторы",},
        ),
        migrations.CreateModel(
            name="PublishingHouse",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания записи"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Время обновления записи"
                    ),
                ),
                ("title", models.CharField(max_length=50, verbose_name="Наименование")),
                ("address", models.CharField(max_length=50, verbose_name="Адрес")),
                (
                    "email",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=50,
                        null=True,
                        verbose_name="Email",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=30,
                        null=True,
                        verbose_name="Телефон",
                    ),
                ),
            ],
            options={
                "verbose_name": "Издательство",
                "verbose_name_plural": "Издательства",
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания записи"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Время обновления записи"
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_index=True, max_length=255, verbose_name="Название"
                    ),
                ),
                (
                    "publishing_year",
                    models.SmallIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(3000),
                            django.core.validators.MinValueValidator(1),
                        ],
                        verbose_name="Год издания",
                    ),
                ),
                (
                    "isbn",
                    models.CharField(
                        help_text='<a href="https://www.isbn-international.org/content/what-isbn" target="_blank">ISBN номер</a>',
                        max_length=13,
                        unique=True,
                        verbose_name="ISBN",
                    ),
                ),
                (
                    "authors",
                    models.ManyToManyField(
                        related_name="author_books",
                        to="booklist.Author",
                        verbose_name="Авторы",
                    ),
                ),
                (
                    "publishing_house",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="publishing_house_book",
                        to="booklist.PublishingHouse",
                        verbose_name="Издательство",
                    ),
                ),
            ],
            options={"verbose_name": "Книга", "verbose_name_plural": "Книги",},
        ),
    ]
