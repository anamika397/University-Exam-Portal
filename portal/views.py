from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ExamForm

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def fill_exam_form(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        course = request.POST['course']
        year = request.POST['year']
        address = request.POST['address']
        phone_number = request.POST['phone_number']

        ExamForm.objects.create(
            full_name=full_name,
            course=course,
            year=year,
            address=address,
            phone_number=phone_number
        )

        return render(request, 'success.html')

    return render(request, 'exam_form.html')