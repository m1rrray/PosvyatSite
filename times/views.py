from rest_framework.response import Response
from rest_framework.views import APIView

from transfer.models import Transfer


class TimesAPIView(APIView):

    def get(self, request):
        times_park = ['15:15', '15:35', '15:55', '17:35']
        times_odi = ['16:45', '17:25', '17:45', '18:25', '18:45', '19:25']
        odi = []
        for time in times_park:
            count_transfer = Transfer.objects.filter(transfer="Одинцово", departure_time=time)
            if len(count_transfer) < 46:
                odi.append(time)
        park = []
        for time in times_odi:
            count_transfer = Transfer.objects.filter(transfer="Парк Победы", departure_time=time)
            if len(count_transfer) < 46:
                park.append(time)

        return Response({"Одинцово": odi, "Парк Победы": park})
