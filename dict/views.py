from django.shortcuts import render

# Create your views here.
from PyDictionary import PyDictionary
def home(request):
  return render(request,'index.html')

def search(request):
    word = request.GET.get('search')
    context = {
        'word': word,
        'meaning': None,
    }

    if word:
        dictionary = PyDictionary()
        meaning = dictionary.meaning(word)

        if meaning:
            context['meaning'] = meaning
        else:
            context['error'] = f'No meaning found for "{word}".'
    else:
        context['error'] = 'No search term provided.'

    return render(request, "search.html", context)