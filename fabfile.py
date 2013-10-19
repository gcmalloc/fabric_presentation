from fabric import run, sudo
from fabric.contrib.files import exists


def uname():
    """Print the name of the system to stdout"""
    run("uname -a")


def update_upgrade():
    """Update the list of dependencies and upgrade the packages,
    reboot if needed"""
    sudo("apt-get update")
    sudo("apt-get upgrade -y")
    if exists("/var/run/reboot-required"):
        sudo("reboot")

