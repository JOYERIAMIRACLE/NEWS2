from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View
from newsletters.models import Newsletter
from newsletters.forms import NewsletterCreationForm
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
# Create your views here.
class DashboardHomeView(TemplateView):
    template_name="dashboard/index.html"

class NewslettersDashboardHomeView(View):
    def get(self, request, *args, **krwargs):
        newsletters= Newsletter.objects.all()
        context= {
            'newsletters':newsletters

        }
        return render(request, 'dashboard/list.html', context)
        
class NewsletterCreateView(View):
    def get(self, request, *args, **kwargs):
        form = NewsletterCreationForm()
        context= {
            'form': form

        }
        return render(request, 'dashboard/create.html', context)
    def post(self, request, *args, **kwargs):
        

        if request.method=='POST':
            form = NewsletterCreationForm(request.POST or None)

            if form.is_valid():
                isinstance=form.save()
                newsletter=Newsletter.objects.get(id=isinstance.id)

                if newsletter.status=='published':
                    subject = newsletter.subject
                    body = newsletter.body
                    from_email = settings.EMAIL_HOST_USER
                    for email in newsletter.email.all():
                        send_mail(subject=subject, from_email=from_email,recipient_list=[email], message=body, fail_silently=True)
                return redirect('dashboard:list')

        context= {
            'form': form

        }
        return render(request, 'dashboard/create.html', context)
    

class NewsletterDetailview(View):
    def get(self, request,pk, *args, **kwargs):
        newsletter=get_object_or_404(Newsletter, pk=pk)
        context= {
            'newsletter': newsletter
        }
        return render(request, 'dashboard/detail.html', context)