from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MeetingRequest
from .forms import MeetingRequestForm
from django.core.paginator import Paginator 
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import MeetingRequest

@staff_member_required
def manage_meetings(request):
    meeting_requests = MeetingRequest.objects.all()
    
    paginacao = Paginator(meeting_requests, 10) # '3' é numero de registro por pagina
    
    # Obter o número da página a partir dos parâmetros da URL
    pagina_numero = request.GET.get("page") # 2 3 4 5 
    page_obj = paginacao.get_page(pagina_numero)
    
    return render(request, 'manage_meetings.html', {'page_obj': page_obj})


@login_required
def request_meeting(request):
    if request.method == 'POST':
        form = MeetingRequestForm(request.POST)
        if form.is_valid():
            meeting_request = form.save(commit=False)
            meeting_request.user = request.user
            meeting_request.save()
            return redirect('meeting_success')
    else:
        form = MeetingRequestForm()
    return render(request, 'request_meeting.html', {'form': form})

def meeting_success(request):
    return render(request, 'meeting_success.html')
