from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, ListView

from accounts.models import User
from userprofile.models import Profile


class TimelineView(DetailView):
    model = User
    template_name = "profile/user-profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    context_object_name = "user"
    object = None

    def get_object(self, queryset=None):
        return self.model.objects.select_related('profile').prefetch_related("posts").get(username=self.kwargs.get(self.slug_url_kwarg))

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class ProfileEditView(UpdateView):
    model = Profile
    template_name = "profile/edit-my-profile.html"
    context_object_name = "profile"
    object = None
    fields = "__all__"

    def get_object(self, queryset=None):
        return self.request.user.profile

    def post(self, request, *args, **kwargs):
        print(request.POST.get('first_name'))
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.about = request.POST.get('about')
        if request.POST.get('gender') == "male":
            user.gender = "male"
        else:
            user.gender = "female"
        user.save()
        profile = user.profile
        profile.country = request.POST.get('country')
        profile.city = request.POST.get('city')
        profile.phone = request.POST.get('phone')
        profile.save()
        return redirect(reverse_lazy('profile:edit-profile'))


def SearchProfile(request):
    profiles = User.objects.all()    
    context = {
        'profiles': profiles,
    }
    
    return render(request, 'search.html')
    


""" 
class ProfileList(ListView):
    queryset = Profile.objects.all()
    model = Profile
    template_name = 'search.html'
    paginate_by = 10
"""

""" 
class ProfileDetail(FormMixin, DetailView):
    posts = Post.objects.filter(status=1)
    #all_tags = posts.tags.all()
    model = Post
    template_name = 'post.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object.pk})
        #context['form'] = self.get_form()
        context['comments'] = self.object.comment_set.filter(approved=True)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        comment = Comment()
        comment.author = form.cleaned_data['author']
        comment.text = form.cleaned_data['text']
        comment.post = form.cleaned_data['post']
        comment.save()
        return super(PostDetail, self).form_valid(form)
 """