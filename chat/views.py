from django.shortcuts import render

def Page(request):
    return render(request, 'chat/chat_page.html')
