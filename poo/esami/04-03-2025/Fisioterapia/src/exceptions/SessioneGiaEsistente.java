package exceptions;

public class SessioneGiaEsistente extends RuntimeException {
    public SessioneGiaEsistente(String message) {
        super(message);
    }
}
