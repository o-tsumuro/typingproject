from django.views import generic
from .models import Content, History
from .forms import HistoryForm
from django.shortcuts import redirect

class IndexView(generic.DetailView):
    model = Content
    template_name = "index.html"
    context_object_name = "content_object"

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk", 1)
        return Content.objects.get(pk=pk)
    
    def post(self, request, *args, **kwargs):
        typing_time = request.POST.get('typing_time')
        pk = self.kwargs['pk'] #URLからpkを取得
        content = Content.objects.get(pk=pk) #取得したpkのContentモデルのインスタンスを取得
        history = History(user=request.user, title=content, typing_time=typing_time)
        history.save()
        return redirect("typingapp:index")

class ContentListView(generic.ListView):
    model = Content
    template_name = "content_list.html"
    context_object_name = "content_object"
    queryset = Content.objects.order_by("pk")