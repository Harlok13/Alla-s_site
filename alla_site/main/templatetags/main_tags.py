from django import template

register = template.Library()

@register.inclusion_tag('main/tag/list_menu.html')
def show_menu(menu_selected=0):
    menu = [
        {'title': 'Главная страница', 'url_name': 'home_page'},
        {'title': 'Обо мне', 'url_name': 'about_me'},
        {'title': 'Мои практики', 'url_name': 'practices'},
        {'title': 'Мои статьи', 'url_name': 'articles'},
        {'title': 'Консультация', 'url_name': 'consultation'},
        {'title': 'Вход', 'url_name': 'login'},
        {'title': 'Регистрация', 'url_name': 'registration'}
    ]
    return {'menu': menu, 'menu_selected': menu_selected}
