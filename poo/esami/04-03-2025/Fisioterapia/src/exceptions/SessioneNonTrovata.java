package exceptions;

public class SessioneNonTrovata extends RuntimeException {
    public SessioneNonTrovata(String message) {
        super(message);
    }
}
