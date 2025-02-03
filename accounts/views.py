from django.views import generic
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)