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
    
    def post(self, request, *args, **kwargs):
        username = request.user.username
        pk = request.POST.get('pk')
        Favorite.objects.filter(pk=pk).delete()
        return redirect("contentapp:mypage", username=username)
        

class TypingListView(generic.ListView):
    template_name = "typing_list.html"
    context_object_name = "typing_list"

    def get_queryset(self):
        queryset = Content.objects.filter(is_public=True)
        search = self.request.POST.get('search')
        search_for = self.request.POST.get('search_for')
        if search:
            if search_for == "title":
                queryset = queryset.filter(title__icontains=search)
            elif search_for == "content":
                queryset = queryset.filter(content__icontains=search)

        return queryset