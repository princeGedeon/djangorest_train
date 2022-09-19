from rest_framework import permissions

class EditorUserPermissionsMixin():
    permission_classes=[permissions.IsAdminUser,permissions.IsAuthenticated]