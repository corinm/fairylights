import sys

module = type(sys)("rpi_ws281x")
sys.modules["rpi_ws281x"] = module
