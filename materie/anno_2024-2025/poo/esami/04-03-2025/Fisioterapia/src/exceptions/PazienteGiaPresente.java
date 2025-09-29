package exceptions;

public class PazienteGiaPresente extends RuntimeException {
    public PazienteGiaPresente(String message) {
        super(message);
    }
}
