#custom Permmission 
from rest_framework.permissions import BasePermission 
class Custom_Permission(BasePermission):
    #  we have alos has_object_permission
    def has_permission(self , request , view):
        if request.method == 'POST':
            # even you are login with super user you can acces it in case of post 
            return True 
        return False



# we can do also object level permission incase of blog post.  you can make the person who create only delete that post 

