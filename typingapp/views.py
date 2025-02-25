from django.views import generic
from django.shortcuts import redirect
from django.db.models import F
from .models import History, Favorite
from contentapp.models import Content

def first_view(request):
    pk = Content.objects.order_by("pk").first().pk
    return redirect("typingapp:typing", pk=pk)

class IndexView(generic.DetailView):
    model = Content
    template_name = "index.html"
    context_object_name = "content_object"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        content = Content.objects.get(pk=pk)
        if self.request.user.is_authenticated:
            is_favorite = Favorite.objects.filter(user=self.request.user, title=content).exists()
        else:
            is_favorite = False
        context['is_favorite'] = is_favorite
        context['content_list'] = Content.objects.filter(is_public=True).order_by('?')
        context['ranking_list'] = History.objects.filter(title__title=self.object.title).order_by("typing_time")
        return context

    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")

        if action == "save_history":
            return self.save_history(request, *args, **kwargs)
        elif action == "guest_result":
            return self.guest_result(request, *args, **kwargs)
        elif action == "add_favorite":
            return self.add_favorite(request, *args, **kwargs)
        elif action == "delete_favorite":
            return self.delete_favorite(request, *args, **kwargs)

    def save_history(self, request, *args, **kwargs):
        typing_time = int(request.POST.get('typing_time'))
        pk = self.kwargs['pk']
        content = Content.objects.get(pk=pk)

        Content.objects.filter(pk=pk).update(play_count=F("play_count") + 1)

        history = History(user=request.user, title=content, typing_time=typing_time)
        existing_history = History.objects.filter(user=request.user, title=content).first()

        if existing_history:
            result_page_pk = existing_history.pk
            if existing_history.typing_time >= typing_time:
                existing_history.delete()
                history.save()
                result_page_pk = history.pk
        else:
            history.save()
            result_page_pk = history.pk

        return redirect("typingapp:result", pk=result_page_pk, typing_time=typing_time)
    
    def guest_result(self, request, *args, **kwargs):
        typing_time = int(request.POST.get('typing_time'))
        pk = self.kwargs['pk']
        return redirect("typingapp:guest_result", pk=pk, typing_time=typing_time)

    
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
    
class ResultView(generic.DetailView):
    model = History
    template_name = "result.html"
    context_object_name = "history"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        typing_time = self.kwargs.get("typing_time")
        pk = self.kwargs['pk']
        history = History.objects.get(pk=pk)

        if self.request.user.is_authenticated:
            is_favorite = Favorite.objects.filter(user=self.request.user, title=history.title).exists()
        else:
            is_favorite = False

        context['is_favorite'] = is_favorite
        context["typing_time"] = int(typing_time)
        context["is_best_time"] = typing_time == self.object.typing_time
        context['ranking_list'] = History.objects.filter(title__title=self.object.title).order_by("typing_time")
        context['content_list'] = Content.objects.filter(is_public=True).order_by('-play_count')
        return context
    
    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")

        if action == "add_favorite":
            return self.add_favorite(request, *args, **kwargs)
        elif action == "delete_favorite":
            return self.delete_favorite(request, *args, **kwargs)
        
    def add_favorite(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        typing_time = self.kwargs['typing_time']
        history = History.objects.get(pk=pk)
        favorite = Favorite(user=request.user, title=history.title)
        favorite.save()
        return redirect("typingapp:result", pk=pk, typing_time=typing_time)
    
    def delete_favorite(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        typing_time = self.kwargs['typing_time']
        history = History.objects.get(pk=pk)
        Favorite.objects.filter(user=request.user, title=history.title).delete()
        return redirect("typingapp:result", pk=pk, typing_time=typing_time)
    
class GuestResultView(generic.DetailView):
    model = Content
    template_name = "guest_result.html"
    context_object_name = "content_object"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        typing_time = self.kwargs.get("typing_time")
        context['typing_time'] = int(typing_time)
        context['ranking_list'] = History.objects.filter(title__title=self.object.title).order_by("typing_time")
        context['content_list'] = Content.objects.filter(is_public=True).order_by("-play_count")
        return context