from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    username = models.CharField(_("username"), max_length=150, unique=True)
    bio = models.CharField(max_length=255, blank=True, null=True)

    email = models.EmailField(_("email address"), blank=True, unique=True)

    profile_picture = models.ImageField(upload_to='profile_pics/%Y/%m', blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = ""
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        abstract = True

    def __str__(self):
        return self.username


class Post(BaseModel):
    title = models.CharField(max_length=32, verbose_name=_('Title'))
    description = models.CharField(max_length=164, verbose_name=_('Description'))

    image = models.ImageField(upload_to='post_images/')

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class PostLike(BaseModel):
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("post", "user"),)


class PostComment(BaseModel):
    comment_text = models.CharField(max_length=264, verbose_name=_('Comments'))

    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE, related_name='comments')


class UserFollow(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name="src_follow")
    follows = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name="dest_follow")
