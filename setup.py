from setuptools import setup, find_packages


setup(
    name = "unittest-tap-reporting",
    version = '0.1',
    author = 'Vitold Sedyshev',
    author_email = 'vit1251@gmail.com',
    description = 'PyUnit-based test runner with TAP reporting.',
    license = 'LGPL',
    platforms = ['Any'],
    keywords = ['pyunit', 'unittest', 'junit xml', 'report', 'testrunner'],
    url = 'http://github.com/vit1251/unittest-tap-reporting/tree/master/',
    classifiers = [
#        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
#        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing'
    ],
    packages = find_packages('src'),
    package_dir = {'': 'src'},
#    test_suite = 'your.module.tests',
)

