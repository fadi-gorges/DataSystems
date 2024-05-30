# Car Sales Database Setup

This repository contains the prototype SQL scripts for creating and populating the database tables for the WheelsDirect Car Sales Analysis System. These scripts were updated and improved upon during the development process.

### Custom Table

This table stores information about the custom features of the cars. The columns in this table are:

- `custom_id`: A unique identifier for each custom feature set.
- `doors`: The number of doors in the car.
- `seats`: The number of seats in the car.
- `extColour`: The external color of the car.
- `intColour`: The internal color of the car.

### Model Table

This table stores information about the model of the cars. The columns in this table are:

- `model_id`: A unique identifier for each model.
- `year`: The year the model was released.
- `transmission`: The type of transmission in the model.

### Line Table

This table stores information about the line of the cars. The columns in this table are:

- `line_id`: A unique identifier for each line.
- `model`: The model of the car.
- `engine`: The engine capacity of the car.
- `driveType`: The type of drive system in the car.
- `fuelType`: The type of fuel the car uses.
- `fuelConsumption`: The fuel consumption rate of the car.
- `cylindersInEngine`: The number of cylinders in the car's engine.
- `bodyType`: The body type of the car.

### Cars Table

This table stores general information about the cars. The columns in this table are:

- `car_id`: A unique identifier for each car.
- `usedOrNew`: Whether the car is used or new.
- `kilometres`: The number of kilometres the car has been driven.
- `price`: The price of the car.

The data for these tables is populated from the `CarSales` table.
