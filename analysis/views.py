from django.shortcuts import render
from .arguments import get_arguments
from .analyzer import Analyzer

def index(request):
    return render(request, "index.html")

def sentiment(request):
    if request.method == 'POST':
        text = request.POST.get("sentence")
        analyzer = Analyzer(will_train=False, args_dict=get_arguments())
        sentiment, percentage = analyzer.classify_sentiment(text)
        print(sentiment)
        print(percentage)
        return render(request, "index.html", {"sentiment": sentiment, "percentage": percentage, "sentence": text})
