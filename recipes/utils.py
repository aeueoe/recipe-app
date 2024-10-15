from .models import Recipe
from io import BytesIO
import base64
import matplotlib.pyplot as plt

# Function to generate base64-encoded graph image
def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png).decode('utf-8')
    buffer.close()
    return graph

# Function to generate chart based on user input
def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(6, 3))

    if chart_type == '#1':
        plt.bar(data['name'], data['cooking_time'])
        plt.title('Cooking Time by Recipe')
    elif chart_type == '#2':
        labels = kwargs.get('labels')
        plt.pie(data['cooking_time'], labels=labels, autopct='%1.1f%%')
        plt.title('Cooking Time Distribution')
    elif chart_type == '#3':
        plt.plot(data['name'], data['cooking_time'], marker='o')
        plt.title('Cooking Time Trend')
    else:
        return None
    
    plt.tight_layout()
    return get_graph()
