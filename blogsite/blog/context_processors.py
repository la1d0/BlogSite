menu = [
    {'title': 'Главная страница', 'url_name':'home'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'О сайте', 'url_name': 'about',},
    {'title': 'Обратная связь', 'url_name': 'contact'},
]


def get_todo_context(request):
    return {'mainmenu': menu}