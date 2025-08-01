package device;

import Canali.Canale;
import enums.Lingua;

import java.util.HashMap;

public class TelevisoreNormale extends Televisore {

    public TelevisoreNormale() {
        this.canaliCorrenti = new HashMap<Integer, Canale>();
        this.numero_schermi_supportati = 1;
    }

    public int getDivisioneSchermo() {
        return 1;
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

}
