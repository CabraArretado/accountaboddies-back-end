from django.contrib.auth.models import User
from accountaboddiesapi.models import Group, Account

# Get the Account User Id of the request
def getUserId(request):
    """Get the user id"""

    user = User.objects.get(pk=request.user.id)
    account = Account.objects.get(pk=user.customer.id)
    return account