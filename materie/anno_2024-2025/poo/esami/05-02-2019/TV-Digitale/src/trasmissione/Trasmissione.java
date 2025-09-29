package trasmissione;

import builders.TrasmissioneBuilder;
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
    private final Sottotitoli sottotitoli;
    private final LocalDate data;
    private final LocalTime ora;


    /***
     * Pre-condizioni:
     *  @param genere genere della trasmissione
     *  @param titolo titolo della trasmissione
     *  @param lingua_audio lingua audio della trasmissione
     *  @param sottotitoli classe Sottotitoli per i sottotitoli della trasmissione
     *  @param data data di trasmissione della trasmissione 
     *  @param ora orario di trasmissione della trasmissione
     *
     * Post-condizioni: genera un oggetto trasmissione.
     */
    public Trasmissione(Genere genere, String titolo, Lingua lingua_audio, Sottotitoli sottotitoli, LocalDate data, LocalTime ora) {
        this.genere = genere;
        this.titolo = titolo;
        this.lingua_audio = lingua_audio;
        this.lingua_sottotitolo = sottotitoli.getLingua();
        this.sottotitoli = sottotitoli;
        this.data = data;
        this.ora = ora;
    }

    public Trasmissione(TrasmissioneBuilder builder) {
        this.genere = builder.getGenere();
        this.titolo = builder.getTitolo();
        this.lingua_audio = builder.getLingua_audio();
        this.lingua_sottotitolo = builder.getLingua_sottotitolo();
        this.sottotitoli = builder.getSottotitoli();
        this.data = builder.getData();
        this.ora = builder.getOra();
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

    public Sottotitoli getSottotitoli() {
        return sottotitoli;
    }

    public LocalDate getData() {
        return data;
    }

    public LocalTime getOra() {
        return ora;
    }
}

