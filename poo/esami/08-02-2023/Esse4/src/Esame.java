import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

public class Esame {
    private Corso corso;
    private Appello appello;
    private int esito;

    public Esame(Corso corso, Appello appello,  int esito) {
        if (!corso.getAppelliCorso().contains(appello)) throw new IllegalArgumentException("L'appello non fa parte ");
    }


}
