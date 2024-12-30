from rest_framework.permissions import BasePermission


class GlobalPermissions(BasePermission):

    def has_permission(self, request, view):
        app_permission_model = self.__get_app_permission_model(request.method, view)
        if not app_permission_model:
            return False
        return request.user.has_perm(app_permission_model)
    
    def __get_app_permission_model(self, method, view):
        try:
            app_label = view.queryset.model._meta.app_label
            permission = self.action(method)
            model = view.queryset.model._meta.model_name
            return f'{app_label}.{permission}_{model}'
        except AttributeError:
            return None

    def action(self, method):
        methods = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'DELETE': 'delete'
        }
        return methods.get(method, '')

    # APP / PERMISSION/ MODEL