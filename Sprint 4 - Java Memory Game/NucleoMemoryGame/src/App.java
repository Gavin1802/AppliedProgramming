import com.fazecast.jSerialComm.SerialPort;
import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        
        // Select the port and configure the connection
        SerialPort sp = SerialPort.getCommPort("COM4");
        
        sp.setComPortParameters(115200, 8, 1, 0); 
        sp.setComPortTimeouts(SerialPort.TIMEOUT_SCANNER, 0, 0);

        // Open the port
        if (sp.openPort()) {
            System.out.println("Successfully opened the port");
        } else {
            System.out.println("Failed to open the port");
            return;
        }

        // Initialize Memory Game
        MemoryGame game = new MemoryGame();
        game.drawBoard(); // Draw the initial screen

        boolean joystickCentered = true; // Prevents rapid-fire movement
        boolean buttonReleased = true;   // Prevents rapid-fire clicking

        // Memory Game
        try (Scanner scanner = new Scanner(sp.getInputStream())) {
            System.out.println("Looking for joystick data...");
            
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                
                // Split string by the commas
                String[] values = line.split(",");
                
                if (values.length == 3) {
                    try {
                        // Convert the text into usable integers
                        int x = Integer.parseInt(values[0].trim());
                        int y = Integer.parseInt(values[1].trim());
                        int btn = Integer.parseInt(values[2].trim());
                        
                        // Check if joystick has returned to the resting deadzone
                        if (x > 1000 && x < 3000 && y > 1000 && y < 3000) {
                            joystickCentered = true;
                        }
                        if (btn == 1) {
                            buttonReleased = true;
                        }

                        // --- GAME LOGIC TRANSLATION ---
                        
                        // Only move if the joystick was previously centered
                        if (joystickCentered) {
                            // X-Axis (Left / Right)
                            if (x < 1000) { 
                                game.moveCursor(-1, 0); 
                                joystickCentered = false; 
                            } else if (x > 3000) { 
                                game.moveCursor(1, 0); 
                                joystickCentered = false; 
                            }

                            // Y-Axis (Up / Down)
                            if (y < 1000) { 
                                game.moveCursor(0, -1); 
                                joystickCentered = false; 
                            } else if (y > 3000) { 
                                game.moveCursor(0, 1); 
                                joystickCentered = false; 
                            }
                        }

                        // Button
                        if (btn == 0 && buttonReleased) {
                            game.selectCard();
                            buttonReleased = false;
                        }

                    } catch (NumberFormatException e) {}
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            sp.closePort();
        }
    }
}