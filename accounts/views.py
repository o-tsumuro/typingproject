from django.views import generic
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('typingapp:index')

    def form_valid(self, form):
        respense = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return respense