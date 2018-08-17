from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponseServerError
from rest_framework.views import APIView
from django.views import generic
from rest_framework.response import Response
from rest_framework import status
from .models import ChildGrantDate
from .tables import ChildGrantDateTable
from .serializers import DateSerializer, CGSuccessSerializer
from .date_converter import NepaliDateConverter
import datetime
from django.core.files.storage import default_storage
import os
from django.conf import settings
from django_tables2 import SingleTableView
from django_tables2.export.views import ExportMixin


class AD_BS(APIView):

    def get(self, request):
        ad = request.GET.get('date')
        dc = NepaliDateConverter()
        ad = tuple(map(int, ad.split('-')))
        bs = dc.ad2bs(ad)
        datestr = '-'.join([str(x).zfill(2) for x in bs])
        date = {'date_type': 'BS', 'date': datestr, 'year': bs[0], 'month': bs[1], 'day': bs[2]}
        serializer = DateSerializer(date, many = False)
        return Response(serializer.data)

    def post(self):
        pass

class BS_AD(APIView):

    def get(self, request):
        bs = request.GET.get('date')
        dc = NepaliDateConverter()
        bs = tuple(map(int, bs.split('-')))
        ad = dc.bs2ad(bs)
        datestr = '-'.join([str(x).zfill(2) for x in ad])
        date = {'date_type': 'AD', 'date': datestr, 'year': ad[0], 'month': ad[1], 'day': ad[2]}
        serializer = DateSerializer(date, many = False)
        return Response(serializer.data)

    def post(self):
        pass


class ChildGrant(APIView):

    def get(self, request):
        address_group = request.GET.get('address_group')
        dist_date_np = request.GET.get('dist_date_np')
        dist_date_en = request.GET.get('dist_date_en')
        final_confirmation = request.GET.get('final_confirmation')
        if address_group is None:
            return HttpResponseServerError()
        cg, _ = ChildGrantDate.objects.get_or_create(address_group=address_group)
        cg.address_group = address_group
        cg.dist_date_np = dist_date_np
        cg.dist_date_en = dist_date_en[:10]
        cg.final_confirmation = final_confirmation
        cg.last_updated_date = datetime.date.today()
        cg.save()
        msg = {'message': 'Date received'}
        serializer = CGSuccessSerializer(msg, many = False)
        return Response(serializer.data)

    def post(self, request):
        pass

class ChildGrantDateList(ExportMixin, SingleTableView):
    model = ChildGrantDate
    table_class = ChildGrantDateTable
    
