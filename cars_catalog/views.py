from django.shortcuts import render
# Added import
from .models import CarModel, CarInstance, CarColor, CarConfiguration, Manufacturer


# Create your views here.


def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_manufacturers = Manufacturer.objects.all().count()
    num_car_configurations = CarConfiguration.objects.all().count()
    num_car_instances = CarInstance.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_manufacturers': num_manufacturers, 'num_car_configurations': num_car_configurations,
                 'num_car_instances': num_car_instances, 'num_visits': num_visits},
    )
