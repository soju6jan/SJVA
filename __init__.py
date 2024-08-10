import os

from support import SupportSC

try:
    if os.path.exists(os.path.join(os.path.dirname(__file__), 'auth.py')):
        from .auth import Auth
    else:
        Auth = SupportSC.load_module_f(__file__, 'auth').Auth
except:
    pass
