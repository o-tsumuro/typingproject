from django.views import generic
from .forms import ContentForm
from django.shortcuts import redirect
from django.urls import reverse
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
        context['content_list'] = Content.objects.filter(user=self.request.user)
        context['history_list'] = History.objects.filter(user=self.request.user)
        context['favorite_list'] = Favorite.objects.filter(user=self.request.user)

        return context
    
    def post(self, request, *args, **kwargs):
        pk = int(request.POST.get('pk'))
        content = Content.objects.get(pk=pk)
        Favorite.objects.filter(user=self.request.user, title=content).delete()
        return redirect("contentapp:mypage", pk=pk)
        