package trasmissione;

import enums.Genere;
import enums.Lingua;

import java.time.LocalDate;
import java.time.LocalTime;


/**
 * CLASSE TRASMISSIONE. <br>
 * Obiettivo:
 * - fornire informazioni relative al programma <br>
 * Sa fare: restituire le informazioni relative alla trasmissione. <br>
 * Conosce:
 * <ul>
 *    <li> titolo; </li>
 *    <li> genere; </li>
 *    <li> lingue; </li>
 *    <li> sottotitoli; </li>
 *    <li> orari di messa in onda <br> </li>
 *  </ul>
 */
public class Trasmissione {


    private final Genere genere;
    private final String titolo;
    private final Lingua lingua_audio;
    private final Lingua lingua_sottotitolo;
    private final String sottotitolo;
    private final LocalDate data;
    private final LocalTime ora;

    /***
     * Pre-condizioni:
     *  @param genere genere della trasmissione
     *  @param titolo titolo della trasmissione
     *  @param lingua_audio lingua audio della trasmissione
     *  @param lingua_sottotitolo lingua dei sottotitoli della trasmissione
     *  @param sottotitolo stringa per i sottotitoli della trasmissione
     *  @param data data di trasmissione della trasmissione 
     *  @param ora orario di trasmissione della trasmissione
     *
     * Post-condizioni: genera un oggetto trasmissione.
     */
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

