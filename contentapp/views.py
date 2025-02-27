from django.views import generic
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import ContentForm
from typingapp.models import History, Favorite
from .models import Content, Category

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
        action = request.POST.get("action")

        if action =="del_favorite":
            return self.del_favorite(request, *args, **kwargs)
        elif action == "set_public":
            return self.set_public(request, *args, **kwargs)
        elif action == "set_private":
            return self.set_private(request, *args, **kwargs)
        
    def del_favorite(self, request, *args, **kwargs):
        pk = request.POST.get("pk")
        Favorite.objects.filter(pk=pk).delete()
        return redirect("contentapp:mypage", username=request.user.username)
    
    def set_public(self, request, *args, **kwargs):
        pk = request.POST.get("pk")
        Content.objects.filter(pk=pk).update(is_public=True)
        return redirect("contentapp:mypage", username=request.user.username)
    
    def set_private(self, request, *ars, **kwargs):
        pk = request.POST.get("pk")
        Content.objects.filter(pk=pk).update(is_public=False)
        return redirect("contentapp:mypage", username=request.user.username)

class TypingListView(generic.ListView):
    template_name = "typing_list.html"
    context_object_name = "typing_list"
    paginate_by = 21

    def get_queryset(self):
        queryset = Content.objects.filter(is_public=True)

        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(title__icontains=search)

        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ContentSettingsView(generic.DetailView):
    model = Content
    template_name = "content_settings.html"
    context_object_name = "content_object"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContentForm

        return context

    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")

        if action == "update_content":
            return self.update_content(request, *args, **kwargs)
        elif action == "del_content":
            return self.del_content(request, *args, **kwargs)
        
    def update_content(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        title = request.POST.get("title")
        sentence = request.POST.get("sentence")
        category = request.POST.get("category")
        is_public = request.POST.get("is_public")

        if is_public == "on":
            is_public = True
        else:
            is_public = False

        Content.objects.filter(pk=pk).update(title=title, sentence=sentence, category=category, is_public=is_public)
        return redirect("contentapp:mypage", username=request.user.username)

    def del_content(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        Content.objects.filter(pk=pk).delete()
        return redirect("contentapp:mypage", username=request.user.username)