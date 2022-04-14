from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        'my_list': [
            {
               "restaurant_name": "KFC",
               "food_type": "Fried Chicken",
            },
            {
               "restaurant_name": "Taco Street",
               "food_type": "Mexican Food",
            },
            {
               "restaurant_name": "Lavan",
               "food_type": "Indian Food",
            },

        ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        'my_object': {
            "restaurant_name": "Meme's Curry",
            "food_type": "Japanese Curry",
        }
    }
    return render(request, 'detail.html', context)
