# Java Terminal Memory Game with STM32 Nucleo Controller

This was a fun project where I could combine some of my skills from Embedded Systems with Java! This project is a Memory Game that recieves input from a joystick connected to a Nucleo Board. The Nucleo board connects to port on the PC and send UART signals to the PC via USB cable. The Nucleo board reads the joystick's analog signals (X/Y axes) and digital button clicks. The Java application parses this data, applies a deadzone, and drives a 4x4 grid in the terminal.

## Instructions for Build and Use

[Software Demo Video](https://youtu.be/G3vYBLT_80U)

Steps to build and/or run the software:

1. Connect the STM32 Nucleo development board to the computer via USB. Ensure the analog joystick is properly wired to the correct ADC and GPIO pins.
2. Flash the Nucleo board with the embedded C program (via STM32CubeIDE) so that it begins printing comma-separated values (`X, Y, Button`) to the serial monitor at a baud rate of 115200.
3. Ensure your PC can run Java programs.
4. Clone or download this project repository and open the folder in Visual Studio Code.
5. Verify that the `jSerialComm-2.11.4.jar` library is located in the project's `lib` folder.
6. Open the device manager on your computer to check which COM port your Nucleo board is using (usually `COM4`).
7. Open `App.java` and update the `SerialPort.getCommPort("COM4");` line to match your board's currently assigned port.
8. Run the Java application.
9.  If security warnings about "restricted methods" appear, they can be safely ignored, as they are a byproduct of `jSerialComm` interfacing with the hardware in newer Java versions.

Instructions for using the software:

1. Launch the program, mve the joystick once, and wait for the terminal to display "Successfully opened the port". The terminal will clear and draw a 4x4 grid of hidden cards (represented by `*`)
2. Push the physical analog joystick Up, Down, Left, or Right to move the cursor (`[ ]`) across the board.
3. Allow the joystick to return to its center resting position (the deadzone) between movements to prevent the cursor from rapidly flying off the grid.
4. Press down on the joystick (button click) to select and flip a card face up, revealing its letter (A-H).
5. Navigate to a second card and click to flip it. 
6. If the two cards match, they will remain face up permanently. If they do not match, the game will pause for 1 second before flipping them back over.
7. Continue moving and flipping until you have successfully matched all 8 pairs on the board!

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Java Development Kit (JDK) version 25.0.2
* Visual Studio Code
* `jSerialComm` library (Version 2.11.4)
* STM32CubeIDE
* STM32 Nucleo-64 Development Board 
* 5-Pin Analog Joystick Module 

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Oracle Java JDK Documentation](https://docs.oracle.com/en/java/)
* [jSerialComm GitHub & Usage Guide](https://fazecast.github.io/jSerialComm/)
* [Java Tutorial—W3Schools](https://www.w3schools.com/java/)
* [Java Collection Frameworks—BeginnersBook](https://beginnersbook.com/2013/12/java-collections-framework/)
* [Gemini](https://gemini.google.com/)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Add a turn counter to track how many attempts it takes to clear the board.
* [ ] Implement File I/O to save and read a "High Score" (lowest number of turns) to a local text file.
* [ ] Add a GUI (Graphical User Interface) using Java Swing or JavaFX to replace the terminal-based grid.
* [ ] Implement a hardware-based "Restart Game" feature by holding the joystick button down for 3 seconds.