from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS
from .models import Movie
from tags.models import Tag
from casts.models import Cast
import io
import pydotplus
from IPython.display import display, Image
from rdflib.tools.rdf2dot import rdf2dot


def create_movie_graph():
    # Create an RDF graph
    graph = Graph()

    # Define your custom namespace
    namespace = Namespace('http://example.org/ontology#')

    # Get all movies from the database
    movies = Movie.objects.all()

    # Iterate over each movie and add it to the RDF graph
    for movie in movies:
        # Create a URI for the movie using its ID
        movie_uri = namespace[str(movie.id)]

        # Add triples for the movie
        graph.add((movie_uri, RDF.type, namespace.Movie))
        graph.add((movie_uri, RDFS.label, Literal(movie.name)))
        graph.add((movie_uri, namespace.description,
                  Literal(movie.description)))
        # Add other properties of the movie to the RDF graph

        # Add relationships with tags
        for tag in movie.tags.all():
            graph.add((movie_uri, namespace.hasTag, Literal(tag.name)))

        # Add relationships with casts
        for cast in movie.casts.all():
            cast_uri = namespace[str(cast.id)]
            graph.add((movie_uri, namespace.hasCast, cast_uri))
            graph.add((cast_uri, RDF.type, namespace.Cast))
            graph.add((cast_uri, RDFS.label, Literal(cast.name)))
            graph.add((cast_uri, namespace.description,
                      Literal(cast.description)))
            # Add other properties of the cast to the RDF graph

        # Add relationships with directors
        for director in movie.directors.all():
            director_uri = namespace[str(director.id)]
            graph.add((movie_uri, namespace.hasDirector, director_uri))
            graph.add((director_uri, RDF.type, namespace.Director))
            graph.add((director_uri, RDFS.label, Literal(director.name)))
            graph.add((director_uri, namespace.description,
                      Literal(director.description)))
            # Add other properties of the director to the RDF graph

    # Return the RDF graph
    return graph


def visualize(g):
    stream = io.StringIO()
    rdf2dot(g, stream, opts={display})
    dg = pydotplus.graph_from_dot_data(stream.getvalue())
    png = dg.create_png()
    image_path = 'graph' + '.png'
    dg.write_png(image_path)
    dot_data = stream.getvalue()
    with open('graph.dot', 'w') as file:
        file.write(dot_data)
    return image_path
