from fabric.api import run, sudo, env, put
from fabric.contrib.files import exists
import cuisine

env.use_ssh_config = True
env.user = "ubuntu"

def uname():
    """Print the name of the system to stdout"""
    run("uname -a")

def mongodb_install():
    """Ensure that mongodb is running
    """
    cuisine.package_install("mongodb")
    cuisine.upstart_ensure("mongodb-server")

def install_fabric():
    """Install fabric and cuisine on the host, use the package manager for
    fabric and pip for cuisine"""
    cuisine.package_ensure("fabric")
    cuisine.package_ensure("python-pip")
    run("pip install --user cuisine")
    put("fabfile.py")
    put("ssh_conf", ".ssh/config")
    put("~/.ssh/open_stack_test", ".ssh/id_rsa")
    run("chmod 600 .ssh/id_rsa")

def update_upgrade():
    """Update the list of dependencies and upgrade the packages,
    reboot if needed"""
    sudo("apt-get update")
    sudo("apt-get upgrade -y")
    if exists("/var/run/reboot-required"):
        sudo("reboot")

def on_cluster():
    """Apply the next rule on the cluster """
    for i in [5,7,8,9,10,11,12,13]:
        host = "192.168.123." + str(i)
        env.hosts += [host]
    env.user = "ubuntu"

def execute(cmd):
    """execute the command given in parameter"""
    run(cmd)
