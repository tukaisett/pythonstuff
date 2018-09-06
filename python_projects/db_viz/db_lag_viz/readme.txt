This project is to visualize the Replication DB Lag of a Slave server w.r.t to a Master server.
The webpage is supposed to auto refresh every 10 minutes
The Lag is stored in a table every 5 minutes, the reading of Lag is taken every minute.
Lag time is obtained via a REST Api call, which gets lag times of NOW() and of the last 2 hours.
For testing purpose, we will simulate the data.
