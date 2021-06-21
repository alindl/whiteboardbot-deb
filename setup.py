from setuptools import setup

VERSION = '0.3.0'
DESCRIPTION='A bot that takes pictures of the whiteboard and sends it per email or slack',
LICENSE = "GNU GPL v3.0",
URL = 'https://github.com/alindl/WhiteBoardCam'

# setup parameters
setup(
    name='whiteboardbot',
    version=VERSION,
    description=DESCRIPTION,
    author='Andreas Lindlbauer',
    author_email='whiteboardbot.understress@aleeas.com',
    license = LICENSE,
    url = URL,
    install_requires=['bluepy', 'file-magic', 'RPi.GPIO', 'slackclient', 'gunicorn', 'wtforms', 'flask', 'flask_wtf', 'bootstrap-flask', 'configparser', 'wtforms_components', 'Flask-HTTPAuth', 'werkzeug', "flask_babel"],
    include_package_data=True,
    packages=['whiteboardbot'],
    package_dir={'whiteboardbot': 'whiteboardbot'},
    #package_data={'whiteboardbot': ['whiteboardbot.conf', 'webserver.sh' 'sounds', 'enhancer.sh', 'static', 'templates']},
    entry_points={
        'console_scripts': ['whiteboardbot = whiteboardbot.whiteboardbot:main']},
    keywords="python whiteboard slack email bot"
    )
