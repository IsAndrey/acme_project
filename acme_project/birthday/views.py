from typing import Any, Dict
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .forms import BirthdayForm
from .utils import calculate_birthday_countdown
from .models import Birthday
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context

class BirthdayDeleteView(DeleteView):
    model = Birthday
    success_url = reverse_lazy('birthday:new_list')


class BirthdayUpdateView(UpdateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayCreateView(CreateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 1


def birthday(request, pk=None):
    """Отображение страницы birthday.html в режиме создания/изменения"""
    instance = None
    oper = 'Создать'
    if pk is not None:
        instance = get_object_or_404(Birthday, pk=pk)
        oper = 'Изменить'
    form = BirthdayForm(
        request.POST or None,
        files=request.FILES or None,
        instance=instance
    )
    context = {'form': form, 'oper': oper}
    if form.is_valid():
        form.save()
        birthday_countdown = calculate_birthday_countdown(
            birthday=form.cleaned_data['birthday']
        )
        context.update({'birthday_countdown': birthday_countdown})
    return render(request, 'birthday/birthday.html', context=context)


def birthday_list(request):
    """Отображение страницы birthday_list.html"""
    birthdays = Birthday.objects.order_by('id')
    paginator = Paginator(birthdays, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # context = {'birthdays': birthdays}
    context = {'page_obj': page_obj}
    return render(request, 'birthday/birthday_list.html', context=context)


def birthday_delete(request, pk=None):
    """отображение страницы birthday.html в режиме удаления"""
    instance = get_object_or_404(Birthday, pk=pk)
    oper = 'Удалить'
    form = BirthdayForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        instance.delete()
        return redirect('birthday:list')
    context = {'form': form, 'oper': oper}
    return render(request, 'birthday/birthday.html', context=context)
