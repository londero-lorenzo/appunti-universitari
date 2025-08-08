package Paziente;

import java.util.ArrayList;
import java.util.List;

public class PazienteBuilder {
    private String codiceFiscale;
    private int eta;
    private String sesso;
    private double peso;
    private double body_mass_index;
    private List<String> patologie = new ArrayList<>();

    public String getCodiceFiscale() {
        return codiceFiscale;
    }

    public int getEta(){
        return eta;
    }

    public String getSesso(){
        return sesso;
    }

    public double getPeso(){
        return peso;
    }

    public double getBodyMassIndex(){
        return body_mass_index;
    }

    public PazienteBuilder codiceFiscale(String codiceFiscale) {
        this.codiceFiscale = codiceFiscale;
        return this;
    }

    public PazienteBuilder eta(int eta) {
        this.eta = eta;
        return this;
    }

    public PazienteBuilder sesso(String sesso) {
        this.sesso = sesso;
        return this;
    }

    public PazienteBuilder peso(double peso) {
        this.peso = peso;
        return this;
    }

    public PazienteBuilder body_mass_index(double body_mass_index) {
        this.body_mass_index = body_mass_index;
        return this;
    }

    public Paziente build(){
        return new Paziente(this);
    }
}
