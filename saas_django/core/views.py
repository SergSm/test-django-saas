from django.core import exceptions


class CompanySafeViewMixin:
    """
    Mixin to be used with views that ensures that models are related
    to the company during creation
    and are querysets are filtered for read operations
    """
    def get_query(self):
        quyeryset = super().get_queryset(

        if not self.request.user.is_authenticated: