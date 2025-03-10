from django.contrib import admin
from .models import Category, Difficulty, Problem, UserProblem, Company, StudyPlan, UserStudyPlan

admin.site.register(Category)
admin.site.register(Difficulty)
admin.site.register(Problem)
admin.site.register(UserProblem)
admin.site.register(Company)
admin.site.register(StudyPlan)
admin.site.register(UserStudyPlan)