from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from password.models import PwdManager

# Create your views here.
from django.views import View


class PwdView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'pwd/enter.html', context={'check_result': True})

    def post(self, request):
        user = request.user
        pwd = request.POST.get('password')
        if user.check_password(pwd):
            pwds = PwdManager.objects.filter(user=user, is_delete=False)
            context = {
                'pwds': pwds
            }
            return render(request, 'pwd/pwd_list.html', context=context)
        else:
            return render(request, 'pwd/enter.html', context={'check_result': False})
