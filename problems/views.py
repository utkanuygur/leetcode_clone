from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Problem, Category, UserProblem, StudyPlan, UserStudyPlan, Company, Difficulty

def home(request):
    categories = Category.objects.all().order_by('-count')
    return render(request, 'home.html', {'categories': categories})

def problem_list(request):
    categories = Category.objects.all().order_by('-count')
    
    # Get query parameters for filtering
    category = request.GET.get('category')
    difficulty = request.GET.get('difficulty')
    status = request.GET.get('status')
    search = request.GET.get('search')
    
    # Start with all problems
    problems = Problem.objects.all().order_by('id')
    
    # Apply filters
    if category:
        problems = problems.filter(categories__name=category)
    
    if difficulty:
        problems = problems.filter(difficulty__name=difficulty)
    
    if search:
        problems = problems.filter(Q(title__icontains=search) | Q(description__icontains=search))
    
    # Get the user's completed problems
    user_problems = {}
    if request.user.is_authenticated:
        user_problem_records = UserProblem.objects.filter(user=request.user)
        for up in user_problem_records:
            user_problems[up.problem.id] = up.completed
    
    # Get study plans
    study_plans = []
    if request.user.is_authenticated:
        user_study_plans = UserStudyPlan.objects.filter(user=request.user, active=True)
        for usp in user_study_plans:
            study_plans.append({
                'name': usp.study_plan.name,
                'progress': usp.progress,
                'description': usp.study_plan.description
            })
    
    # Get companies
    companies = Company.objects.all().order_by('-count')
    
    context = {
        'categories': categories,
        'problems': problems,
        'user_problems': user_problems,
        'study_plans': study_plans,
        'companies': companies,
    }
    
    return render(request, 'problem_list.html', context)

@login_required
def problem_detail(request, problem_id):
    problem = Problem.objects.get(id=problem_id)
    
    # Get user's progress on this problem
    user_problem, created = UserProblem.objects.get_or_create(
        user=request.user,
        problem=problem
    )
    
    context = {
        'problem': problem,
        'user_problem': user_problem
    }
    
    return render(request, 'problem_detail.html', context)