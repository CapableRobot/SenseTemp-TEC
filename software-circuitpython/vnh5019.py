import digitalio
import analogio
import pulseio

class VNH5019:

    def __init__(self, pins):
        self.pins = pins
        self.state = 0

        self.setup_pins()

    def setup_pins(self):
        self.ina = digitalio.DigitalInOut(self.pins['ina'])
        self.ina.switch_to_output(digitalio.DriveMode.PUSH_PULL)

        self.inb = digitalio.DigitalInOut(self.pins['inb'])
        self.inb.switch_to_output(digitalio.DriveMode.PUSH_PULL)

        self.diaga = digitalio.DigitalInOut(self.pins['diaga'])
        self.diaga.switch_to_input(pull=digitalio.Pull.UP)

        self.diagb = digitalio.DigitalInOut(self.pins['diagb'])
        self.diagb.switch_to_input(pull=digitalio.Pull.UP)

        self.fb = analogio.AnalogIn(self.pins['fb'])

        self.pwm = pulseio.PWMOut(self.pins['pwm'], frequency=20000) 

    def set(self, rate):

        # Ignore values that are out of bounds
        if abs(rate) >= 2**16:
            return

        if rate > 0:
            if self.state <= 0:
                print("State {} to 1".format(self.state))
                self.inb.value = False
                self.ina.value = True
                self.state = 1

        elif rate < 0:
            if self.state >= 0:
                print("State {} to -1".format(self.state))
                self.ina.value = False
                self.inb.value = True
                self.state = -1
        else:
            self.state = 0
            self.ina.value = False
            self.inb.value = False


        self.pwm.duty_cycle = abs(rate)

    def faults(self):
        return (not self.diaga.value, not self.diagb.value)

    def current(self):
        voltage = float(self.fb.value) * self.fb.reference_voltage / 2**16
        current = voltage / 0.14
        return current