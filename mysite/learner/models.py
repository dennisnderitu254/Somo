from django.db import models

class Learner(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.Charfield(max_length=100)
	learner_email = models.EmailField(max_length=200)
	learnerid = models.IntegerField(primary_key=True)

class Course(modeld.Model):
	course_id = models.IntegerField(primary_key=True)
	course_title = models.models.Charfield(max_length=100)

class Instructor(models.Model):
	instructor_id = models.IntegerField(primary_key=True)
	instructor_email = models.EmailField(max_length=200)

class CourseDuration(models.Model):
	course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
	learner_id = models.ForeignKey(Learner, on_delete=models.CASCADE)
	instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)
	course_duration = models.TimeField()



