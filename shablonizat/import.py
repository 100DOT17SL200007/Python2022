from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('shablonizat./templates')
env = Environment(loader=file_loader)

tm = env.get_template('hom.html')
msg = tm.render(title = "Домашнее задание", ep = "Страница с домашним заданием")

print(msg)