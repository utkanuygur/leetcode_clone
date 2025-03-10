from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Difficulty(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Difficulties"

class Problem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    example_input = models.TextField(blank=True, null=True)
    example_output = models.TextField(blank=True, null=True)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    acceptance_rate = models.DecimalField(max_digits=5, decimal_places=2)
    frequency = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category, related_name="problems")
    solution_code = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class UserProblem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    attempts = models.IntegerField(default=0)
    last_submission = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        unique_together = ('user', 'problem')
    
    def __str__(self):
        return f"{self.user.username} - {self.problem.title}"

class Company(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    problems = models.ManyToManyField(Problem, related_name="companies")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Companies"

class StudyPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    problems = models.ManyToManyField(Problem, related_name="study_plans")
    
    def __str__(self):
        return self.name

class UserStudyPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('user', 'study_plan')
    
    def __str__(self):
        return f"{self.user.username} - {self.study_plan.name}"