from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import DescriptionRequest
import random

# Create your views here.

def get_templates_for_style(style):
    templates = {
        'professional': [
            "Discover the best in {keywords} with our latest collection.",
            "Our {keywords} are designed for excellence and reliability.",
            "Experience top-tier {keywords} trusted by professionals.",
        ],
        'friendly': [
            "Hey there! Check out our awesome {keywords} just for you!",
            "You'll love our {keywords}—they're made to make you smile!",
            "Looking for something cool? Our {keywords} have you covered!",
        ],
        'persuasive': [
            "Don't miss out on our exclusive {keywords}—get yours today!",
            "Transform your life with our unbeatable {keywords}.",
            "Join thousands who chose our {keywords} and never looked back!",
        ],
        'fun': [
            "Zap! Pow! Our {keywords} are here to save your day!",
            "Make every moment fun with our quirky {keywords}.",
            "Why be boring? Our {keywords} bring the party!",
        ],
    }
    return templates.get(style, templates['professional'])

def description_generator(request):
    if request.method == 'POST':
        keywords = request.POST.get('keywords')
        style = request.POST.get('style', 'professional')
        templates = get_templates_for_style(style)
        generated = random.choice(templates).format(keywords=keywords)
        obj = DescriptionRequest.objects.create(keywords=keywords, generated_description=generated)
        history = DescriptionRequest.objects.order_by('-created_at')
        return render(request, 'ai_assistant/description_result.html', {
            'description': generated,
            'keywords': keywords,
            'style': style,
            'history': history
        })
    history = DescriptionRequest.objects.order_by('-created_at')
    return render(request, 'ai_assistant/description_form.html', {'history': history})

def regenerate_description(request):
    if request.method == 'POST':
        keywords = request.POST.get('keywords')
        style = request.POST.get('style', 'professional')
        templates = get_templates_for_style(style)
        generated = random.choice(templates).format(keywords=keywords)
        obj = DescriptionRequest.objects.create(keywords=keywords, generated_description=generated)
        history = DescriptionRequest.objects.order_by('-created_at')
        return render(request, 'ai_assistant/description_result.html', {
            'description': generated,
            'keywords': keywords,
            'style': style,
            'history': history
        })
    return redirect('description_generator')

def delete_description(request, pk):
    desc = get_object_or_404(DescriptionRequest, pk=pk)
    desc.delete()
    return redirect('description_generator')

def download_description(request, pk):
    desc = get_object_or_404(DescriptionRequest, pk=pk)
    response = HttpResponse(desc.generated_description, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename=description_{pk}.txt'
    return response
