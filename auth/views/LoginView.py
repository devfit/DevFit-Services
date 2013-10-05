from commons.utils.Global import P3P_HEADER
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.base import View

class LoginView(View):
    state = ""
    username = password = ''
    template_name = 'auth.html'
    
    def getResponse(self, request):
        initialData = {'state':self.state, 'username': self.username}
        csrfContext = RequestContext(request, initialData)
        response = render_to_response(self.template_name, csrfContext)
        # IE Blocking iFrame Cookies fix 
        # http://adamyoung.net/IE-Blocking-iFrame-Cookies
        response["P3P"] = P3P_HEADER
        return response
    
    def get(self, request, *args, **kwargs):
        return self.getResponse(request)

    def post(self, request, *args, **kwargs):
        self.username = request.POST.get('username')
        self.password = request.POST.get('password')
        
        user = authenticate(username=self.username, password=self.password)
        if user is not None:
            if user.is_active:
                login(request, user)
                self.state = "LOGIN_SUCCESS"
            else:
                self.state = "Your account is not active, please contact the site admin."
        else:
            self.state = "Your username and/or password were incorrect."
        
        return self.getResponse(request)
