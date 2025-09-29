package device;

import Canali.Canale;
import enums.Lingua;

import java.util.List;
import java.util.Map;

/***
 * Mission: mettere a disposizione i parametri della televisione alle classi che estenderanno questa classe
 * Conosce: volume, luminosità, lingua, se ha la modalità 2in1 oppure no
 * Sa fare: settare i vari parametri del televisore
 *
 */

public abstract class Televisore extends VideoRegistratore {
    protected int volume;
    protected int luminosita;
    protected Lingua lingua;
    protected boolean b2_in_1;
    protected int numero_schermi_supportati;

    protected Map<Integer, Canale> canaliCorrenti;

    protected List<Canale> canali;

    public List<Canale> getCanali() {
        return canali;
    }

    public void cambiaCanale(Canale canale, Integer schermo) {
        if (schermo < this.getNumeroSchermiSupportati())
            this.canaliCorrenti.put(schermo, canale);
        else
            throw new IllegalArgumentException("Il televisore non supporta più di " + this.getNumeroSchermiSupportati() + " schermo");
    }

    public void cambiaCanale(Canale canale) throws Exception{
        if (this.getDivisioneSchermo() != 1){
            throw new Exception("Immettere in quale schermo cambiare canale");
        }else{
            this.cambiaCanale(canale, 0);
        }
    }

    public int getNumeroSchermiSupportati(){
        return this.numero_schermi_supportati;
    }

    /*
    public void cambiaCanale(Canale canale, Integer schermo) {
        if (schermo < this.getNumeroSchermiSupportati())
            if (this instanceof Televisore2in1){
                if (this.is2In1Abilitato())
                    this.cambiaCanale(schermo, canale);
                else
                    throw new IllegalArgumentException("Il televisore supporta il numero di schermo inserito, ma non ha la funzione 2in1 abilitata");
            }else{

                this.cambiaCanale(0, canale);
            }
        else
            throw new IllegalArgumentException("Il televisore non supporta più di " + this.getNumeroSchermiSupportati() + " schermo");
    }

    public void cambiaCanale(Canale canale) throws Exception {
        if (this instanceof Televisore2in1 && this.is2In1Abilitato()){
            throw new Exception("Immettere in quale schermo cambiare canale");
        }else{
            this.cambiaCanale(0, canale);
        }
    }

     */

    public abstract int getDivisioneSchermo();

    public abstract void setVolume(int volume);

    public abstract int getVolume();

    public abstract void setLuminosita(int luminosita);

    public abstract int getLuminosita();

    public abstract void setLingua(Lingua lingua);

    public abstract Lingua getLingua();



}
