from django.contrib import admin
from . models import Coin, Author, Post 


"""Добавление новых действий над группой выбранных объектов"""
@admin.action(description="Очистить сведения о биографии")
def reset_bio(modeladmin, request, queryset):
    queryset.update(bio='Сведения о биографии не заполнены')


class AuthorAdmin(admin.ModelAdmin):
    """Для страниц вывода списка записей"""
    list_display = ['name', 'last_name', 'email', 'birthday']
    ordering = ['last_name', '-name']
    list_filter = ['birthday', 'name']
    search_fields = ['bio']
    search_help_text = 'Поиск по полю bio'

    """Для страницы вывода отдельной записи"""
    # fields =
    readonly_fields = ['birthday']
    fieldsets = [     #определяем группы полей
        (
            None,    #без заголовка
            {
                'classes': ['wide'],       #макс. широкое поле на панели
                'fields': ['name', 'last_name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],    #свернуто, развернуть по клику
                'description': 'Дата рождения, биография автора',
                'fields': ['birthday', 'bio'],
            },
        ),
        (
            'Контакты',
            {
                'description': 'Автор предоставляет обратную связь',
                'fields': ['email'],
            }
        ),
    ]
    actions = [reset_bio]


class PostAdmin(admin.ModelAdmin):
    """Для страниц вывода списка записей"""
    list_display = ['title', 'author', 'publish_date', 'views']
    ordering = ['-views']
    list_filter = ['publish_date', 'author']
    search_fields = ['title']
    search_help_text = 'Поиск по полю title'
    
    """Для страницы вывода отдельной записи"""
    fields = ['title', 'author', 'publish_date', 'views']
    readonly_fields = ['publish_date', 'views']


admin.site.register(Coin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)