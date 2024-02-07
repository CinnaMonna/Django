from django.contrib import admin
from . models import Client, Product, Order


"""Добавление новых действий над группой выбранных объектов"""
@admin.action(description="Очистить сведения о номере телефона")
def reset_phone(modeladmin, request, queryset):
    queryset.update(phone='Телефон не указан')

@admin.action(description="Очистить описание продукта")
def reset_description(modeladmin, request, queryset):
    queryset.update(description='Описание не добавлено')

class ClientAdmin(admin.ModelAdmin):
    """Для страниц вывода списка записей"""
    list_display = ['name', 'phone', 'email', 'register_date']
    ordering = ['-register_date']
    list_filter = ['register_date']
    search_fields = ['name']
    search_help_text = 'Поиск по полю name'

    """Для страницы вывода отдельной записи"""
    readonly_fields = ['register_date']
    fieldsets = [     
        (
            'Заказчик',
            {
                'classes': ['wide'],      
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],   
                'description': 'Контакты',
                'fields': ['phone', 'email', 'adress'],
            },
        ),
        (
            None,
            {
                'description': 'Дата регистрации устанавливается автоматически',
                'fields': ['register_date']
            },
        ),
    ]
    actions = [reset_phone]

class ProductAdmin(admin.ModelAdmin):
    """Для страниц вывода списка записей"""
    list_display = ['title', 'description', 'price', 'add_date']
    ordering = ['-add_date']
    list_filter = ['title']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание'

    """Для страницы вывода отдельной записи"""
    readonly_fields = ['add_date']
    fieldsets = [     
        (
            'Товар, цена',
            {
                'classes': ['wide'],      
                'fields': ['title', 'price'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],   
                'description': 'Описание',
                'fields': ['description', 'image'],
            },
        ),
        (
            None,
            {
                'description': 'Дата регистрации добавления автоматически',
                'fields': ['add_date']
            },
        ),
    ]

    actions = [reset_description]

class OrderAdmin(admin.ModelAdmin):
    """Для страниц вывода списка записей"""
    list_display = ['pk', 'client', 'summary_cost', 'order_date']
    ordering = ['order_date']
    list_filter = ['client']
    search_fields = ['client']
    search_help_text = 'Поиск по полю Заказчик'

    """Для страницы вывода отдельной записи"""
    fields = ['client', 'products', 'summary_cost', 'order_date']
    readonly_fields = ['order_date']


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)