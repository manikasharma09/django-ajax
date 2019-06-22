from django.db import models

class Post(models.Model):
	post_heading=models.CharField(max_length=200)
	post_text=models.TextField()

	def __str__(self):
		return self.post_heading

class Like(models.Model):
	post=models.ForeignKey(Post,on_delete=models.CASCADE)

