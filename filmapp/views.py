from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class KinoViewSet(ModelViewSet):
    queryset = Kino.objects.all()
    serializer_class = KinolarSerializer

    @action(methods=['GET', 'POST'], detail=True)
    def comments(self,request,pk):
        kino = Kino.objects.get(id=pk)
        comments = Comment.objects.filter(kino=kino)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


# class AktyorViewSet(ModelViewSet):
#     queryset = Aktyor.objects.all()
#     serializer_class = AktyorlarSerializer

class AktyorlarAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        aktyorlar = Aktyor.objects.all()
        serializer = AktyorlarSerializer(aktyorlar, many=True)
        natija = {
            "Aktyorlar ro'yhati": serializer.data
        }
        return Response(natija)

    def post(self,request):
        aktyor = request.data
        serializer = AktyorlarSerializer(data = aktyor)
        if serializer.is_valid():
            serializer.save()
            natija = {
                "xabar": "Aktyor ma'lumotlari saqlandi.",
                "Aktyor": serializer.data
            }
            return Response(natija)
        return Response({"xabar":"Xabarda xatolik bor", "Xatolik matni":serializer.errors})

class AktyorAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request, pk):
        aktyor = Aktyor.objects.get(id=pk)
        serializer = AktyorlarSerializer(aktyor, data=request.data)
        if serializer.is_valid():
            natija = {
                "Aktyor": serializer.data
            }
            return Response(natija)
        return Response({"Xabar": "Aktyor topilmadi"})

    def put(self, request, pk):
        aktyor = Aktyor.objects.get(id=pk)
        serializer = AktyorlarSerializer(aktyor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            natija = {
                "Xabar": "Aktyor ma'lumotlari muvoffaqiyatli o'zgartirildi.",
                "O'zgartirilgan Aktyor": serializer.data
            }
            return Response(natija)
        return Response({"Xabar": "Ma'lumotda xatolik bor.", "xatolik": serializer.errors})

    def delete(self,request, pk):
        aktyor = Aktyor.objects.get(id=pk)
        serializer = AktyorlarSerializer(aktyor, data=request.data)
        if serializer.is_valid():
            aktyor.delete()
            natija = {
                "Xabar": "Aktyor muvofoqqiyatli o'chirildi",
                "O'chirilgan aktyor": serializer.data
            }
            return Response(natija)
        return Response({"xabar":"Aktyor ma'lumotlari o'chirilmadi."})


class IzohlarAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        izohlar = Izohlar.objects.all()
        serializer = CommentSerializer(izohlar, many=True)
        return Response({"Izohlar":serializer.data})

    def post(self,request):
        izoh = request.data
        serializer = IzohSerialzier(data=izoh)
        if serializer.is_valid():
            serializer.save(user=request.user)
            natija = {
                "Success": serializer.data
            }
            return Response(natija)
        return Response({"Error":serializer.errors})








