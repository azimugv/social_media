from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
	body = models.TextField()
	created_on = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	likes = models.ManyToManyField(User, blank=True, related_name='likes')
	dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
	loves = models.ManyToManyField(User, blank=True, related_name='loves')
	hahas = models.ManyToManyField(User, blank=True, related_name='haha')

	def __str__(self):
		return f'{self.body}'

class Comment(models.Model):
	comment = models.TextField()
	created_on = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey('Post', on_delete=models.CASCADE)
	likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
	dislikes = models.ManyToManyField(User, blank=True, related_name='comment_dislikes')
	loves = models.ManyToManyField(User, blank=True, related_name='comment_loves')
	hahas = models.ManyToManyField(User, blank=True, related_name='comment_haha')
	parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')

	@property
	def children(self):
		return Comment.objects.filter(parent=self).order_by('-created_on').all()

	@property
	def is_parent(self):
		if self.parent is None:
			return True
		return False


	

	def __str__(self):
		return f'{self.comment}'
	

class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
	name = models.CharField(max_length=30, blank=True, null=True)
	bio = models.TextField(max_length=500, blank=True, null=True)
	birth_date = models.DateField(null=True, blank=True)
	location = models.CharField(max_length=30, blank=True, null=True)
	picture = models.ImageField(upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.png', blank=True)
	followers = models.ManyToManyField(User, blank=True, related_name='follower')


	def __str__(self):
		return f'{self.name} Profile'

@receiver(post_save, sender=User)
def crete_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)
	pass


@receiver(post_save, sender=User)
def  save_user_profile(sender, instance, **kwargs):
	instance.profile.save()




class Notification(models.Model):

	# 1 = React, 2 = Comment, 3 = Follow

	notification_type = models.IntegerField()
	to_user = models.ForeignKey(User, related_name='notification_to', on_delete=models.CASCADE, null=True)
	from_user = models.ForeignKey(User, related_name='notification_from', on_delete=models.CASCADE, null=True)

	post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='+', blank=True, null=True)
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='+', blank=True, null=True)
	date = models.DateTimeField(default=timezone.now)
	user_has_seen = models.BooleanField(default=False)