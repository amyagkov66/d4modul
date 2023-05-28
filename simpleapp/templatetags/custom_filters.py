from django import template

register = template.Library()  # если мы не зарегестрируем наши фильтры, то django никогда не узнает где именно их искать и фильтры потеряются :(

mat_list = ['сука','педик','блядь','лох']


@register.filter(name='censor')
def matt(value):
    a = []
    value = value.split()
    for i in value:
      if i in mat_list:
        i = "***"
      a.append(i)
    s = " ".join(a)
    return s




# @register.filter(name='censor')
# def matt(value):
#     value = value.split()
#     for i in value:
#       if i in mat_list:
#         i = "***"
#       a.append(i)
#     s = " ".join(a)
#     return s