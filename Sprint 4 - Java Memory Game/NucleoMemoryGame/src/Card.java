public class Card {
    private char symbol;
    private boolean isFlipped;
    private boolean isMatched;

    public Card(char symbol) {
        this.symbol = symbol;
        this.isFlipped = false;
        this.isMatched = false;
    }

    public char getSymbol() { return symbol; }
    public boolean isFlipped() { return isFlipped; }
    public boolean isMatched() { return isMatched; }
    
    public void setFlipped(boolean flipped) { this.isFlipped = flipped; }
    public void setMatched(boolean matched) { this.isMatched = matched; }
}