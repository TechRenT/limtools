from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms
from . import models

@login_required
def linkedin_profile_list(request):
    linkedin_profiles_list = models.LinkedinProfile.objects.all()
    total = len(linkedin_profiles_list)
    page = request.GET.get('page', 1)

    paginator = Paginator(linkedin_profiles_list, 100)
    try:
        linkedin_profiles = paginator.page(page)
    except PageNotAnInteger:
        linkedin_profiles = paginator.page(1)
    except EmptyPage:
        linkedin_profiles = paginator.page(paginator.num_pages)

    return render(request, 'linkedin/linkedin_profile_list.html', {'linkedin_profiles': linkedin_profiles,
                                                                   'total': total})

@login_required
def linkedin_profile_create(request):
    form = forms.LinkedinProfileForm()
    linkedin_profiles = len(models.LinkedinProfile.objects.all())
    if request.method == 'POST':
        form = forms.LinkedinProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.checker = request.user
            profile.save()
            messages.add_message(request, messages.SUCCESS,
                'LinkedIn profile has been successfully added!')
            return HttpResponseRedirect(reverse('linkedin:linkedin_form'))
    return render(request, 'linkedin/linkedin_form.html', {'form': form, 'profiles': linkedin_profiles})

