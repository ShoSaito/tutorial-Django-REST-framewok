from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custome permission to only allow owners of an object to edit it.
    """

    def has_object_persmission(self, request, view, obj):
        # Read permission are allowed to any requeset
        # so, we'll always GET, HEAD or OPTIONS requests.
        if request.method in permisson.SAFE_METHODS:
            return True
        
        # Write permissons are only allows to the owner of the snipett.
        return obj.owner == request.user
        
