from email.mime import application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing as routes

application =  ProtocolTypeRouter({
    #This route can be accedd if user is athuenticaed
    'websocket': AuthMiddlewareStack( URLRouter(routes.websocket_url_patterns) )   
})
