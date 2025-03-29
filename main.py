import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def calculate_total_power(devices):
    """
    Calculate the total power consumption (in watts) of all supplied devices.
    :param devices: List of device power ratings in watts
    :return: Total power consumption in watts
    """
    total_power = sum(devices)
    #logging.info(f"Total power consumption: {total_power} W")
    return total_power


def calculate_total_energy(total_power, time_duration):
    """
    Calculate total energy consumption in kilowatt-hours (kWh) over a given time.
    :param total_power: Total power consumption in watts
    :param time_duration: Time duration in hours
    :return: Total energy consumption in kWh
    """
    total_energy = (total_power / 1000) * time_duration
    #logging.info(f"Total energy consumption: {total_energy} kWh")
    return total_energy


def calculate_energy_cost(total_energy, unit_cost):
    """
    Calculate the estimated cost of energy consumption.
    :param total_energy: Total energy consumption in kWh
    :param unit_cost: Unit cost of energy (Naira per kWh)
    :return: Total estimated energy cost in Naira
    """
    total_cost = total_energy * unit_cost
   #logging.info(f"Estimated energy cost: {total_cost} Naira")
    return total_cost


def get_user_inputs():
    """
    Collects input from the user for device power ratings, usage duration, and unit energy cost.
    :return: Tuple containing device power ratings, usage duration, and unit energy cost
    """
    devices_power = list(
        map(float, input("Enter the power ratings of devices in watts, separated by commas: ").split(',')))
    time_usage = float(input("Enter usage duration in hours: "))
    unit_energy_cost = float(input("Enter unit cost of energy (Naira per kWh): "))
    return devices_power, time_usage, unit_energy_cost


if __name__ == "__main__":
    # Get user inputs
    devices_power, time_usage, unit_energy_cost = get_user_inputs()

    # Perform Calculations
    total_power = calculate_total_power(devices_power)
    total_energy = calculate_total_energy(total_power, time_usage)
    total_cost = calculate_energy_cost(total_energy, unit_energy_cost)

    # Display Results
    print(f"\nTotal Power Consumption: {total_power} W")
    print(f"Total Energy Consumption: {total_energy} kWh")
    print(f"Estimated Energy Cost: {total_cost} ₦")


"""
New implementation to cook
1. Input validation: Making sure the program does not break when wrong data type is entered
2. Making the functions to be able to run as simple units and to be able to call one another if needs be
3. Implement Flask so that the program can be run as a web app 



"""