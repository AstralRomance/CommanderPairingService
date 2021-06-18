from .views import register_views, pairing_views, views

def setup_routes(app):
    app.router.add_route('GET', '/', register_views.index)
    app.router.add_route('POST', '/', register_views.add_player)
    app.router.add_route('GET', '/token', views.get_token)
    app.router.add_route('GET', '/validate_token', views.validate_token)
    app.router.add_route('GET', '/pairings', pairing_views.pairings)
    app.router.add_route('GET', '/get_players', pairing_views.get_players)
    app.router.add_route('GET', '/make_pairings', pairing_views.make_pairings)
