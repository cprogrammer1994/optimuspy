import argparse
import os
import shutil
import subprocess
from distutils import sysconfig
from distutils._msvccompiler import MSVCCompiler
from distutils.util import get_platform

cvars = sysconfig.get_config_vars()


def find_program(name):
    for path in os.environ['PATH'].split(os.pathsep):
        executable = os.path.join(path, name + '.exe')
        if os.path.isfile(executable):
            return executable


def compile_with_msvcc():
    msvcc = MSVCCompiler()
    msvcc.initialize()
    msvcc.add_include_dir(cvars['INCLUDEPY'])
    msvcc.add_library_dir(os.path.join(cvars['exec_prefix'], 'libs'))

    args = [msvcc.cc]
    args += ['/nologo', '/Ox', '/W3', '/GL', '/DNDEBUG', '/MD']
    args += ['-I' + inc for inc in msvcc.include_dirs]
    args += ['optimuspy.cpp']
    args += ['/link']
    args += ['/LIBPATH:' + inc for inc in msvcc.library_dirs]
    args += ['User32.lib', 'Shell32.lib']
    args += ['/OUT:optimuspy.exe']

    subprocess.Popen(args).wait()

    for temp in ['optimuspy.obj', 'optimuspy.lib', 'optimuspy.exp']:
        if os.path.isfile(temp):
            os.unlink(temp)


def compile_with_gcc():
    gcc = find_program('g++')
    dll = os.path.join(cvars['BINDIR'], 'python%s.dll' % cvars['VERSION'])
    bits = '32' if get_platform() == 'win32' else '64'

    args = [gcc]
    args += ['-O2']
    args += ['-m' + bits]
    args += ['-I' + cvars['INCLUDEPY']]
    args += ['optimuspy.cpp']
    args += [dll]
    args += ['-o', 'optimuspy.exe']

    subprocess.Popen(args).wait()


parser = argparse.ArgumentParser(prog='build.py')
parser.add_argument('--gcc', action='store_true', help='compile using gcc')
parser.add_argument('--install', action='store_true', help='install the optimuspy')
args = parser.parse_args()

if args.gcc and not find_program('g++'):
    raise Exception('Cannot find g++.exe')

if args.gcc:
    compile_with_gcc()

else:
    compile_with_msvcc()

if args.install:
    install = os.path.join(cvars['exec_prefix'], 'optimuspy.exe')
    shutil.copyfile('optimuspy.exe', install)
    print('Created', install)
