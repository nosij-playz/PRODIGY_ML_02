from django.shortcuts import render
from .segment import SegmenterWrapper

segmenter = SegmenterWrapper()

def index(request):
    result = None
    if request.method == 'POST':
        gender = request.POST.get('gender')
        age = int(request.POST.get('age'))
        income = float(request.POST.get('income'))
        spending_score = float(request.POST.get('spending_score'))  # matches the form field name now

        result = segmenter.predict(gender, age, income, spending_score)

    return render(request, 'segmenterapp/index.html', {'result': result})
