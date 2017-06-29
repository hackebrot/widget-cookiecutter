import ipywidgets as widgets
from traitlets import Unicode


EMOJI = {
    'python': '🐍',
    'smile': '😃',
    'grin': '😁',
    'robot': '🤖',
    'coffee': '☕',
    'dog': '🐶',
    'cat': '🐱',
    'cry': '😢',
}

DEFAULT_TEXT = "Hi, I'm {{cookiecutter.author_name}}"
DEFAULT_EMOJI = "{{cookiecutter.default_emoji}}"

@widgets.register('hello.Hello')
class HelloWorld(widgets.DOMWidget):
    """"""
    _view_name = Unicode('HelloView').tag(sync=True)
    _model_name = Unicode('HelloModel').tag(sync=True)
    _view_module = Unicode('{{ cookiecutter.npm_package_name }}').tag(sync=True)
    _model_module = Unicode('{{ cookiecutter.npm_package_name }}').tag(sync=True)
    _view_module_version = Unicode('^{{ cookiecutter.npm_package_version }}').tag(sync=True)
    _model_module_version = Unicode('^{{ cookiecutter.npm_package_version }}').tag(sync=True)

    value = Unicode('').tag(sync=True)

    def __init__(self, text=DEFAULT_TEXT, emoji=DEFAULT_EMOJI):
        if emoji not in EMOJI:
            text = 'Sorry, this emoji is not supported'
            emoji = 'cry'

        super(HelloWorld, self).__init__(value=f'{text} {EMOJI[emoji]}')
