from fabric.api import run, sudo, env
from fabric.contrib.files import exists
import cuisine

env.ssh_config = True

def uname():
    """Print the name of the system to stdout"""
    run("uname -a")

def mongodb_install():
    """Ensure that mongodb is running
    """
    cuisine.package_install("mongodb")
    cuisine.upstart_ensure("mongodb-server")

def update_upgrade():
    """Update the list of dependencies and upgrade the packages,
    reboot if needed"""
    sudo("apt-get update")
    sudo("apt-get upgrade -y")
    if exists("/var/run/reboot-required"):
        sudo("reboot")

