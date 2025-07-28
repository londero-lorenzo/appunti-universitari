package Iniziativa;

import Attivita.AttivitaMotoria;
import Palestra.Palestra;
import Paziente.Paziente;
import Sessione.Sessione;
import exceptions.LimiteNumeroSessioniSettimanaliSuperato;
import exceptions.SessioneGiaEsistente;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * Mission: registrare i dati relativi al corso che un paziente deve seguire
 * Conosce: l'attività motoria, quanti giorni a settimana deve fare, data di inizio e data fine
 * Sa fare: restituire i dati relativi al corso
 */

public class Iniziativa {
    private AttivitaMotoria attivita;
    private int frequenzaSettimanale;
    private List<Sessione> sessioni = new ArrayList<>();


    public Iniziativa(AttivitaMotoria attivita, int frequenzaSettimanale) {
        this.attivita = attivita;
        this.frequenzaSettimanale = frequenzaSettimanale;
    }

    /***
     * Pre-condizioni:
     *  - non devono essere gia presenti nella lista sessioni la stessa data, ora e palestra
     *
     * Post-condizioni: aggiunge una sessione all'iniziativa
     *
     * Throws:
     *  - IllegalArgumentException: se il numero di sessioni supera la frequenza settimanale
     *
     */
    public void aggiungiSessione(Sessione sessione) throws  LimiteNumeroSessioniSettimanaliSuperato, SessioneGiaEsistente {
        if (sessioni.size() >= frequenzaSettimanale) {
            throw new LimiteNumeroSessioniSettimanaliSuperato("Hai superato il limite di sessioni settimanali");
        }
        for (Sessione s : sessioni) {
            if (s.getData().equals(sessione.getData()) && s.getOra().equals(sessione.getOra()) && s.getPalestra().equals(sessione.getPalestra()))
                throw new SessioneGiaEsistente("Hai gia inserito questa sessione");
        }
        sessioni.add(sessione);
    }

    // Getters
    public AttivitaMotoria getAttivita() {
        return attivita;
    }

    public int getFrequenzaSettimanale() {
        return frequenzaSettimanale;
    }

    public Iterator<Sessione> getSessioniIterator() {
        return sessioni.iterator();
    }

    /*
    public class api {
        public static void iscriviPaziente(Iniziativa in, String codice_sessione, Paziente p){
            s.registraPaziente(p)
        }

     */

}
