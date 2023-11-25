from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,UpdateView,ListView,DetailView,View
from .models import Notice,Response
from .forms import NoticeForm,ResponseForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .tasks import notification_send

class NoticeCreateView(LoginRequiredMixin,CreateView):
    model = Notice
    template_name = 'NoticeCreate.html'
    form_class = NoticeForm

class NoticeUpdateView(LoginRequiredMixin,UpdateView):
    model = Notice
    template_name = 'NoticeUpdate.html'
    form_class = NoticeForm

class NoticeListView(ListView):
    model=Notice
    paginate_by = 10
    template_name = 'NoticeList.html'
    context_object_name = 'notices'

class NoticeView(DetailView):
    model = Notice
    template_name = 'NoticeDetail.html'
    context_object_name = 'notice'

    def get_context_data(self, **kwargs):
        context = super(NoticeView, self).get_context_data(**kwargs)
        context['response_form'] = ResponseForm(initial={'notice_pk': self.object.pk})

        return context


class ResponseCreateView(CreateView):
    model = Response
    template_name = 'ResponseCreate.html'
    form_class = ResponseForm
    success_url = reverse_lazy('NoticeList')



class UserNoticeListView(View):
    def get(self, request):
        user = request.user
        notices = Notice.objects.filter(author__name=user)
        response_form = ResponseForm()

        response_data = []
        for notice in notices:
            responses = Response.objects.filter(notice=notice)
            response_data.append({
                'notice': notice,
                'responses': responses
            })

        return render(request, 'UserNoticeList.html', {
            'response_data': response_data,
            'response_form': response_form
        })

    def post(self, request):
        response_form = ResponseForm(request.POST)
        if response_form.is_valid():
            response = response_form.save()

            author = response.notice.author
            subject = 'Ваш отклик был принят'
            message = 'Ваш отклик на объявление "{0}" был принят.'.format(response.notice.title)
            send_mail(subject, message, 'Nikto51@yandex.ru', [author.name.email])

            response_data = []
            notices = Notice.objects.filter(author__name=request.user)
            for notice in notices:
                responses = Response.objects.filter(notice=notice)
                response_data.append({
                    'notice': notice,
                    'responses': responses
                })

            return render(request, 'UserNoticeList.html', {
                'response_data': response_data,
                'response_form': response_form
            })












