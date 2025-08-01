package trasmissione;

import enums.Lingua;

import java.time.LocalTime;

public abstract class Sottotitoli {

    public abstract String ottieni_battuta_in_funzione_al_tempo(LocalTime tempo_battuta);

    public abstract Lingua getLingua();
    /*



    lingua(sottotitolo);

    private String sottotitolo = Lingua.inglese(action_time); // s = "home"
    LocalTime session = LocalTime.parse("14:21.629");
    System.out.println("session: " + session);
     */

}
