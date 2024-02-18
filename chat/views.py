from django.shortcuts import render

# the view function for the chat page
def chat_page(request):
    return render(request, 'chat/chat_page.html')
