package trasmissione;

import enums.Genere;
import enums.Lingua;
import trasmissione.film.SignoreDegliAnelli;

import java.time.LocalDate;
import java.time.LocalTime;

import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.assertEquals;

class TrasmissioneTest {

    public Trasmissione t = new Trasmissione(Genere.film, "Il signore degli anelli", Lingua.italiano, new SignoreDegliAnelli(Lingua.francese), LocalDate.parse("2025-07-27"), LocalTime.parse("17:42:30"));

    @org.junit.jupiter.api.Test
    void getGenere() {
        assertEquals(Genere.film, t.getGenere());
    }

    @org.junit.jupiter.api.Test
    void getTitolo() {
        assertEquals("Il signore degli anelli", t.getTitolo());
    }

    @org.junit.jupiter.api.Test
    void getLingua_audio() {
        assertEquals(Lingua.italiano, t.getLingua_audio());
    }

    @org.junit.jupiter.api.Test
    void getLingua_sottotitolo() {
        assertEquals(Lingua.francese, t.getLingua_sottotitolo());
    }

    @org.junit.jupiter.api.Test
    void getSottotitoli() {
        assertEquals(Lingua.francese, t.getSottotitoli().getLingua());
    }

    @org.junit.jupiter.api.Test
    void getData() {
        assertEquals(LocalDate.parse("2025-07-27"), t.getData());
    }

    @org.junit.jupiter.api.Test
    void getOra() {
        assertEquals(LocalTime.parse("17:42:30"), t.getOra());
    }


    @org.junit.jupiter.api.Test
    void ottieni_battuta_in_funzione_al_tempo() {
        assertEquals("Fuyez, imbéciles!", t.getSottotitoli().ottieni_battuta_in_funzione_al_tempo(LocalTime.of(0, 5)));
    }
}