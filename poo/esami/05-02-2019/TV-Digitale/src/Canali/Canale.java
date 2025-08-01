package Canali;

import trasmissione.Trasmissione;

import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class Canale {
    private String nome;

    private int numero;

    private Map<LocalDateTime, Trasmissione> trasmissioni = new HashMap<>();

    public Canale(String nome, int numero) {
        this.nome = nome;
        this.numero = numero;
    }

    /***
     * Aggiungo una trasmissione nuova
     * solleva un IllegalArgumentException se la trasmissione è gia in lista
     *
     * @param trasmissione
     */

    public void aggiungiTrasmissione(Trasmissione trasmissione){
        LocalDateTime date = LocalDateTime.of(trasmissione.getData(), trasmissione.getOra());
        if (trasmissioni.get(date) != null)
            throw new IllegalArgumentException("Trasmissione già presente nel palinsesto " + date);
        trasmissioni.put(date, trasmissione);
    }

    /***
     * Rimuovo la trasmissione dal palinsesto
     * solleva un IllegalArgumentException se la trasmissione non è presente nella lista
     * @param tempo_onda_canale
     */

    public void eliminaTrasmissione(LocalDateTime tempo_onda_canale){
        if (trasmissioni.remove(tempo_onda_canale) == null)
            throw new IllegalArgumentException("Trasmissione non trovata per l'orario inserito: " + tempo_onda_canale);
    }



    public int getNumero(){
        return this.numero;
    }


}
