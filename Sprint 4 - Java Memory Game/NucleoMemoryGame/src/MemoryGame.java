import java.util.ArrayList;
import java.util.Collections;

public class MemoryGame {
    private ArrayList<Card> deck; // Java Collection Framework requirement
    private int cursorX = 0;
    private int cursorY = 0;
    private final int GRID_SIZE = 4;
    
    private Card firstPick = null;
    private Card secondPick = null;

    public MemoryGame() {
        deck = new ArrayList<>();
        char[] symbols = {'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H'};
        
        for (char s : symbols) {
            deck.add(new Card(s));
        }
        Collections.shuffle(deck); // Randomize the cards
    }

    public void drawBoard() {
        // Clear the terminal (works in most modern terminals)
        System.out.print("\033[H\033[2J");
        System.out.flush();
        
        System.out.println("=== TERMINAL MEMORY GAME ===\n");

        for (int row = 0; row < GRID_SIZE; row++) {
            for (int col = 0; col < GRID_SIZE; col++) {
                int index = (row * GRID_SIZE) + col;
                Card card = deck.get(index);
                
                // Determine what to display for the card
                char displayChar = '*';
                if (card.isFlipped() || card.isMatched()) {
                    displayChar = card.getSymbol();
                }

                // Draw the cursor if we are on this card
                if (row == cursorY && col == cursorX) {
                    System.out.print("[" + displayChar + "] ");
                } else {
                    System.out.print(" " + displayChar + "  ");
                }
            }
            System.out.println("\n");
        }
    }

    public void moveCursor(int dx, int dy) {
        // Conditionals to keep the cursor inside the 4x4 grid
        if (cursorX + dx >= 0 && cursorX + dx < GRID_SIZE) {
            cursorX += dx;
        }
        if (cursorY + dy >= 0 && cursorY + dy < GRID_SIZE) {
            cursorY += dy;
        }
        drawBoard();
    }

    public void selectCard() {
        int index = (cursorY * GRID_SIZE) + cursorX;
        Card selectedCard = deck.get(index);

        // Ignore if already matched or already flipped
        if (selectedCard.isMatched() || selectedCard.isFlipped()) return;

        selectedCard.setFlipped(true);
        drawBoard();

        if (firstPick == null) {
            firstPick = selectedCard;
        } else if (secondPick == null) {
            secondPick = selectedCard;
            checkMatch();
        }
    }

    private void checkMatch() {
        // Simple pause so the player can see the second card before it hides
        try { Thread.sleep(1000); } catch (InterruptedException e) {}

        if (firstPick.getSymbol() == secondPick.getSymbol()) {
            firstPick.setMatched(true);
            secondPick.setMatched(true);
        } else {
            firstPick.setFlipped(false);
            secondPick.setFlipped(false);
        }
        
        // Reset picks
        firstPick = null;
        secondPick = null;
        drawBoard();
    }
}