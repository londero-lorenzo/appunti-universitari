import java.util.ArrayList;
import java.util.List;

/***
 * Mission: fornire informazioni e dati sullo studente
 * Conosce: dati anagrafici, matricola, corsi a cui è iscritto, anno di corso, CFU, esami già sostenuti
 */


public class Studente {
    private String nome;
    private String cognome;
    private int matricola;
    private AnnoCorso annoCorso;
    private List<Corso> corsiAttuali = new ArrayList<>();

    public Studente(String nome, String cognome, int matricola, AnnoCorso annoCorso) {
        this.nome = nome;
        this.cognome = cognome;
        this.matricola = matricola;
        this.annoCorso = annoCorso;
    }

    public void aggiungiCorsiAttuali(Corso corso) {
        if (corso.getAnnoCorso() != annoCorso){
            throw new IllegalArgumentException("Il corso deve essere dell'anno corrente dello studente");
        }
        corsiAttuali.add(corso);
    }

    public String getNome() {
        return nome;
    }

    public String getCognome() {
        return cognome;
    }

    public int getMatricola() {
        return matricola;
    }

    public AnnoCorso getAnnoCorso() {
        return annoCorso;
    }

}
