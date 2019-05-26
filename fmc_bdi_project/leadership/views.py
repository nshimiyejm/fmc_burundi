from django.shortcuts import render, get_object_or_404
from .models import Profile_Role

# Display Home page 
def index(request): 
    return render(request, 'leadership/index.html')

# Dispplay profiles 
def profiles(request):
    '''
    Will be used to display the profiles of the leaders in church
    ''' 
    # Pull all the leaders from the database 
    all_leaders = Profile_Role.objects
    return render(request, 'leadership/profile.html', {'leaders' : all_leaders})

# Display the full bio of the leader
def bio(request, leader_id):
    leader_bio = get_object_or_404(Profile_Role, pk=leader_id)
    return render(request, 'leadership/bio.html', {'leader':leader_bio})


    
