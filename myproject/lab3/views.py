from django.shortcuts import render


def main_page(request):
    # Список твоїх улюблених ігор
    games = ['The Witcher 3', 'Minecraft', 'Cyberpunk 2077', 'GTA V']
    return render(request, 'lab3/index.html', {'games': games})


def sub_page(request, page_name):
    context = {
        'game_title': page_name,
        'description': f"Опис гри {page_name}: Це одна з моїх найулюбленіших ігор!"
    }
    return render(request, 'lab3/page.html', context)



