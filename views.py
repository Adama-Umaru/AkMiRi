"""
michael.views

This module contains the view functions for the 'michael' app.
"""

from django.shortcuts import render


def index(request):
    """
    Render the 'index.html' template for the index view.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered template response.
    """
    return render(request, 'index.html')
