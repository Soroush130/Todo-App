from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import WorkSerializer, TypeWorkSerializer
from app_work.models import Work, TypeWork
from rest_framework.permissions import IsAuthenticated


class WorkViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        works = Work.objects.filter(user=request.user)
        serializer = WorkSerializer(works, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = WorkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        work = Work.objects.get(pk=pk, user=request.user)
        if work.user == request.user:
            work.delete()
        return Response({'Message': 'Delete Work'}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def finish_work(self, request, pk):
        work = get_object_or_404(Work.objects.filter(user=request.user), pk=pk)
        work.is_finished = True
        work.save()
        return Response({"Message": "The work is finished"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def calc_percent_work(self, request):
        year, month, day = request.data['date'].split('-')
        works = Work.objects.filter(user=request.user, created__year=int(year), created__day=int(day),
                                    created__month=int(month))
        count_all_works = works.count()
        count_is_finished_works = works.filter(is_finished=True).count()
        percent = int((count_is_finished_works / count_all_works) * 100)
        return Response({'percent': percent})

    @action(detail=False, methods=['get'])
    def compare_daily_performance(self, request):
        context = {}
        date = set()

        works = Work.objects.filter(user=request.user)

        for work in works: date.add(f"{work.created.year}-{work.created.month}-{work.created.day}")

        for d in date:
            year, month, day = d.split('-')
            works_in_day = Work.objects.filter(created__year=year, created__month=month, created__day=day)
            count_work_all = works_in_day.count()
            count_work_finished = works_in_day.filter(is_finished=True).count()
            count_work_not_finished = count_work_all - count_work_finished
            context[d] = [count_work_all, count_work_finished, count_work_not_finished]

        return Response(context)


class TypeWorkViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = TypeWorkSerializer(TypeWork.objects.all(), many=True)
        return Response(serializer.data)
