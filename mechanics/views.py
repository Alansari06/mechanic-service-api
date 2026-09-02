from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Mechanic, ServiceRequest
from .serializers import MechanicSerializer, ServiceRequestSerializer


@api_view(['GET', 'POST'])
def get_mechanics(request):

    if request.method == 'GET':
        mechanics = Mechanic.objects.all()

        serializer = MechanicSerializer(mechanics, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MechanicSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_mechanic(request, id):

    try:
        mechanic = Mechanic.objects.get(id=id)
    except Mechanic.DoesNotExist:
        return Response({"error": "Mechanic not found"}, status=404)

    serializer = MechanicSerializer(mechanic)

    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
def update_mechanic(request, id):

    try:
        mechanic = Mechanic.objects.get(id=id)
    except Mechanic.DoesNotExist:
        return Response({"error": "Mechanic not found"}, status=404)

    serializer = MechanicSerializer(
        mechanic,
        data=request.data,
        partial=request.method == 'PATCH'
    )

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_mechanic(request, id):

    try:
        mechanic = Mechanic.objects.get(id=id)
    except Mechanic.DoesNotExist:
        return Response({"error": "Mechanic not found"}, status=404)

    mechanic.delete()

    return Response(status=204)

@api_view(['GET', 'POST'])
def service_requests(request):

    if request.method == 'GET':
        requests = ServiceRequest.objects.all()

        serializer = ServiceRequestSerializer(requests, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ServiceRequestSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_service_request(request, id):

    try:
        service_request = ServiceRequest.objects.get(id=id)
    except ServiceRequest.DoesNotExist:
        return Response({"error": "Service request not found"}, status=404)

    serializer = ServiceRequestSerializer(service_request)

    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
def update_service_request(request, id):

    try:
        service_request = ServiceRequest.objects.get(id=id)
    except ServiceRequest.DoesNotExist:
        return Response(
            {"error": "Service request not found"},
            status=404
        )

    if 'status' not in request.data:
        return Response(
            {"error": "Status is required"},
            status=400
        )

    allowed_status = [
        "PENDING",
        "IN_PROGRESS",
        "COMPLETED",
        "CANCELLED"
    ]

    if request.data['status'] not in allowed_status:
        return Response(
            {"error": "Invalid status"},
            status=400
        )

    service_request.status = request.data['status']
    service_request.save()

    serializer = ServiceRequestSerializer(service_request)

    return Response(serializer.data)