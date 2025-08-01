import java.time.LocalDate;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/***
 * Mission: gestire i dati relativi a un corso
 * Conosce: nome, docente, DFU, anno del corso
 * Sa fare: fornisce i dati relativi al corso
 */


public class Corso {
    private String nomeCorso;
    private String docente;
    private int CFU;
    private AnnoCorso annoCorso;
    private List<Appello> appelliCorso = new ArrayList<>();

    public Corso(String nomeCorso, String docente, int CFU, AnnoCorso annoCorso) {
        if (nomeCorso == null || docente == null) throw  new IllegalArgumentException("Questo campo non pùò essere nullo");
        if (CFU <= 0) throw  new IllegalArgumentException("CFU devono essere positivi");
        if (annoCorso == null) throw new IllegalArgumentException("AnnoCorso non può essere null");
        this.nomeCorso = nomeCorso;
        this.docente = docente;
        this.CFU = CFU;
        this.annoCorso = annoCorso;
    }

    public void aggiungiAppello(Appello appello) {
        for  (Appello app : appelliCorso) {
            if (appello.getData() == app.getData()) throw new IllegalArgumentException("Gli appelli devono avere date diverse");
        }
        appelliCorso.add(appello);
    }

    public String getNomeCorso() {
        return nomeCorso;
    }

    public String getDocente() {
        return docente;
    }

    public int getCFU() {
        return CFU;
    }

    public AnnoCorso getAnnoCorso() {
     return annoCorso;
    }

    public List<Appello> getAppelliCorso() {
        return appelliCorso;
    }
}
