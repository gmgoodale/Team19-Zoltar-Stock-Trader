# Major Classes

<!---You should have an UML class diagram in this section, along with a description of each class and a table that relates each component to one or more user stories. At a minimum, you need 1 diagram of your major classes. You are encouraged to also include more detailed diagrams that include all of your classes.-->

- Data Handler: This class takes in data from a yahoo database that contains data for most major stocks.

- sqlDatabase: This class interfaces with the database to allow for simple function calls to gather full data from a stock ticker output in the desired datatype in one function call.

- DNN: This class provides functionality to easily create and train a Keras DNN based on TensorFlow.

- Window: This creates the structure and functionality for the user interface.

- Grapher: This is behind the window and provides a module for graphing functionality.

![ClassDiagram](Class_Diagram.jpg)
