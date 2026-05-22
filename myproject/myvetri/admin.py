from django.contrib import admin
from .models import SiteLogo, Banner, WhyChoose, WhyPoint, WorkProcess, Testimonial, Project, FAQ, AboutUs, VisionMission, WebPage, WorkStage, StaticSection, DynamicSection, EcommerceSection, Plan, SoftwarePage, NativeAppPage, HybridApp, ProgressiveWebApp, WearableEmbedded, DigitalMarketing, SEOSection, SocialMediaSection, ContentCreation, StrategyPlan, GoogleAnalytics, EmailMarketing, VideoMarketing, GoogleAds, DigitalPlan

admin.site.register(SiteLogo)
admin.site.register(Banner)

class WhyPointInline(admin.TabularInline):
    model = WhyPoint
    extra = 1

class WhyChooseAdmin(admin.ModelAdmin):
    inlines = [WhyPointInline]

class ProjectAdmin(admin.ModelAdmin):
    fields = ['image']  # only show image

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)

class StaticSectionAdmin(admin.ModelAdmin):
    fields = ['image']  # only image upload

class DynamicSectionAdmin(admin.ModelAdmin):
    fields = ['image']  # only image upload

class EcommerceSectionAdmin(admin.ModelAdmin):
    fields = ['image']  # only image upload 

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['plan_type', 'price']       

admin.site.register(DynamicSection, DynamicSectionAdmin)    
admin.site.register(StaticSection, StaticSectionAdmin) 
admin.site.register(EcommerceSection, EcommerceSectionAdmin)   

admin.site.register(FAQ, FAQAdmin)    
admin.site.register(Project, ProjectAdmin)
admin.site.register(WhyChoose, WhyChooseAdmin)
admin.site.register(WorkProcess)
admin.site.register(Testimonial)
admin.site.register(AboutUs)
admin.site.register(VisionMission)
admin.site.register(WebPage)
admin.site.register(WorkStage)
admin.site.register(SoftwarePage)
admin.site.register(NativeAppPage)
admin.site.register(HybridApp)
admin.site.register(ProgressiveWebApp)
admin.site.register(WearableEmbedded)
admin.site.register(DigitalMarketing)
admin.site.register(SEOSection)
admin.site.register(SocialMediaSection)
admin.site.register(ContentCreation)
admin.site.register(StrategyPlan)
admin.site.register(GoogleAnalytics)
admin.site.register(EmailMarketing)
admin.site.register(VideoMarketing)
admin.site.register(GoogleAds)
admin.site.register(DigitalPlan)