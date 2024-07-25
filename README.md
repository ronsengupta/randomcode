# randomcode

Customers and Bartenders: Identified as key players. Customers follow their own schedule: arrive, order, and drink. Bartenders are the critical resource needed for orders to be processed.

Staggered Arrivals: To mimic real-world scenarios, customers don't all arrive at once. Instead, they come in at different times, selected randomly from a predefined list, to simulate the natural flow of a pub.

Simple:
Kept customer actions straightforward to focus on the impact of bartender availability on service times and customer wait times.

Using SimPy, the simulation tracks discrete events such as arrivals and departures.

Resource: Bartenders are managed as limited resources, affecting how quickly customers are served.

