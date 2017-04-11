from django import forms

from . import models

class LinkedinProfileForm(forms.ModelForm):
    class Meta:
        model = models.LinkedinProfile
        fields = [
            'profile_link',
        ]

    def clean(self):
        cleaned_data = super(LinkedinProfileForm, self).clean()
        profile_link = cleaned_data.get("profile_link")

        profile_list = [str(profile) for profile in models.LinkedinProfile.objects.all()]

        if profile_link[-1] == '/':
            raise forms.ValidationError("Profile link must not end with slash!")
        if profile_link in profile_list:
            raise forms.ValidationError("This profile already exist in our database!")
