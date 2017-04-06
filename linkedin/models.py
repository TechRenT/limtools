from django.db import models


class LinkedinProfile(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    profile_link = models.URLField(max_length=200)
    # checker = models.ForeignKey(User)

    def __str__(self):
        return self.profile_link
