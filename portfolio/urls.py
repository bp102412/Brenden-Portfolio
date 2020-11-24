"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import jobs.views, resume.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^tracking/', include('tracking.urls')), #for user tracking app, can go to /tracking/
    path('admin/', admin.site.urls), #/admin page, can only be used with credentials. Admin page is generated automatically, can over ride templates. May do this later.
    path('resume/',include('resume.urls')), #/resume references resume urls in resume directory
    path('', jobs.views.home, name='home'), #/ home page
    path('language/<int:lang_id>', jobs.views.lang_detail, name='language details'), #/language/(langugae primary key) , language detail page
    path('language/framework/<int:frame_id>', jobs.views.frame_detail, name='framework details'), #language/framework/(framework primary key) , framework details page
    path('language/project/<int:project_id>', jobs.views.project_detail, name='project details'), #language/project/(project pk) , project no framework details page
    path('language/framework/project/<int:project_id>', jobs.views.framework_project_detail, name='framework project details'), #/language/framework/project/(project PK), project with framework detail page
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #you could technically navigate to certain static files in the browser if you know the path
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
