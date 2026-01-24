# Project Title (Update)

This is a basic hangman game. It was created because it helped me understand all the basics of Rust as specified by the module requirements. The project was challenging to properly handing user input, vectors(lists), and value comparison. I learned how to create functions, manipulate basic data structures, and handle I/O properly.

## Instructions for Build and Use

[Software Demo](https://youtu.be/MHpTt8CVcBI)

Steps to build and/or run the software:

1. Have Visual Studio Code with Rust extensions
2. Install Rust
3. Open the project in Visual Studio Code
4. Navigate to the Main1.rs file within the my_sprint_1 folder
5. Open the terminal in this location and type 'cargo run'


Instructions for using the software:

1. Follow the prompts as requested by the program within the terminal
2. The game hangman requires a word that the user doesn't know, then allowing the user to guess individual letters within the word
3. If the user guesses a letter that is in the word, the game shows the placement of that letter relative to the other letters represented by '_'
4. If the user guesses a letter that is not in the word, the game decrements the number of lives(6 in this case), and tells the user that letter isn't in the word.
5. If the life count hits zero, the game is over, the word is revealed and the program exits.
6. If the user guesses the word, the game is won, and the program exits.

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Standard I/O library for user input

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Rust Programming Full Course](https://www.youtube.com/watch?v=rQ_J9WH6CGk&pp=ygUgcnVzdCBwcm9ncmFtbWluZyBsYW5ndWFnZSBjb3Vyc2XSBwkJhwoBhyohjO8%3D)
* [The Rust Programming Language](https://doc.rust-lang.org/book/)
* [Gemini](https://gemini.google.com/)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [Structs] Currently the game state passes data through functions loosely. I should encapsulate this data into a single struct to better manage ownership.
* [Input] The game doesn't handle uppercase letters other than saying they're not in the word. I should create a function to handle input entirely and remove that from the main logic.
* [Visuals] I could probably add an ascii representation of a gallows with a stick figure to represent lives left.
* [Efficiency] I should improve efficiency of the program by using a different data type than a vector so that I don't have to iterate through the vector each time. If the word had a million letters, it wouldn't be very efficient at all.
