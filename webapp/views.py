from rest_framework.views import APIView
from rest_framework.response import Response  
from rest_framework import status, parsers
from drf_spectacular.utils import extend_schema,OpenApiResponse

from .serializers import CeleryTaskSerializers, CeleryPriorityTaskSerializers
from .tasks import counter_task



# Create your views here.

class CeleryTaskViewSet(APIView):
    parser_classes = [parsers.FormParser]
    
    @extend_schema(
        summary='Celery Tasks',
        request= CeleryTaskSerializers,
        responses={
            200: OpenApiResponse(description='Json Response'),
            400: OpenApiResponse(description='Validation error')
        }
    )
    def post(self,request): 
        serializer = CeleryTaskSerializers(data=request.data)
        if not serializer.is_valid():
            return Response({"errors":serializer.errors}, status.HTTP_400_BAD_REQUEST)
        queue_name = serializer.validated_data['queue_list']
        task = counter_task.apply_async(queue=queue_name)
        return Response({"message":"Celery task started", "task_id":task.id},status.HTTP_200_OK)
    

class CeleryPriorityTaskViewSet(APIView):
    parser_classes = [parsers.FormParser]
    
    @extend_schema(
        summary='Celery Priority Tasks',
        request= CeleryPriorityTaskSerializers,
        responses={
            200: OpenApiResponse(description='Json Response'),
            400: OpenApiResponse(description='Validation error')
        }
    )
    def post(self,request): 
        serializer = CeleryPriorityTaskSerializers(data=request.data)
        if not serializer.is_valid():
            return Response({"errors":serializer.errors}, status.HTTP_400_BAD_REQUEST)
        task_priority = serializer.validated_data['task_priority']
        queue_name = 'priority_queue'
        task = counter_task.apply_async(queue=queue_name,priority=task_priority)
        return Response({"message":"Celery task started", "task_id":task.id},status.HTTP_200_OK)
    