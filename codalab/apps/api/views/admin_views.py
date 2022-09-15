from rest_framework import (permissions, status, views)
from rest_framework.decorators import permission_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from apps.web.models import Competition


@permission_classes((permissions.IsAuthenticated,))
class GetCompetitions(views.APIView):
    """
    Gets the competitions
    """
    def get(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            raise PermissionDenied(detail="Admin only")

        competitions = []
        for competition in list(Competition.objects.order_by('id').all()):
            competitions.append({
                'id': competition.id,
                'title': competition.title,
                'creator': competition.creator.username,
                'start_date': competition.start_date,
                'end_date': competition.end_date,
                'upper_bound_max_submission_size': competition.upper_bound_max_submission_size * 1000 * 1000
            })

        return Response(competitions, status=status.HTTP_200_OK)
