from django.shortcuts import render
from .models import DescriptionRequest

# Create your views here.

def description_generator(request):
    if request.method == 'POST':
        keywords = request.POST.get('keywords')
        # Placeholder: In real use, call AI API here
        generated = f"Generated description for: {keywords}"
        obj = DescriptionRequest.objects.create(keywords=keywords, generated_description=generated)
        return render(request, 'ai_assistant/description_result.html', {'description': generated})
    return render(request, 'ai_assistant/description_form.html')
