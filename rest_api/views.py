from rest_framework.response import Response
from rest_api.serializers import LocationSerializer
from rest_api.models import Location
from rest_framework import status
from django.db.models import Q
from rest_framework.views import APIView


class LocationList(APIView):

    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            query = Q()
            date_param = request.query_params.get('date')
            city_param = request.query_params.get('city')
            sort = request.query_params.get('sort')
            queryset = Location.objects.all()
            if date_param:
                queryset = queryset.filter(date=date_param)
            if city_param:
                for city in city_param.split(','):
                    query.add(Q(city__icontains=city), Q.OR)
            if sort:
                queryset = queryset.order_by(sort, 'id')
            serializer = LocationSerializer(queryset.filter(query), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Location.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class LocationDetail(APIView):

    def get(self, request, pk):
        try:
            location = Location.objects.get(id=pk)
            serializer = LocationSerializer(location)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Location.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
