from drivers.android_driver import create_android_driver

def get_driver(platform='android', config_path='config/dev.yml'):
    if platform == 'android':
        return create_android_driver(config_path)
    else:
        raise NotImplementedError('Only Android is implemented in this project.')
