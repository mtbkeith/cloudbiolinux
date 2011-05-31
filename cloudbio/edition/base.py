"""Base edition supplying CloudBioLinux functionality which can be customized.
"""
from fabric.api import *

class Edition:
    """Base class. Every edition derives from this
    """
    def __init__(self, env):
        self.name = "BioLinux base Edition"
        self.short_name = "biolinux"
        self.version = env.version
        self.env = env

    def check_packages_source(self):
        """Override for check package definition file before updating
        """
        self.env.logger.debug("check_packages_source not implemented")

    def rewrite_apt_sources_list(self, sources):
        """Allows editions to modify the sources list
        """
        return sources

    def rewrite_apt_automation(self, list):
        """Allows editions to modify the apt automation list
        """
        return list

    def rewrite_apt_keys(self, list):
        """Allows editions to modify key list"""
        return list

    def rewrite_apt_keyserver(self, list):
        """Allows editions to modify key list"""
        return list

    def apt_upgrade_system(self):
        """Upgrade system through apt - so this behaviour can be 
        overridden
        """
        sudo("apt-get -y --force-yes upgrade")

    def post_install(self):
        """Post installation hook"""

