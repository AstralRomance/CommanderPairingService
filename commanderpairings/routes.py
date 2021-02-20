from .views import views

def setup_routes(app):
    app.router.add_route('GET', '/', views.index)
    app.router.add_route('POST', '/', views.add_player)
    app.router.add_route('GET', '/token', views.get_token)
    app.router.add_route('GET', '/validate_token', views.validate_token)
    app.router.add_route('GET', '/pairings', views.pairings)
    app.router.add_route('GET', '/get_players', views.get_players)
    app.router.add_route('GET', '/make_pairings', views.make_pairings)
