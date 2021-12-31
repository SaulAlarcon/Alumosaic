from django.shortcuts import render

gallery = [
    {
        'author': 'Saul',
        'title': 'Test Post 1',
        'content': 'Test Content 1',
        'date_posted': 'December 26, 2021'
    },
    {
        'author': 'Saul',
        'title': 'Test Post 2',
        'content': 'Test Content 2',
        'date_posted': 'December 26, 2021'
    }
]

def home(request):
    context = {
        'gallery': gallery
    }
    return render(request, 'alumosaic/home.html', context)

def about(request):
    return render(request, 'alumosaic/about.html', {'title': 'About'})

