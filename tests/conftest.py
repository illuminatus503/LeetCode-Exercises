import os
import sys

# Prepend project root so `import src…` works
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
