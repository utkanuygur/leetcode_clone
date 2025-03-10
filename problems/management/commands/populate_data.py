from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from problems.models import Category, Difficulty, Problem, Company, StudyPlan

class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **options):
        # Create difficulties
        easy, _ = Difficulty.objects.get_or_create(name='Easy', color='teal-500')
        medium, _ = Difficulty.objects.get_or_create(name='Medium', color='yellow-500')
        hard, _ = Difficulty.objects.get_or_create(name='Hard', color='red-500')
        
        # Create categories
        array, _ = Category.objects.get_or_create(name='Array', count=1848)
        string, _ = Category.objects.get_or_create(name='String', count=769)
        hash_table, _ = Category.objects.get_or_create(name='Hash Table', count=670)
        dp, _ = Category.objects.get_or_create(name='Dynamic Programming', count=567)
        math, _ = Category.objects.get_or_create(name='Math', count=561)
        sorting, _ = Category.objects.get_or_create(name='Sorting', count=441)
        greedy, _ = Category.objects.get_or_create(name='Greedy', count=404)
        linked_list, _ = Category.objects.get_or_create(name='Linked List', count=350)
        
        # Create problems
        problems_data = [
            {
                'title': 'Two Sum',
                'description': 'Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.',
                'example_input': 'nums = [2,7,11,15], target = 9',
                'example_output': '[0,1]',
                'difficulty': easy,
                'acceptance_rate': 55.1,
                'frequency': 90,
                'categories': [array, hash_table]
            },
            {
                'title': 'Add Two Numbers',
                'description': 'You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit.',
                'example_input': 'l1 = [2,4,3], l2 = [5,6,4]',
                'example_output': '[7,0,8]',
                'difficulty': medium,
                'acceptance_rate': 45.4,
                'frequency': 85,
                'categories': [math, linked_list]
            },
            {
                'title': 'Longest Substring Without Repeating Characters',
                'description': 'Given a string s, find the length of the longest substring without repeating characters.',
                'example_input': 's = "abcabcbb"',
                'example_output': '3',
                'difficulty': medium,
                'acceptance_rate': 36.3,
                'frequency': 80,
                'categories': [string, hash_table]
            },
            {
                'title': 'Median of Two Sorted Arrays',
                'description': 'Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.',
                'example_input': 'nums1 = [1,3], nums2 = [2]',
                'example_output': '2.0',
                'difficulty': hard,
                'acceptance_rate': 42.9,
                'frequency': 75,
                'categories': [array, sorting]
            },
            {
                'title': 'Longest Palindromic Substring',
                'description': 'Given a string s, return the longest palindromic substring in s.',
                'example_input': 's = "babad"',
                'example_output': '"bab" or "aba"',
                'difficulty': medium,
                'acceptance_rate': 35.3,
                'frequency': 70,
                'categories': [string, dp]
            },
            {
                'title': 'Zigzag Conversion',
                'description': 'The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows.',
                'example_input': 's = "PAYPALISHIRING", numRows = 3',
                'example_output': '"PAHNAPLSIIGYIR"',
                'difficulty': medium,
                'acceptance_rate': 50.8,
                'frequency': 65,
                'categories': [string]
            },
            {
                'title': 'Reverse Integer',
                'description': 'Given a signed 32-bit integer x, return x with its digits reversed.',
                'example_input': 'x = 123',
                'example_output': '321',
                'difficulty': medium,
                'acceptance_rate': 29.9,
                'frequency': 60,
                'categories': [math]
            },
            {
                'title': 'String to Integer (atoi)',
                'description': 'Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.',
                'example_input': 's = "42"',
                'example_output': '42',
                'difficulty': medium,
                'acceptance_rate': 18.7,
                'frequency': 55,
                'categories': [string, math]
            },
        ]
        
        for i, data in enumerate(problems_data, 1):
            categories = data.pop('categories')
            problem, created = Problem.objects.get_or_create(id=i, **data)
            if created:
                problem.categories.set(categories)
            
        # Create companies
        companies_data = [
            {'name': 'Meta', 'count': 1055},
            {'name': 'Amazon', 'count': 1180},
            {'name': 'Google', 'count': 1841},
            {'name': 'Uber', 'count': 613},
            {'name': 'Apple', 'count': 707},
            {'name': 'Bloomberg', 'count': 984},
            {'name': 'Microsoft', 'count': 1088},
            {'name': 'Oracle', 'count': 284},
            {'name': 'TikTok', 'count': 438},
            {'name': 'LinkedIn', 'count': 607},
            {'name': 'Goldman Sachs', 'count': 230},
            {'name': 'Adobe', 'count': 681},
            {'name': 'Salesforce', 'count': 143},
            {'name': 'PayPal', 'count': 112},
            {'name': 'tcs', 'count': 168},
            {'name': 'Walmart Labs', 'count': 157},
        ]
        
        for data in companies_data:
            Company.objects.get_or_create(**data)
            
        # Create study plans
        study_plans_data = [
            {'name': 'LeetCode 75', 'description': 'Merge Strings Alternately'},
            {'name': 'Introduction to Pandas', 'description': ''},
            {'name': '30 Days of JavaScript', 'description': ''},
        ]
        
        for data in study_plans_data:
            StudyPlan.objects.get_or_create(**data)
            
        self.stdout.write(self.style.SUCCESS('Successfully populated database'))