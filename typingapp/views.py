from django.views import generic
from .models import Content, History, Favorite
from django.shortcuts import redirect

class IndexView(generic.DetailView):
    model = Content
    template_name = "index.html"
    context_object_name = "content_object"

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk", 1)
        return Content.objects.get(pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content_list'] = Content.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")

        if action == "save_history":
            return self.save_history(request, *args, **kwargs)
        elif action == "add_favorite":
            return self.add_favorite(request, *args, **kwargs)
        elif action == "delete_favorite":
            return self.delete_favorite(request, *args, **kwargs)

    def save_history(self, request, *args, **kwargs):
        typing_time = request.POST.get('typing_time')
        pk = self.kwargs['pk'] #URLからpkを取得
        content = Content.objects.get(pk=pk) #取得したpkのContentモデルのインスタンスを取得
        history = History(user=request.user, title=content, typing_time=typing_time)
        history.save()
        return redirect("typingapp:index")
    
    def add_favorite(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        content = Content.objects.get(pk=pk)
        favorite = Favorite(user=request.user, title=content)
        favorite.save()
        return redirect("typing:index")
    
    def delete_favorite(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        content = Content.objects.get(pk=pk)
        favorite = Favorite(user=request.user, title=content)
        favorite.delete()
        return redirect("typing:index")