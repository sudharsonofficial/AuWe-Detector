import json
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request: HttpRequest) -> HttpResponse:
    """
    View function to render the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    return render(request, "index.html")


@csrf_exempt
def add_city(request: HttpRequest) -> HttpResponse:
    """
    View function to handle adding a new city's weather data.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: An HTTP response.
    """
    if request.method == "POST":
        try:
            location = request.POST.get('location')
            min_temp = float(request.POST.get('min_temp'))
            max_temp = float(request.POST.get('max_temp'))
            email = request.POST.get('email')

            new_data = {
                'name': location,
                'min-temp': min_temp,
                'max-temp': max_temp
            }

            # Open and update the JSON data file
            with open('data.json', 'r+') as file:
                data = json.load(file)

                if not data:
                    data["location"] = [new_data]
                    data["email"] = email
                else:
                    data["location"].append(new_data)

                file.seek(0)
                json.dump(data, file, indent=4)

            print("Data added successfully")

        except Exception as e:
            print(e)
            return HttpResponse("Something unexpected happened. Please try again!")

        return HttpResponse()

    else:
        return render(request, 'index.html')
