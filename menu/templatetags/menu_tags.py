from django import template
from ..models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu_items_filtered = MenuItem.objects.all()
    menu_items = []
    for menu_item in menu_items_filtered:
        if menu_item.parent and menu_item.parent.title == menu_name:
            menu_items.append(menu_item)
    if not menu_items:
        return ''

    return template.Template('''
    <ul>
        {% for menu_item in menu_items %}
            <li class="dropdown">
                <a href={{menu_item.get_absolute_url}}>{{ menu_item.title }}</a>
                    {% if menu_item.children.exists %}
                        <div class="dropdown-content">
                            {% for child in menu_item.children.all %}
                                <a href={{child.get_absolute_url}}>{{ child.title }}</a>
                            {% endfor %}
                        </div>
                    {% endif %}
            </li>
        {% endfor %}
    </ul>
    ''').render(template.Context({'menu_items': menu_items}))