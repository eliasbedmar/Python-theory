from time import sleep

print("This is my file to demonstrate best practices.")

print("The value of __name__ is:", repr(__name__))

def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data

def read_data_from_web():
    print("Reading data from the Web")
    data = "Data from the Web"
    return data

def write_data_to_database(data):
    print("Writing data to database:")
    print(data)

# Def function [entry point] with default workflow
def main():
    data = read_data_from_web()
    modified_data=process_data(data)
    write_data_to_database(modified_data)

if __name__ == '__main__':
    main()
