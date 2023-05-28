
from django.shortcuts import render
from django.views.generic import ListView, DetailView # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import News, Category
from datetime import datetime
from django.core.paginator import Paginator # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from django.views import View

from .filters import NewsFilter # импортируем недавно написанный фильтр


class NewsList(ListView):
    model = News  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = News.objects.order_by('-id')
    ordering = ['-price']
    paginate_by = 10 # поставим постраничный вывод в один элемент


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow() # добавим переменную текущей даты time_now
        context['value1'] = None # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset()) # вписываем наш фильтр в контекст

        return context

    def get(self, request):
        news = News.objects.order_by('-price')
        p = Paginator(news, 10)  # создаём объект класса пагинатор, передаём ему список наших товаров и их количество для одной страницы

        news = p.get_page(request.GET.get('page', 1))  # берём номер страницы из get-запроса. Если ничего не передали, будем показывать первую страницу.
        # теперь вместо всех объектов в списке товаров хранится только нужная нам страница с товарами

        data = {
            'news': news,
        }
        return render(request, 'news.html', data)

# создаём представление, в котором будут детали конкретного отдельного товара
class NewsDetail(DetailView):
    model = News # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'new.html' # название шаблона будет product.html
    context_object_name = 'new' # название объекта

