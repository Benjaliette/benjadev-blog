from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from posts.models import Post
from posts.forms import PostForm
from django.urls import reverse, reverse_lazy
from allauth.utils import get_user_model

# Create your views here.
class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name_suffix = '_create_form'

    def get_success_url(self):
        return reverse("posts:show", kwargs={'pk': self.object.id})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial']['user'] = self.request.user
        return kwargs

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse("posts:show", kwargs={'pk': self.object.id})

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("posts:index")
