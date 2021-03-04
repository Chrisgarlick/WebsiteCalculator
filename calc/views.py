from django.shortcuts import render
from .forms import CalculatorForm


def HomePage(request):
    if request.method == 'POST':
        num1 = request.POST['number_one']
        num2 = request.POST['number_two']
        operator = request.POST['operator']

        if operator == '+':
            result = int(num1) + int(num2)
        elif operator == '-':
            result = int(num1) - int(num2)
        elif operator == '*':
            result = int(num1) * int(num2)
        elif operator == '/':
            result = int(num1) / int(num2)
        
        return render(request, 'calc/home.html', {'result': result})
    return render(request, 'calc/home.html')