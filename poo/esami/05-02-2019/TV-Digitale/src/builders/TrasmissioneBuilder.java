package builders;

import enums.Genere;
import enums.Lingua;

import trasmissione.Sottotitoli;
import trasmissione.Trasmissione;
import java.time.LocalDate;
import java.time.LocalTime;




public class TrasmissioneBuilder {

    private Genere genere;
    private String titolo;
    private Lingua lingua_audio;
    private Lingua lingua_sottotitolo;
    private Sottotitoli sottotitoli;
    private LocalDate data;
    private LocalTime ora;

    public TrasmissioneBuilder setGenere(Genere genere) {
        this.genere = genere;
        return this;
    }

    public TrasmissioneBuilder setTitolo(String titolo) {
        this.titolo = titolo;
        return this;
    }

    public TrasmissioneBuilder setLingua_Audio(Lingua lingua_audio) {
        this.lingua_audio = lingua_audio;
        return this;
    }

    public TrasmissioneBuilder setLingua_Sottotitolo(Lingua lingua_sottotitolo) {
        this.lingua_sottotitolo = lingua_sottotitolo;
        return this;
    }

    public TrasmissioneBuilder setSottotitoli(Sottotitoli sottotitoli) {
        this.sottotitoli = sottotitoli;
        return this;
    }

    public TrasmissioneBuilder setData(LocalDate data) {
        this.data = data;
        return this;
    }

    public TrasmissioneBuilder setOra(LocalTime ora) {
        this.ora = ora;
        return this;
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


    public Trasmissione build() {
        return new Trasmissione(this);
    }

}