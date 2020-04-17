from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# note: differeniate the funtion name and package name here
# UserCreateForm vs. UserCreationForm
class UserCreateForm(UserCreationForm):
    # Meta: declare the fields that wants user to fill
    class Meta:
        fields = ("username", "email", "password1", "password2")
        # import from contrib.auth
        model = get_user_model()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
