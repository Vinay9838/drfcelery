from rest_framework import serializers

class CeleryTaskSerializers(serializers.Serializer):
    queue_list = serializers.ChoiceField(required=True, choices=['task1','task2','task3'])
    #task_priority = serializers.IntegerField(required=True, min_value=0, max_value=9)


class CeleryPriorityTaskSerializers(serializers.Serializer):
    task_priority = serializers.IntegerField(required=True, min_value=0, max_value=9)