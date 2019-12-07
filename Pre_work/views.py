from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import ProjectList, ProjectDetails
import re

def dfs(u, visited, graph, stack, allwork_virtual):
    visited[u] = 1
    for v in graph[u]:
        v = allwork_virtual.index(v)
        if not visited[v]:
            dfs(v, visited, graph, stack, allwork_virtual)

    stack.append(u)

def top_sort(graph, visited, stack, allwork_virtual):
    for v in range(len(graph)):
        if not visited[v]:
            dfs(v, visited, graph, stack, allwork_virtual)

def toposort(Graph, stack, stackLateStart, allwork_virtual, earlyStartList, inDegree):
    while stack:
        x = stack.pop()
        stackLateStart.append(x)
        for v in Graph[x]:
            v = allwork_virtual.index(v)
            inDegree[v] -= 1
            if not inDegree[v]:
                stack.append(v)
            try:
                if earlyStartList[x]+ProjectList.objects.get(pk=allwork_virtual[x]).man_hour > earlyStartList[v]:
                    earlyStartList[v] = earlyStartList[x]+ProjectList.objects.get(pk=allwork_virtual[x]).man_hour
            except:
                    pass

def index(request):
    return HttpResponse("Hello, world. You're at the firstapp index.")

def handledata(request):
    startwork = []
    finalwork = []
    allwork = []
    order = 0
    # nofinalwork = []

    for x in ProjectList.objects.all():
        if not x.pre_work:
            startwork.append(x.id)
        else:
            mask = list(map(int, re.findall(r'(\d+)', x.pre_work, flags=0)))
            for y in mask:
                    finalwork.append(y)
        allwork.append(x.id)

    Graph = []
    Graph.append(startwork)
    for x in ProjectList.objects.all():
        chain = []
        for y in list(set(allwork)-set(startwork)):
            for z in list(map(int, re.findall(r'(\d+)', ProjectList.objects.get(pk=y).pre_work, flags=0))):
                if z == x.id:
                    chain.append(y)
        Graph.append(chain)

    minId = min(allwork)
    maxId = max(allwork)
    for x in Graph:
        if not x:
            x.append(maxId+1)
            order += 1
    
    Graph.append([])
    allwork_virtual=[minId-1]
    for x in allwork:
        allwork_virtual.append(x)
    allwork_virtual.append(maxId+1)

    # toposort
    # stack = []
    # visited = [0 for x in range(len(allwork_virtual))]

    # top_sort(Graph, visited, stack, allwork_virtual)

    # sort_list = []
    # for x in allwork_virtual:
    #     sort_list.append(allwork_virtual[stack.pop()])

    # toposort_2
    # inDegree = [len(x) for x in Graph] 
    inDegree = [0]
    for x in ProjectList.objects.all():
        try:
            inDegree.append(len(re.findall(r'(\d+)', x.pre_work, flags=0)))
        except TypeError:
            inDegree.append(0)
        
    inDegree.append(order)
    for x in startwork:
        inDegree[allwork_virtual.index(x)] += 1
    earlyStartList = [0 for x in range(len(Graph))]
    stack = [0]
    stackLateStart = []
    toposort(Graph, stack, stackLateStart, allwork_virtual, earlyStartList, inDegree)
    
    # CriticalPath
    lateStartList = [earlyStartList[allwork_virtual.index(maxId+1)] for x in allwork_virtual]
    while stackLateStart:
        x = stackLateStart.pop()
        for y in Graph[x]:
            try:
                if lateStartList[allwork_virtual.index(y)]-ProjectList.objects.get(pk=y).man_hour < lateStartList[x]:
                    lateStartList[x] = lateStartList[allwork_virtual.index(y)]-ProjectList.objects.get(pk=y).man_hour
            except:
                pass
    # for x in allwork_virtual:
    #     sort_list.append(allwork_virtual[stackLateStart.pop()])

    # Earlystart
    # p = ProjectList(project_name='end')
    # p.save()
    # for x in allwork_virtual[1:]:
    #     if not ProjectList.objects.get(pk=x).pre_work:
    #         Earlystart = 0
    #     else:
    #         Earlystart = [ProjectList.objects.get(pk=x).man_hour for x in list(map(int, re.findall(r'(\d+)', ProjectList.objects.get(pk=x).pre_work, flags=0)))]
    #     try:
    #         ProjectList.objects.get(pk=x).projectdetails_set.create(ES=Earlystart)
    #     except:
    #         ProjectList.objects.get(pk=x).projectdetails_set.all()[0]()
        
    #     pass

    # nofinalwork = [str(i) for i in list(set(allwork) - set(finalwork))]
    # pattern = '-'
    # nofinalwork = pattern.join(nofinalwork)
    context = {
        'Graph': Graph, 
        'allwork': allwork, 
        'startwork': startwork,
        'finalwork': finalwork,
        'allwork_virtual': allwork_virtual,
        'stackLateStart': inDegree,
        'earlyStartList': earlyStartList,
        'lateStartList': lateStartList,
        }

    return render(request, 'handle.html', context)