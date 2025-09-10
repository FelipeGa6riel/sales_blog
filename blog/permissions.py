from django.contrib.auth.models import User

User.add_to_class(
    "can_access_profile_admin",
    lambda self: self.has_perm("blog.can_access_profile_admin"),
)
