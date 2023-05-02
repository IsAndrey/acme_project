from django.shortcuts import render, get_object_or_404, redirect
from .forms import BirthdayForm
from .utils import calculate_birthday_countdown
from .models import Birthday


def birthday(request, pk=None):
    """Отображение страницы birthday.html в режиме создания/изменения"""
    instance = None
    oper = 'Создать'
    if pk is not None:
        instance = get_object_or_404(Birthday, pk=pk)
        oper = 'Изменить'
    form = BirthdayForm(request.POST or None, instance=instance)
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
    birthdays = Birthday.objects.all()
    context = {'birthdays': birthdays}
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

