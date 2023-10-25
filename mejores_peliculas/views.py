from django.shortcuts import render

movies = [
    {
        'id': 1,
        'titulo': 'El Padrino',
        'director': 'Francis Ford Coppola',
        'anio': 1972,
        'genero': 'Drama',
        'duracion': 175,    
        'quote': 'I\'m gonna make him an offer he can\'t refuse.',
        'imagen': 'mejores_peliculas/images/padrino.jpg',
        'sinopsis': 'Don Vito Corleone (Marlon Brando) es el respetado y temido jefe de una de las cinco familias de la mafia de Nueva York. Tiene cuatro hijos: una chica, Connie (Talia Shire), y tres varones: el impulsivo Sonny (James Caan), el pusilánime Fredo (John Cazale) y Michael (Al Pacino), que no quiere saber nada de los negocios de su padre. Cuando Corleone, siempre aconsejado por su consejero Tom Hagen (Robert Duvall), se niega a intervenir en el negocio de las drogas, el jefe de otra banda ordena su asesinato. Empieza entonces una violenta y cruenta guerra entre las familias mafiosas.',
        'votos': 100
    },
    {
        'id': 2,
        'titulo': 'El Padrino. Parte II',
        'director': 'Francis Ford Coppola',
        'anio': 1974,
        'genero': 'Drama',
        'duracion': 200,
        'quote': 'Keep your friends close, but your enemies closer.',
        'imagen': 'mejores_peliculas/images/padrinoii.jpg',
        'sinopsis': 'Continuación de la saga de los Corleone con dos historias paralelas: la elección de Michael Corleone como jefe de los negocios familiares y los orígenes del patriarca, el ya fallecido Don Vito, primero en Sicilia y luego en Estados Unidos, donde, empezando desde abajo, llegó a ser un poderosísimo jefe de la Mafia de Nueva York.',
        'votos': 100
    },
    {
        'id': 3,
        'titulo': 'Pulp Fiction',
        'director': 'Quentin Tarantino',
        'anio': 1994,
        'genero': 'Drama',
        'duracion': 154,
        'imagen': 'mejores_peliculas/images/pulp.jpg',
        'quote': 'I\'m sorry, did I break your concentration?',
        'sinopsis': 'Jules y Vincent, dos asesinos a sueldo con no demasiadas luces, trabajan para Marsellus Wallace. Vincent le confiesa a Jules que Marsellus le ha pedido que cuide de Mia, su atractiva mujer. Jules le recomienda prudencia porque es muy peligroso sobrepasarse con la novia del jefe. Cuando llega la hora de trabajar, ambos deben ponerse manos a la obra. Su misión: recuperar un misterioso maletín.',
        'votos': 100
    },
    {
        'id': 4,
        'titulo': 'Vertigo',
        'director': 'Alfred Hitchcock',
        'anio': 1958,
        'genero': 'Drama',
        'duracion': 128,
        'imagen': 'mejores_peliculas/images/vertigo.jpg',
        'quote': 'I don\'t want to die. There\'s someone inside me, and she says I must die.',
        'sinopsis': 'Un detective privado (Stewart) que padece de vértigo se encuentra con una atractiva mujer (Novak) que guarda un oscuro secreto. Este es el argumento de la película más personal de Hitchcock, una obra maestra del suspense que contiene algunas de las escenas más recordadas del cine. James Stewart y Kim Novak están inolvidables en esta película que, en su día, no fue bien recibida por la crítica, pero que con el tiempo se ha convertido en una de las más grandes películas de la historia del cine.',
        'votos': 100
    }
]

# Create your views here.
def index(request):
    return render(request, "mejores_peliculas/index.html", {'movies':movies})

def detalle(request, id):    
    movie = []
    for m in movies:
        if m.get("id") == id:
            movie = m
    return render(request, "mejores_peliculas/detalle.html", {"movie":movie})