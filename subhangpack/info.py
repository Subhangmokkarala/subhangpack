#generate a module which will tell system specs of your computer
import platform
def sysinfo():
    print("System info:")
    print(platform.platform())
    print(platform.machine())
    print(platform.processor())
    print(platform.system())
    print(platform.version())
    print(platform.uname())
    print(platform.architecture())
    print(platform.node())
    print(platform.python_version())
    print(platform.python_build())
    print(platform.python_compiler())
    print(platform.python_branch())
    print(platform.python_implementation())
    print(platform.python_revision())
    print(platform.release())
