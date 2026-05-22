from django.db import models

class SiteLogo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.name

class Banner(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()
    projects = models.IntegerField()
    clients = models.IntegerField()
    technologies = models.IntegerField()
    button_text = models.CharField(max_length=50, default="Get Started")
    image = models.ImageField(upload_to='banner/')

    def __str__(self):
        return self.heading

class WhyChoose(models.Model):
    heading = models.CharField(max_length=200)
    highlight_word = models.CharField(max_length=50, default="Best")
    image = models.ImageField(upload_to='why/')

    def __str__(self):
        return self.heading


class WhyPoint(models.Model):
    whychoose = models.ForeignKey(WhyChoose, on_delete=models.CASCADE, related_name='points')
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='icons/')

    def __str__(self):
        return self.title

class WorkProcess(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='workprocess/')

    def __str__(self):
        return self.heading

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')
    review = models.TextField()
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.name

class Project(models.Model):
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return f"Project {self.id}"

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class AboutUs(models.Model):
    image = models.ImageField(upload_to='aboutus/')

    def __str__(self):
        return "About Us Image"

class VisionMission(models.Model):
    image = models.ImageField(upload_to='vision_mission/')

    def __str__(self):
        return "Vision/Mission Image" 

class WebPage(models.Model):
    heading = models.CharField(max_length=200, default="Web Development")
    description = models.TextField()
    image = models.ImageField(upload_to='web/')

    def __str__(self):
        return self.heading

class WorkStage(models.Model):
    image = models.ImageField(upload_to='work_stages/')

    def __str__(self):
        return f"Stage {self.id}"

class StaticSection(models.Model):
    image = models.ImageField(upload_to='static_section/')

    def __str__(self):
        return "Static Section Image"

class DynamicSection(models.Model):
    image = models.ImageField(upload_to='dynamic_section/')

    def __str__(self):
        return "Dynamic Section Image"

class EcommerceSection(models.Model):
    image = models.ImageField(upload_to='ecommerce_section/')

    def __str__(self):
        return "Ecommerce Section Image"

class Plan(models.Model):
    PLAN_CHOICES = [
        ('basic', 'Basic Plan'),
        ('standard', 'Standard Plan'),
        ('premium', 'Premium Plan'),
    ]

    plan_type = models.CharField(max_length=20, choices=PLAN_CHOICES)
    price = models.IntegerField()

    def __str__(self):
        return self.plan_type 

class SoftwarePage(models.Model):
    image = models.ImageField(upload_to='software/')

    def __str__(self):
        return "Software Page Image"  

class NativeAppPage(models.Model):
    image = models.ImageField(upload_to='nativeapp/')

    def __str__(self):
        return "Native App Image"                     

class HybridApp(models.Model):
    image = models.ImageField(upload_to='hybrid/')

    def __str__(self):
        return "Hybrid App Image"

class ProgressiveWebApp(models.Model):
    image = models.ImageField(upload_to='pwa/')

    def __str__(self):
        return "PWA Image"

class WearableEmbedded(models.Model):
    image = models.ImageField(upload_to='wearable/')

    def __str__(self):
        return "Wearable & Embedded Image"

class DigitalMarketing(models.Model):
    image = models.ImageField(upload_to='digital_marketing/')

    def __str__(self):
        return "Digital Marketing Image"

class SEOSection(models.Model):
    image = models.ImageField(upload_to='seo_images/')

    def __str__(self):
        return f"SEO Image {self.id}"  

class SocialMediaSection(models.Model):
    image = models.ImageField(upload_to='social_media/')

    def __str__(self):
        return "Social Media Section"              

class ContentCreation(models.Model):
    image = models.ImageField(upload_to='content_creation/')

    def __str__(self):
        return "Content Creation"

class StrategyPlan(models.Model):
    image = models.ImageField(upload_to='strategy_plan/')

    def __str__(self):
        return "Strategy Plan"

class GoogleAnalytics(models.Model):
    image = models.ImageField(upload_to='google_analytics/')

    def __str__(self):
        return "Google Analytics"   

class EmailMarketing(models.Model):
    image = models.ImageField(upload_to='email_marketing/')

    def __str__(self):
        return "Email Marketing Image"    

class VideoMarketing(models.Model):
    image = models.ImageField(upload_to='video_marketing/')

    def __str__(self):
        return "Video Marketing Image"

class GoogleAds(models.Model):
    image = models.ImageField(upload_to='google_ads/')

    def __str__(self):
        return "Google Ads Image"

class DigitalPlan(models.Model):
    PLAN_CHOICES = (
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    )

    plan_type = models.CharField(max_length=20, choices=PLAN_CHOICES)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.plan_type} - ₹{self.price}"
