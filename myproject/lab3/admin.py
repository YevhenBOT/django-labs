from django.contrib import admin
from .models import Genre, Game, Platform


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # Відображаємо назву, жанр та дати (вимога лаби)
    list_display = ('title', 'genre', 'created_at', 'updated_at')
    # Додаємо фільтр справа, щоб було зручніше
    list_filter = ('created_at', 'genre')
    # Пошук за назвою гри
    search_fields = ('title',)


# Реєструємо інші таблиці просто
admin.site.register(Genre)
admin.site.register(Platform)
from django.contrib import admin

# Register your models here.
