#from .auth import Auth
from support import SupportSC

Auth = SupportSC.load_module_f(__file__, 'auth').Auth

