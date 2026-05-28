\#Project Overview
This project aims to build a traffic simulation environment for intra-city delivery agents operating on a dynamic road network with stochastic order arrivals and congestion-aware routing.



\#Objectives

* Simulate intra-city delivery operations
* Model dynamic traffic congestion
* Study Dispatch Policies
* Evaluate routing algorithms
* Build a future RL compatible environment for system.

\#Components of Environment (High-Level):
1) Network of Roads:
- Road Segments (Edges)
- Intersection/Junction (Nodes)
- Traffic Signals
- Type of Roads
- Speed Limits 
- Turn Restrictions

2) Traffic Dynamics Engine:
- Vehicle Behaviour: Speed, Acceleration, Deceleration
- Fluid/Atomic behaviour
- Max Speed, Length of vehicle, Other constraints

3) Event Scheduler:
- Discrete time step for simulation
- Order arrival
- Traffic Light Change
- Pickup time

4) Distribution:
- Distribution of order time throughout the day
- Distribution of capacity of restaurant 
- Distribution of orders throughout the geography
- Location of halt/parking places for delivery guys

5) Some policies:
- Cancellation Policy
- Acception/Rejection Rate and Policy

6) Routing and Dispatching Engine:
- Route planning
- Batching Decision
- Rerouting

7) Traffic Modelling:
- Traffic Congestion Model

8) KPIs:
- Average Delivery Time
- Order Completion Rate
- Fleet Utilisation


