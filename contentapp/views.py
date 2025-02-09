from django.views import generic
from .forms import ContentForm
from django.shortcuts import redirect
from django.urls import reverse

class CreateContentView(generic.CreateView):
    form_class = ContentForm
    template_name = "create_content.html"

    def form_valid(self, form):
        data = form.save(commit=False)
        data.user = self.request.user
        data.save()
        success_url = reverse('typingapp:typing', kwargs={'pk':data.pk})
        return redirect(success_url)