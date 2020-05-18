# ta + sb
class Pulverizer:
    def initialize (self, a, b):
        self.a = a
        self.b = b
        self.t_queue = [0,1]
        self.s_queue = [0,1]
        self.t = 1
        self.s = self.calculate_s(a // b)

    def calculate_t (self, quotient):
        return self.t_queue[0] - quotient * self.t_queue[1]

    def calculate_s (self, quotient):
        return self.s_queue[0] + quotient * self.s_queue[1]

    def update_queue (self, queue, new_value):
        return [queue[1], new_value]

    def transit_t (self, quotient, remainder):
        self.t = self.calculate_t(quotient)
        self.t_queue = self.update_queue(self.t_queue, self.t)

    def transit_s (self, quotient, remainder):
        self.s = self.calculate_s(quotient)
        self.s_queue = self.update_queue(self.s_queue, self.s)
        self.a = self.b
        self.b = remainder

    def transit (self, quotient, remainder):
        self.transit_t(quotient, remainder)
        self.transit_s(quotient, remainder)

    def calculate_quotient (self):
        quotient = self.a // self.b
        remainder = self.a - quotient * self.b
        return quotient, remainder

    def get_current_result(self):
        return self.b, self.t, self.s

    def calculate_gcd(self, a, b):
        self.initialize(a, b)

        quotient, remainder = self.calculate_quotient()
        if remainder == 0: return self.get_current_result()
        self.transit_s(quotient, remainder)
        quotient, remainder = self.calculate_quotient()
        
        while remainder != 0:
            self.transit(quotient, remainder)
            quotient, remainder = self.calculate_quotient()

        return self.get_current_result()

# pulverizer = Pulverizer()
# gcd, t, s = pulverizer.calculate_gcd(24, 12)
# print('Result:', gcd, t, s)

# gcd, t, s = pulverizer.calculate_gcd(135, 59)
# print('Result:', gcd, t, s)

# gcd, t, s = pulverizer.calculate_gcd(259, 70)
# print('Result:', gcd, t, s)

# gcd, t, s = pulverizer.calculate_gcd(3, 100)
# print('Result:', gcd, t, s)

# gcd, t, s = pulverizer.calculate_gcd(13, 256)
# print('Result:', gcd, t, s)