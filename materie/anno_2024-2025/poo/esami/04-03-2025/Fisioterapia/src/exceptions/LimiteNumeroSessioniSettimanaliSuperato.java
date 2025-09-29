package exceptions;

public class LimiteNumeroSessioniSettimanaliSuperato extends RuntimeException {
    public LimiteNumeroSessioniSettimanaliSuperato(String message) {
        super(message);
    }
}
