from django.shortcuts import render
from analysis.arguments import get_arguments
from analysis.analyzer import Analyzer
from django.contrib.auth.decorators import login_required


@login_required(login_url='signin')
def link_index(request):
    return render(request, "link_index.html")


@login_required(login_url='signin')
def link_sentiment(request):
    if request.method == 'POST':
        link = request.POST.get("link")
        option = request.POST.get("option")

        # Assuming your analyzer can handle URLs or process content from URLs
        analyzer = Analyzer(will_train=False, args_dict=get_arguments())
        sentiment, percentage = analyzer.classify_sentiment(link)  # Modify this if needed to process the link content

        return render(request, "link_index.html", {"sentiment": sentiment, "percentage": percentage, "link": link})
