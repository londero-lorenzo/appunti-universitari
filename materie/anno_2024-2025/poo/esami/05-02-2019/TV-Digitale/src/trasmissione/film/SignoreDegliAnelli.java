package trasmissione.film;

import trasmissione.Sottotitoli;
import enums.Lingua;

import java.time.LocalTime;
import java.util.HashMap;
import java.util.Map;

public class SignoreDegliAnelli extends Sottotitoli {

    public String titolo;

    public Map<LocalTime, String> battute;

    public Lingua lingua;

    public SignoreDegliAnelli(Lingua lingua_sottotitoli) {
        this.titolo = "Signore degli anelli";
        this.battute = new HashMap<LocalTime, String>();
        this.lingua = lingua_sottotitoli;
        switch (lingua_sottotitoli) {
            case inglese -> {
                this.battute.put(LocalTime.of(0, 1), "Gandaaaaaalf!!!!");
                this.battute.put(LocalTime.of(0, 5), "Run, fools!");
            }
            case italiano -> {
                this.battute.put(LocalTime.of(0, 1), "Gandaaaaaalf!!!!");
                this.battute.put(LocalTime.of(0, 5), "Fuggite sciocchi!");
            }
            case francese -> {
                this.battute.put(LocalTime.of(0, 1), "Gandaaaaaalf!!!!");
                this.battute.put(LocalTime.of(0, 5), "Fuyez, imbéciles!");
            }
        }


    }


    @Override
    public String ottieni_battuta_in_funzione_al_tempo(LocalTime tempo_battuta) {
        return this.battute.get(tempo_battuta);
    }

    @Override
    public Lingua getLingua() {
        return this.lingua;
    }
}
