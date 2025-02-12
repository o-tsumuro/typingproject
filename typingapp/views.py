from django.views import generic
from .models import History, Favorite
from contentapp.models import Content
from django.shortcuts import redirect

def first_view(request):
    pk = 1
    return redirect("typingapp:typing", pk=pk)

class IndexView(generic.DetailView):
    model = Content
    template_name = "index.html"
    context_object_name = "content_object"

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk", 1)
        return Content.objects.get(pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        content = Content.objects.get(pk=pk)
        if self.request.user.is_authenticated:
            is_favorite = Favorite.objects.filter(user=self.request.user, title=content).exists()
        else:
            is_favorite = False
        context['is_favorite'] = is_favorite
        context['content_list'] = Content.objects.filter(is_public=True)
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
        typing_time = int(request.POST.get('typing_time'))
        pk = self.kwargs['pk']
        content = Content.objects.get(pk=pk)
        history = History(user=request.user, title=content, typing_time=typing_time)
        existing_history = History.objects.filter(user=request.user, title=content).first()

        if existing_history:
            if existing_history.typing_time >= typing_time:
                existing_history.delete()
                history.save()
        else:
            history.save()
        return redirect("typingapp:typing", pk=pk)
    
    def add_favorite(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        content = Content.objects.get(pk=pk)
        favorite = Favorite(user=request.user, title=content)
        favorite.save()
        return redirect("typingapp:typing", pk=pk)
    
    def delete_favorite(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        content = Content.objects.get(pk=pk)
        Favorite.objects.filter(user=request.user, title=content).delete()
        return redirect("typingapp:typing", pk=pk)