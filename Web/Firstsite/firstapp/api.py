from firstapp.models import ProjectList
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def project(requst):
    data = []
    queryset = ProjectList.objects.all().order_by('-id')
    for i in queryset:
        q_tmp = {
            'project_name': i.project_name,
            'pre_work': i.pre_work,
            'man_hour': i.man_hour,
            'id': i.id,
        }
        data.append(q_tmp)
    return Response(json.dumps(data))