from rest_framework import permissions
class IsStaffPermission(permissions.DjangoModelPermissions):

    def has_object_permission(self, request, view):
        user=request.user
        if user.is_staff:
            if user.has_perm('app.add_Product'):
                return True
            if user.has_perm('app.change_Product'):
                return True
            if user.has_perm('app.view_Product'):
                return True
            if user.has_perm('app.delete_Product'):
                return True
        return False

