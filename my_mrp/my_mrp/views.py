"""Define the My MRP home view."""
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from django.views.generic.base import TemplateView
from vehicle_quote.models import VehicleQuote


# Generates Graph based on Data.
def createGraph():
    """Creates Visual for most popular models quoted."""
    vehicles = {}
    colors = {}
    car_models = VehicleQuote.objects.all()
    for car in [model.model_name.model_name for model in car_models]:
        if car not in vehicles:
                vehicles[car] = 1
        else:
            vehicles[car] += 1
    try:
        # Uses Plotly's API
        plotly.tools.set_credentials_file(username='kiirby', api_key='TdfP7ccHINP4BI76EDNj')
        trace = go.Pie(
            labels=list(vehicles.keys()),
            values=list(vehicles.values())
        )
        # GRAPH DIMENSION.
        layout = go.Layout(
            title='Most Quoted Models',
            width=800, height=640,
            paper_bgcolor='rgb(27, 32, 46)',
            font=dict(color='rgb(52, 156, 134)', size=30)
        )
        graph = go.Figure(data=[trace], layout=layout)
        # Creates graph and saves it to the project.
        print('-' * 45)
        py.image.save_as(graph, filename='my_mrp/static/popular_models.png')
        py.image.ishow(graph)
    except:
        print('[!] FATAL ERROR')
        return False
    finally:
        print('[*] Finished Executing PLOTLY/DB Queries.')
        print('-' * 45)


class HomeView(TemplateView):
    """Make the HomeView class."""
    template_name = 'generic/home.html'
    context_object_name = 'quotes'

    def get_context_data(self):
        createGraph()
        return {}
