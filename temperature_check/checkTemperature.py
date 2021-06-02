from gpiozero import CPUTemperature

cpu = CPUTemperature()


def checkTemperature() -> bool:
    return cpu.temperature > 60
