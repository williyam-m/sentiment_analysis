from django.shortcuts import render
from analysis.arguments import get_arguments
from analysis.analyzer import Analyzer
from django.contrib.auth.decorators import login_required


@login_required(login_url='signin')
def text_index(request):
    return render(request, "text_index.html")


@login_required(login_url='signin')
def text_sentiment(request):
    if request.method == 'POST':
        text = request.POST.get("sentence")
        analyzer = Analyzer(will_train=False, args_dict=get_arguments())
        sentiment, percentage = analyzer.classify_sentiment(text)
        return render(request, "text_index.html", {"sentiment": sentiment, "percentage": percentage, "sentence": text})
