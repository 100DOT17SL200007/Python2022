# from jinja2 import Template
#
# menu = [
#     {'index': 'Главная'},
#     {'news': 'Новости'},
#     {'about': 'О компании'},
#     {'shop': 'Магазин'},
#     {'contacts': 'Контакты'}
# ]
# link = """
#      <ul>
#          {% for c in menu -%}
#          {% if c.index -%}
#          <li><a href= "{{"/index"}}" class = "active"> {{c['index']}}</a></li>
#          <li><a href= "{{"/news"}}">Новости</a></li>
#          <li> <a href= "{{"/about"}}"> О компании </a> </li>
#          <li> <a href= "{{"/shop"}}"> Магазин </a> </li>
#          <li> <a href= "{{"/contacts"}}"> Контакты </a> </li>
#          {% endif -%}
#          {%- endfor %}
#      </ul>
#
# """
# tm = Template(link)
# msg = tm.render(menu=menu)
#
# print(msg)

# html = """
# {%- macro text_input(name, placeholder, type='text') -%}
#     <input type="{{type}}" name="{{name}}" placeholder="{{placeholder}}">
# {%- endmacro -%}
#
# <p>{{ text_input('firstname', 'Имя')}}</p>
# <p>{{ text_input('lastname', 'Фамилия') }}</p>
# <p>{{ text_input('address', 'Адрес') }}</p>
# <p>{{ text_input('phone','Телефон',  'tel' ) }}</p>
# <p>{{ text_input('email', 'Почта','email' ) }}</p>
#
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)