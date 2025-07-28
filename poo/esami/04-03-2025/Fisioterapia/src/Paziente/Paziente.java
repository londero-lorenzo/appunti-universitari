package Paziente;

import java.util.ArrayList;
import java.util.List;

/**
 * Mission: registrare i dati di un iscritto a un certo corso
 * Conosce: dati anagrafici dell'iscritto e condizioni mediche
 * Sa fare: restituire i dati relativi all'iscritto
 */


public class Paziente {
    private String codiceFiscale;
    private int eta;
    private String sesso;
    private double peso;
    private double body_mass_index;
    private List<String> patologie = new ArrayList<>();

    public Paziente(String codiceFiscale, int eta, String sesso, double peso, double bodyMassIndex) {
        this.codiceFiscale = codiceFiscale;
        this.eta = eta;
        this.sesso = sesso;
        this.peso = peso;
        this.body_mass_index = body_mass_index;
    }

    public Paziente(PazienteBuilder pazienteBuilder) {
        this.codiceFiscale = pazienteBuilder.getCodiceFiscale();
        this.eta = pazienteBuilder.getEta();
        this.sesso = pazienteBuilder.getSesso();
        this.peso = pazienteBuilder.getPeso();
        this.body_mass_index = pazienteBuilder.getBodyMassIndex();
    }

    @Override
    public boolean equals(Object paziente) {
        if (paziente instanceof Paziente) {
            return this.codiceFiscale.equals(( (Paziente) paziente).getCodiceFiscale());
        }
        return false;
    }

    @Override
    public int hashCode() {
        return this.codiceFiscale.hashCode();
    }

    public String getCodiceFiscale() {
        return codiceFiscale;
    }

    public int getEta() {
        return eta;
    }

    public String getSesso() {
        return sesso;
    }

    public double getPeso() {
        return peso;
    }

    public double getBodyMassIndex() {
        return body_mass_index;
    }

    public List<String> getPatologie() {
        return patologie;
    }

}
