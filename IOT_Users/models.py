from django.db import models
from django.contrib.auth.models import User

class IOTUser(models.Model):
	user = models.ForeignKey(User)

	user_choices = (
		('D', 'Doctor'),
		('N', 'Nurse'),
	)
	user_type = models.CharField(max_length=30, choices=user_choices)

	# def __str__(self):
	# 	return self.usernames
	# 	return '{l}, {f}'.format(l=self.last_name, f=self.first_name)