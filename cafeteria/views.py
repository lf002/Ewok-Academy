from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def landing(request):
    """Public landing page for the Endor Ewok Academy."""
    return render(request, 'cafeteria/landing.html')


@login_required
def secret_menu(request):
    """
    The Secret Lunch Menu — classified Ewok cuisine.
    @login_required ensures only authenticated users can access this view.
    If not logged in, Django automatically redirects to LOGIN_URL.
    """
    menu_items = [
        {
            'name': 'Roasted Gorax Ribs',
            'description': 'Slow-roasted over an open fire pit, glazed with sweet Endorian honey-sap.',
            'emoji': '🍖',
        },
        {
            'name': 'Endorian Sunberry Stew',
            'description': 'A hearty stew packed with golden sunberries and wild forest herbs.',
            'emoji': '🍲',
        },
        {
            'name': 'Logray\'s Mushroom Skewers',
            'description': 'Giant moon-mushrooms skewered and seasoned with the Medicine Man\'s secret spice blend.',
            'emoji': '🍢',
        },
        {
            'name': 'Wicket\'s Acorn Bread',
            'description': 'Freshly baked acorn-flour loaves with a crispy bark crust — a village favorite.',
            'emoji': '🍞',
        },
        {
            'name': 'Bantha Milk Pudding',
            'description': 'Creamy dessert made from smuggled Bantha milk, topped with crushed starberries.',
            'emoji': '🍮',
        },
    ]
    return render(request, 'cafeteria/secret_menu.html', {'menu_items': menu_items})
