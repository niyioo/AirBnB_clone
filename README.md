AirBnB Clone Console
This project is a command-line interface (CLI) that serves as a simplified clone of the Airbnb booking platform. It includes a command interpreter that allows users to interact with the application's models, create, retrieve, update, and delete data, and perform various operations on the objects.

Command Interpreter
The command interpreter is the core of this project. It allows users to interact with the application using text-based commands. The commands are designed to manage and manipulate the data models of the application. The command interpreter supports features such as creating, updating, deleting, and querying data objects.

How to Start the Command Interpreter

1. Clone this repository to your local machine:
 
    git clone https://github.com/niyi/AirBnB_clone.git

2. Navigate to the project directory:

    cd AirBnB_clone

3. Start the command interpreter:

    ./console.py

How to Use the Command Interpreter

Once the command interpreter is running, you can interact with it by typing commands and pressing Enter. The general syntax of the commands is as follows:

    (command) (model name) (operation) (parameters)

command: The action you want to perform (e.g., create, show, all).
model name: The name of the model you want to operate on (e.g., BaseModel, Amenity, City).
operation: The specific operation you want to perform on the model (e.g., create, update, delete, show, all).
parameters: Any additional parameters required for the operation (e.g., object ID).

Examples
1. Creating a new BaseModel instance:

    (hbnb) create BaseModel

2. Showing an instance's details by ID:

    (hbnb) show BaseModel 12345

3. Listing all instances of a model:

    (hbnb) all BaseModel

4. Updating an instance's attributes:

    (hbnb) update BaseModel 12345 attribute_name "new value"

5. Deleting an instance by ID:

    (hbnb) destroy BaseModel 12345

Exiting the Command Interpreter

To exit the command interpreter, use the quit or EOF command:

    (hbnb) quit
or
    Ctrl + D
