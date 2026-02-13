from django.shortcuts import render

def home(request):
    return render(request, "home.html", {
        "name": "Nandana S",
        "title": "Computer Science Engineering Student",
        "tagline": "Web Development | Machine Learning | Python"
    })

def about(request):
    return render(request, "about.html", {
        "about": "I am a Computer Science student interested in building creative and intelligent web applications."
    })

def skills(request):
    return render(request, "skills.html")

def projects(request):
    return render(request, "projects.html", {
        "projects": [
            {
                "name": "NOESIS",
                "desc": "A technical academic platform designed for idea sharing, innovation, and collaborative learning.",
                "image": "noesis.jpg"
            },
            {
                "name": "Portfolio Website",
                "desc": "A creative and animated personal portfolio website built using Django and modern UI/UX principles.",
                "image": "portfolio.jpg"
            },
            {
                "name": "Simulator",
                "desc": "A simulation-based system developed to visualize and test real-world scenarios.",
                "image": "simulator.jpg"
            },
            {
                "name": "Diabetic Retinopathy Detection",
                "desc": "A machine learning-based healthcare system for early detection of diabetic retinopathy from retinal images.",
                "image": "diabetic.jpg"
            },
            {
                "name": "Falling Detection System",
                "desc": "A real-time fall detection system to monitor elderly individuals and send alert notifications.",
                "image": "falling.jpg"
            },
            {
                "name": "Simple Calculator",
                "desc": "A basic calculator application built using HTML, CSS, and JavaScript with a clean interface.",
                "image": "calculator.jpg"
            }
        ]
    })

def contact(request):
    return render(request, "contact.html")
