from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .forms import MessageForm
from .models import Message


@login_required
def inbox(request):
    received = Message.objects.filter(recipient=request.user)
    sent = Message.objects.filter(sender=request.user)[:10]
    return render(request, 'messenger/inbox.html', {'received': received, 'sent': sent})


@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.sender = request.user
            new_message.save()
            messages.success(request, 'El mensaje fue enviado correctamente.')
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'messenger/message_form.html', {'form': form})


@login_required
def message_detail(request, pk):
    message = get_object_or_404(
        Message,
        Q(pk=pk) & (Q(recipient=request.user) | Q(sender=request.user))
    )
    if message.recipient == request.user and not message.read:
        message.read = True
        message.save(update_fields=['read'])
    return render(request, 'messenger/message_detail.html', {'message': message})
