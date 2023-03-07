I am going to use Python and SQLAlchemy to do a basic climate analysis and data exploration for climate database.
I am going to use the provided files (climate_starter.ipynb and hawaii.sqlite) to complete  climate analysis and data exploration.
I use create_engine() function to connect to SQLite database.

I use the SQLAlchemy automap_base() function to reflect my tables into classes, and then save references to the classes named station and measurement.

Next step is to Link Python to the database by creating a SQLAlchemy session.
![image1](https://user-images.githubusercontent.com/111449865/223540525-76bb2606-1c01-48b7-925e-59f893ace637.png)
![image](https://user-images.githubusercontent.com/111449865/223540726-b533c2a3-ce74-4c51-9888-a1dea07c3014.png)


![precipitation](https://user-images.githubusercontent.com/111449865/223539854-ec49f0e2-afc0-4a0c-ac8f-7bcab4fbc3a7.png)
![station-histogram](https://user-images.githubusercontent.com/111449865/223539943-b9342677-6dd6-440a-917d-e44c78a80ac2.png)
