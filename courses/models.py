from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject






class Course(models.Model):

    id = models.IntegerField(primary_key=True)

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)  # Add this line

    def __str__(self):
        return self.title

class Chapter(models.Model):
    COURSE_CONTENT_CHOICES = [
        ('PDF', 'PDF'),
        ('TEXT', 'Text'),
        ('VIDEO', 'Video'),
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=100)
    description = models.TextField()
    content_type = models.CharField(max_length=10, choices=COURSE_CONTENT_CHOICES)
    content = models.FileField(upload_to='chapters/', null=True, blank=True)

    def __str__(self):
        return f"{self.course.title} - {self.title}"






class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text