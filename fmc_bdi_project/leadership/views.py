from django.shortcuts import render, get_object_or_404
from .models import Profile_Role, Church_Background, Church_Mission, Church_Vision

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

# Display information on the church history 
def history(request): 
    all_history = Church_Background.objects.all()
    all_mission = Church_Mission.objects.all()
    all_vision  = Church_Vision.objects.all()
    
    return render(request, 'leadership/about.html', {'about': all_history,'mission': all_mission, 'vision': all_vision })

# Display information about the church


    
