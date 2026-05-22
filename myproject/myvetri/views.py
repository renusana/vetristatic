from django.shortcuts import render
from .models import SiteLogo, Banner, WhyChoose, WorkProcess, Testimonial, Project, FAQ, AboutUs, VisionMission, WebPage, WorkStage, StaticSection, DynamicSection, EcommerceSection, Plan, SoftwarePage, NativeAppPage, HybridApp, ProgressiveWebApp, WearableEmbedded, DigitalMarketing, SEOSection, SocialMediaSection, ContentCreation, StrategyPlan, GoogleAnalytics, EmailMarketing, VideoMarketing, GoogleAds, DigitalPlan

def home(request):
    logo = SiteLogo.objects.first()
    banner = Banner.objects.first()
    why = WhyChoose.objects.first()
    work = WorkProcess.objects.first()
    testimonials = Testimonial.objects.all()
    projects = Project.objects.all()
    faqs = FAQ.objects.all()

    return render(request, 'home.html', {
        'logo': logo,
        'banner': banner,
        'why': why,
        'work': work,
        'testimonials': testimonials,
        'projects': projects,
        'faqs': faqs,
    })

def aboutus(request):
    logo = SiteLogo.objects.first()
    about = AboutUs.objects.first() 
    vm_images = VisionMission.objects.all()  # Fetch all VisionMission entries  

    return render(request, 'aboutus.html', {
        'logo': logo,
        'about': about,
        'vm_images': vm_images
    })

def web(request):
    logo = SiteLogo.objects.first()
    web_data = WebPage.objects.first()
    stages = WorkStage.objects.all()  # Fetch all WorkStage entries
    static_section = StaticSection.objects.first() 
    dynamic_section = DynamicSection.objects.first() 
    ecommerce_section = EcommerceSection.objects.first() 
    plans = Plan.objects.all()  # Fetch all Plan entries

    return render(request, 'web.html', {
        'logo': logo,
        'web_data': web_data,
        'stages': stages,
        'static_section': static_section,
        'dynamic_section': dynamic_section,
        'ecommerce_section': ecommerce_section,
        'plans': plans
    })    

def software(request):
    logo = SiteLogo.objects.first()
    software_data = SoftwarePage.objects.first()
    native_data = NativeAppPage.objects.first()
    hybrid_data = HybridApp.objects.first()
    pwa_data = ProgressiveWebApp.objects.first()
    wearable_data = WearableEmbedded.objects.first()

    return render(request, 'software.html', { 
        'logo': logo, 
        'software_data': software_data, 
        'native_data': native_data, 
        'hybrid_data': hybrid_data,
        'pwa_data': pwa_data,
        'wearable_data': wearable_data
    })

def digital_marketing(request):
    logo = SiteLogo.objects.first()
    data = DigitalMarketing.objects.first()
    seo_image = SEOSection.objects.first()  # Fetch the first SEOSection entry
    social_image = SocialMediaSection.objects.first()
    content_image = ContentCreation.objects.first()
    strategy_image = StrategyPlan.objects.first()
    google_image = GoogleAnalytics.objects.first()
    email_image = EmailMarketing.objects.last()
    video_image = VideoMarketing.objects.last()
    ads_image = GoogleAds.objects.last()
    plans = DigitalPlan.objects.all()

    return render(request, 'digital.html', {
        'logo': logo,
        'data': data,
        'seo_image': seo_image,
        'social_image': social_image,
        'content_image': content_image,
        'strategy_image': strategy_image,
        'google_image': google_image,
        'email_image': email_image,
        'video_image': video_image,
        'ads_image': ads_image,
        'plans': plans
    })