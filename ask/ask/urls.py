"""ask URL Configuration

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
from django.conf.urls import url 
import qa.views as qa


urlpatterns = [
   url(r'^$', qa.new, name='new'),                                                              
#    url(r'^login/.*$', qa.login, name='login'),                                    
#    url(r'^signup/.*', qa.signup, name='signup'),                                   
   url(r'^question/(?P<id>[0-9]+)/$', qa.question, name='question'),                 
#    url(r'^ask/.*', qa.ask, name='ask'),                                         
   url(r'^popular/.*', qa.popular, name='popular'),                                 
   url(r'^new/.*', qa.new, name='new'),                                          
]



# urlpatterns = [
#     path('admin/', admin.site.urls),
    
#     path('', qa.index),
#     path('popular/', qa.popular),
#     path('question/<int:id>/', qa.question),
    
#     path('test/', qa.test),
    
#     path('login/', qa.test),
#     path('ask/', qa.test),    
#     path('new/', qa.test),
#     path('signup/', qa.test),
# ]
