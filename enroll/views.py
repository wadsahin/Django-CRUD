from django.shortcuts import render
from .forms import userForm
from .models import User

# Create your views here.
def add_show(request):
    if request.method == 'POST':
      fm = userForm(request.POST)
      if fm.is_valid():
        fm.save();
        fm = userForm()

    else:
      fm = userForm()
    dataShow = User.objects.all()
    return render(request, 'addandshow.html', {'form': fm, 'dt':dataShow})



 