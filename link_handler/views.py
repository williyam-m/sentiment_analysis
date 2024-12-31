from django.shortcuts import render
from analysis.arguments import get_arguments
from analysis.analyzer import Analyzer
from web_scraper.views import scrape_kynhood_post
from django.contrib.auth.decorators import login_required

error_msg = ["Post not exist or something went wrong", "Link must be https://kynhood.com/post/"]

@login_required(login_url='signin')
def link_index(request):
    return render(request, "link_index.html")


@login_required(login_url='signin')
def link_sentiment(request):
    if request.method == 'POST':
        link = request.POST.get("link")
        option = request.POST.get("option")

        if option == "kyn":
            content = scrape_kynhood_post(link)
            print(content)

            if content in error_msg:
                return render(request, "link_index.html",
                              {"error": content})

            analyzer = Analyzer(will_train=False, args_dict=get_arguments())
            sentiment, percentage = analyzer.classify_sentiment(content)

            return render(request, "link_index.html", {"sentiment": sentiment, "percentage": percentage, "content": content})
