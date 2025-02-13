from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse
from .forms import ContentForm
from typingapp.models import History, Favorite
from .models import Content

class CreateContentView(generic.CreateView):
    form_class = ContentForm
    template_name = "create_content.html"

    def form_valid(self, form):
        data = form.save(commit=False)
        data.user = self.request.user
        data.save()
        success_url = reverse('typingapp:typing', kwargs={'pk':data.pk})
        return redirect(success_url)
    
class MyPageView(generic.TemplateView):
    template_name = "mypage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_content_list'] = Content.objects.filter(user=self.request.user)
        context['my_history_list'] = History.objects.filter(user=self.request.user)
        context['my_favorite_list'] = Favorite.objects.filter(user=self.request.user)
        return context
    
    # def post(self, request, *args, **kwargs):
    #     username = request.user.username
    #     pk = request.POST.get('pk')
    #     Favorite.objects.filter(pk=pk).delete()
    #     return redirect("contentapp:mypage", username=username)
        
    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")

        if action =="del_favorite":
            return
        elif action == "set_public":
            return
        elif action == "set_private":
            return
        
    def del_favorite(self, request, *args, **kwargs):
        pk = request.POST.get("pk")
        Favorite.objects.filter(pk=pk).delete()
        return redirect("contentapp:mypage", username=request.user.username)
    
    def set_public(self, request, *args, **kwargs):
        pk = request.POST.get("pk")
        content = Content.objects.filter(pk=pk)
        content(is_public=True)
        return redirect("contentapp:mypage", username=request.user.username)

class TypingListView(generic.ListView):
    template_name = "typing_list.html"
    context_object_name = "typing_list"

    def get_queryset(self):
        queryset = Content.objects.filter(is_public=True)
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset