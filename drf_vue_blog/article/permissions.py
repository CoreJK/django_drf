from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    仅管理员用户可以修改
    其他用户尽可以查看
    """
    def has_permission(self, request, view):
        # 对所有人允许 get, head, options 
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser
    
    
