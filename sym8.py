import simpy
import random

def customer(env, name, pub, order_time_range, drinking_time_range, delay=0):
    yield env.timeout(delay)
    print(f"{env.now:.2f} - {name} arrives at the bar")
    with pub.bartenders.request() as request:
        yield request
        order_time = random.randint(*order_time_range)
        yield env.timeout(order_time)
        print(f"{env.now:.2f} - {name} received their order")
    drinking_time = random.randint(*drinking_time_range)
    yield env.timeout(drinking_time)
    print(f"{env.now:.2f} - {name} leaves the bar")

class Pub:
    def _init_(self, env, num_bartenders):
        self.bartenders = simpy.Resource(env, num_bartenders)

def setup_environment(num_customers, num_bartenders, order_time_range, drinking_time_range, simulation_time):
    env = simpy.Environment()
    pub = Pub(env, num_bartenders)
    arrival_times = [0, 10, 20, 30, 40, 50, 60]
    for i in range(num_customers):
        delay = random.choice(arrival_times)
        env.process(customer(env, f'Customer{i}', pub, order_time_range, drinking_time_range, delay))
    env.run(until=simulation_time)

num_customers = int(input("Enter the number of customers: "))
num_bartenders = int(input("Enter the number of bartenders: "))
min_order_time = int(input("Enter the minimum order time (in minutes): "))
max_order_time = int(input("Enter the maximum order time (in minutes): "))
min_drinking_time = int(input("Enter the minimum drinking time (in minutes): "))
max_drinking_time = int(input("Enter the maximum drinking time (in minutes): "))
simulation_time = int(input("Enter the total simulation time (in minutes): "))

setup_environment(num_customers, num_bartenders, (min_order_time, max_order_time), (min_drinking_time, max_drinking_time), simulation_time)
