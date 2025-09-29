package device;

import Canali.Canale;
import enums.Lingua;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Televisore2in1 extends Televisore {

    public Televisore2in1() {
        this.canaliCorrenti = new HashMap<Integer, Canale>();
        this.b2_in_1 = false;
        this.numero_schermi_supportati = 2;
    }

    public void cambiaCanale(Canale canale, Integer schermo) {

        if (schermo < this.getNumeroSchermiSupportati()) {
            if (schermo < this.getDivisioneSchermo())
                super.cambiaCanale(canale, schermo);
            else
                throw new IllegalArgumentException("Il televisore supporta il numero di schermo inserito, ma non ha la funzione 2in1 abilitata");
        }else
            throw new IllegalArgumentException("Il televisore non supporta più di " + this.getNumeroSchermiSupportati() + " schermo");
    }

    public int getDivisioneSchermo() {
        return (this.is2In1Abilitato()) ? this.numero_schermi_supportati : 1;
    }

    @Override
    public void setVolume(int volume) {
        this.volume = volume;
    }

    @Override
    public int getVolume() {
        return this.volume;
    }

    @Override
    public void setLuminosita(int luminosita) {
        this.luminosita = luminosita;
    }

    @Override
    public int getLuminosita() {
        return this.luminosita;
    }

    @Override
    public void setLingua(Lingua lingua) {
        this.lingua = lingua;
    }

    @Override
    public Lingua getLingua() {
        return this.lingua;
    }

    public boolean is2In1Abilitato() {
        return this.b2_in_1;
    }

    public void attiva_2in1() {
        System.out.println("Attivazione schermo 2in1");
        this.b2_in_1 = true;
        // TODO
    }

    public void disattiva_2in1() {
        System.out.println("Disattivazione schermo 2in1");
        this.b2_in_1 = false;
        // TODO
    }
}
