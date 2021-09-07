from django.shortcuts import render
from .forms import BaseForm
from .models import Base

# A method that outputs a specific html template.
def index(request):
    error = ''
    # Processing the received data, checking and saving on server. Otherwise, the error text will be displaed
    if request.method == "POST":
        form = BaseForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Something went wrong'

    form = BaseForm()
    data = Base.objects.order_by('date')
    context = {
        'form': form,
        'error': error,
        'data': data,
    }

    return render(request, 'main/main.html', context)
