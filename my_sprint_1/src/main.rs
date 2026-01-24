use std::io; // input/output library

fn main() {
    // Immutable Variable.
    let secret_word = String::from("rustacean"); 

    // Mutable Variable.
    let mut lives = 6;

    // We create a mutable empty vector to hold user guesses.
    let mut guesses: Vec<char> = Vec::new();

    println!("Welcome to Hangman!");

    // Loop until out of lives or the user wins.
    while lives > 0 {
        // To prevent loss of ownership, we use borrowing with '&'.
        print_game_status(&secret_word, &guesses, lives);

        if is_word_guessed(&secret_word, &guesses) {
            println!("\nYou win! The word was: {}", secret_word);
            break; // Exit loop
        }

        println!("Please enter guess (single lower letter):");

        // Mutable string for user input.
        let mut input = String::new();
        
    
        // Match on user input
        match io::stdin().read_line(&mut input) {
            Ok(_) => {
                // Get the first character from the input
                // .trim() removes the "Enter" key newline
                // .chars().next() gets the first letter
                let guess_char = input.trim().chars().next();

                // Nested match to see if they actually typed a character
                match guess_char {
                    Some(c) => {
                        // Check if we already guessed it
                        if guesses.contains(&c) {
                            println!("You already guessed '{}'!", c);
                        } else {
                            guesses.push(c); // Add to guesses vector
                            
                            // Check if the guess was wrong
                            if !secret_word.contains(c) {
                                println!("Sorry, '{}' is not in the word.", c);
                                lives -= 1;
                            }
                        }
                    },
                    None => println!("You didn't type anything!"),
                }
            }
            Err(error) => {
                println!("Error reading input: {}", error);
            }
        }
    }

    if lives == 0 {
        println!("\nGame Over! The word was: {}", secret_word);
    }
}

// Function to print the current game status 
// Use &String and &Vec because I just want to READ the data, not change it.
fn print_game_status(word: &String, guesses: &Vec<char>, lives: i32) {
    println!("\n---------------------------------------");
    println!("Lives remaining: {}", lives);
    print!("Word: ");

    // Iterate through secret word
    for c in word.chars() {
        if guesses.contains(&c) {
            print!("{} ", c); // Print the letter if guessed
        } else {
            print!("_ "); // Print underscore if not
        }
    }
    println!();
}

// Function to check if the user has guessed every letter
fn is_word_guessed(word: &String, guesses: &Vec<char>) -> bool {
    for c in word.chars() {
        if !guesses.contains(&c) {
            return false; // Letter hasn't been guessed yet
        }
    }
    true // All letters are guessed
}