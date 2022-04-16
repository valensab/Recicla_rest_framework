from sre_parse import State
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from publications.models import Publication
from publications.api.serializers import PublicationSerializer,SearchSerializer

@api_view(['GET'])
def publication_list(request):

    if request.method == 'GET':
        publications = Publication.objects.all()
        publications_serializer = PublicationSerializer(publications,many = True)
        return Response(publications_serializer.data,status = status.HTTP_200_OK)
    
    else:
        return Response({'Método \"GET\" no permitido.'},status = status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def publication_delete(request,pk=None):
    # queryset
    publication = Publication.objects.filter(id_publication= pk).first()

    # validation
    if publication:
        if request.method == 'DELETE':
            publication.state = False
            publication.save()
            return Response({'message':'La publicación fue eliminada correctamente!'},status = status.HTTP_200_OK)

    return Response({'message':'No se ha encontrado ninguna publicación con estos datos'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def publications_availables(request, pk = None):
    if request.method == 'GET':
        publication = Publication.objects.filter(user_id= pk, state = True)
        publication_count = Publication.objects.filter(user_id= pk, state = True).count()
        publication_serializer = SearchSerializer(publication,many = True)
        if publication_count == 0:
            return Response({'message': 'No hay publicaciones realizadas'},status = status.HTTP_200_OK)
        else:
            data = {
                'Número de publicaciones': publication_count,
                "Publicaciones": publication_serializer.data,
            }
            return Response(data,status = status.HTTP_200_OK)
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def publications_made(request, pk = None):
    if request.method == 'GET':
        publication = Publication.objects.filter(user_id= pk, state = False)
        publication_count = Publication.objects.filter(user_id= pk, state = False).count()
        publication_serializer = SearchSerializer(publication,many = True)
        if publication_count == 0:
            return Response({'message': 'No hay material recolectado'},status = status.HTTP_200_OK)
        else:
            data = {
                'Número de publicaciones': publication_count,
                "Publicaciones": publication_serializer.data,
            }
            return Response(data,status = status.HTTP_200_OK)
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def publication_filter(request, pk = None):      
    if request.method == 'GET':
        publication = Publication.objects.filter(type_material= pk)  
        publication_count = Publication.objects.filter(type_material= pk).count()
        publication_serializer = SearchSerializer(publication,many = True)
        if publication_count == 0:
            return Response({'message': 'No hay publicaciones para este tipo de material'},status = status.HTTP_200_OK)
        else:
            data = {
                'Número de publicaciones': publication_count,
                "Publicaciones": publication_serializer.data,
            }
            return Response(data,status = status.HTTP_200_OK)
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)
