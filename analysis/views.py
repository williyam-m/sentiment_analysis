from django.shortcuts import get_object_or_404, render, redirect
from .arguments import get_arguments
from .analyzer import Analyzer


def index(request):
    return render(request, "index.html")


def sentiment(request):
    #text = request.args["text"]
    analyzer = Analyzer(will_train=False, args_dict=get_arguments())
    text = "test"
    sentiment, percentage = analyzer.classify_sentiment(text)
    print(sentiment)
    return render(request, "index.html", {"sentiment": sentiment, "percentage": percentage})





