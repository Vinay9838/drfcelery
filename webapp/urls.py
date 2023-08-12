from django.urls import path

from webapp import views

urlpatterns = [
 path('celery-task',views.CeleryTaskViewSet.as_view(),name='celery_task'),
 path('celery-priority-task',views.CeleryPriorityTaskViewSet.as_view(),name='celery_pririty_task')

]
