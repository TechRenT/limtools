from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms
from . import models

@login_required
def linkedin_profile_list(request):
    linkedin_profiles = models.LinkedinProfile.objects.all()
    return render(request, 'linkedin/linkedin_profile_list.html', {'linkedin_profiles': linkedin_profiles})

@login_required
def linkedin_profile_create(request):
    form = forms.LinkedinProfileForm()
    linkedin_profiles = len(models.LinkedinProfile.objects.all())
    if request.method == 'POST':
        form = forms.LinkedinProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                'LinkedIn profile has been successfully added!')
            return HttpResponseRedirect(reverse('linkedin:linkedin_form'))
    return render(request, 'linkedin/linkedin_form.html', {'form': form, 'profiles': linkedin_profiles})

