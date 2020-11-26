import base64

import pexpect
import xmltodict

from utilities.api_utils import clean_api_dict
from utilities.files import file_get_contents


class Sftp:
    """
    This class does SFTP the way you aren't supposed to in Python.
    It uses the pexpect module to execute the system sftp command, and interact with it to upload files.

    Based on the answer nobody liked at:
    https://stackoverflow.com/questions/432385/sftp-in-python-platform-independent#answer-42337162
    """

    sftp_command = "/usr/bin/sftp"
    child = None

    host = None
    username = None
    password = None
    port = 22

    def __init__(self, host=None, **kwargs):
        self.host = host
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.port = kwargs.get("port", 22)

        self.sftp_command = "/usr/bin/sftp"

    def read_config(self, filename):
        # Read a site exported from FileZilla
        xml = file_get_contents(filename)
        fz_config_read = clean_api_dict(xmltodict.parse(xml))
        fz_config = fz_config_read.get("file_zilla3").get("servers").get("server")

        pass_encoded = fz_config.get("pass").get("#text")
        pass_decoded = base64.b64decode(pass_encoded).decode()

        self.host = fz_config.get("host")
        self.username = fz_config.get("user")
        self.password = pass_decoded
        self.port = int(fz_config.get("port"))

    def connect(self):
        if self.host and self.username:
            self.child = pexpect.spawn("%s %s@%s" % (self.sftp_command, self.username, self.host))

        if self.password:
            # Auth
            self.child.expect(".* password:")
            self.child.sendline(self.password)
            self.child.expect("sftp> ")
            self.child.sendline("")
            self.child.expect("sftp> ")

    def disconnect(self):
        # Close
        self.child.sendline("bye")

    def put(self, local_file, remote_file):
        self.child.sendline("put %s %s" % (local_file, remote_file))

        return self.child.expect("sftp> ")

    def get(self, remote_file, local_file):
        self.child.sendline("get %s %s" % (remote_file, local_file))

        return self.child.expect("sftp> ")
