from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    full_text = request.GET['fulltext']
    num_words = full_text.split()
    text_len = len(full_text)

    word_dictionary = {}

    for word in num_words : 
        if word in word_dictionary :
            word_dictionary[word] += 1
        else :
            word_dictionary[word] = 1

    return render(request, 'count.html', {'text' : full_text, 'word' : num_words, 'len' : text_len, 'dic' : word_dictionary.items})
