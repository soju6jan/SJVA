"""
{
    'uri': __package__,
    'name': 'SJVA',
    'list': [
        {
            'uri': 'setting',
            'name': '설정',
            'list': [
                {
                    'uri': 'auth',
                    'name': '인증',
                },
                {
                    'uri': 'bot',
                    'name': '텔레그램 봇',
                }
            ]
        },
        {
            'uri': 'plugin',
            'name': '전용 플러그인',
        },
        {
            'uri': 'log',
            'name': '로그',
        },
    ]
},
"""

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
WEB_DIRECT_URL= "http://52.78.103.230:49734"
DEFINE_DEV = False


from plugin import *

P = create_plugin_instance(setting)

try:
    if DEFINE_DEV:
        from .mod_setting import ModuleSetting
    else:
        from support import SupportSC
        ModuleSetting = SupportSC.load_module_P(P, 'mod_setting').ModuleSetting
        
    P.set_module_list([ModuleSetting])
except Exception as e:
    P.logger.error(f'Exception:{str(e)}')
    P.logger.error(traceback.format_exc())

