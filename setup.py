setting = {
    'filepath' : __file__,
    'use_db': True,
    'use_default_setting': True,
    'home_module': 'setting',
    'menu': None,
    'setting_menu': {
        'uri': f"sjva/setting/auth",
        'name': 'SJVA 설정',
    },
    'default_route': 'normal',
}

from plugin import *

P = create_plugin_instance(setting)

try:
    if os.path.exists(os.path.join(os.path.dirname(__file__), 'mod_setting.py')):
        from .mod_setting import ModuleSetting
    else:
        from support import SupportSC
        ModuleSetting = SupportSC.load_module_P(P, 'mod_setting').ModuleSetting
        
    P.set_module_list([ModuleSetting])
except Exception as e:
    P.logger.error(f'Exception:{str(e)}')
    P.logger.error(traceback.format_exc())

from . import Auth

P.get_auth_status = Auth.get_auth_status

# python -m flaskfarm.cli.code_encode --source=C:\work\FlaskFarm\data\LOADING2\sjva
