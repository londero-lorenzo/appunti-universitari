package device;


import trasmissione.Trasmissione;

import java.util.ArrayList;
import java.util.List;

public class VideoRegistratore {
    private final List<Trasmissione> trasmissioni_da_registrare = new ArrayList<Trasmissione>();

    public void aggiungiTrasmissione(Trasmissione trasmissione){

        this.trasmissioni_da_registrare.add(trasmissione);
    }

    public List<Trasmissione> getTrasmissioni_da_registrare() {
        return this.trasmissioni_da_registrare;
    }
}
