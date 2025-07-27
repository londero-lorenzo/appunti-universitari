package builders;

import enums.Genere;
import enums.Lingua;

import trasmissione.Trasmissione;
import java.time.LocalDate;
import java.time.LocalTime;




public class TrasmissioneBuilder {

    private Genere genere;
    private String titolo;
    private Lingua lingua_audio;
    private Lingua lingua_sottotitolo;
    private String sottotitolo;
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

    public TrasmissioneBuilder setSottotitolo(String sottotitolo) {
        this.sottotitolo = sottotitolo;
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



    public Trasmissione build() {
        return new Trasmissione(this.genere, this.titolo, this.lingua_audio, this.lingua_sottotitolo, this.sottotitolo, this.data, this.ora);
    }

}