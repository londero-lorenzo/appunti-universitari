import java.time.LocalDate;
import java.time.LocalTime;


/**
 * CLASSE TRASMISSIONE.
 * Obiettivo:
 * - fornire informazioni relative al programma:
 *     * titolo;
 *     * genere;
 *     * lingue;
 *     * sottotitoli;
 *     * orari di messa in onda
 * Sa fare: 
 */
public class Trasmissione {


    private final Genere genere;
    private final String titolo;
    private final Lingua lingua_audio;
    private final Lingua lingua_sottotitolo;
    private final String sottotitolo;
    private final LocalDate data;
    private final LocalTime ora;


    public Trasmissione(Genere genere, String titolo, Lingua lingua_audio, Lingua lingua_sottotitolo, String sottotitolo, LocalDate data, LocalTime ora) {
        this.genere = genere;
        this.titolo = titolo;
        this.lingua_audio = lingua_audio;
        this.lingua_sottotitolo = lingua_sottotitolo;
        this.sottotitolo = sottotitolo;
        this.data = data;
        this.ora = ora;
    }


    public Genere getGenere() {
        return genere;
    }

    public String getTitolo() {
        return titolo;
    }

    public Lingua getLingua_audio() {
        return lingua_audio;
    }

    public Lingua getLingua_sottotitolo() {
        return lingua_sottotitolo;
    }

    public String getSottotitolo() {
        return sottotitolo;
    }

    public LocalDate getData() {
        return data;
    }

    public LocalTime getOra() {
        return ora;
    }
}

