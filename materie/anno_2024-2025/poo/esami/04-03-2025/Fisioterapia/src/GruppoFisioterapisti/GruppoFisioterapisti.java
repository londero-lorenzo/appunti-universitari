package GruppoFisioterapisti;

import Attivita.AttivitaMotoria;
import Iniziativa.Iniziativa;
import Palestra.Palestra;
import Paziente.Paziente;
import Sessione.Sessione;
import exceptions.SessioneNonTrovata;

import java.time.LocalDate;
import java.time.LocalTime;
import java.util.*;

/***
 * Mission: gestire la pianificazione delle iniziative, l'iscrizione alle varie sessioni e estrarre i dati di partecipazione
 *
 * Cosa sa fare: Sa pianificare le iniziative, iscrive i partecipanti alle sessioni e sa estrapolare dati di partecipazione
 *
 * Cosa conosce: lista di iniziative;
 */


public class GruppoFisioterapisti {

    private List<Iniziativa> iniziative = new ArrayList<>();

    /***
     *  Pre-condizioni: data, ora e la palestra
     *  Post-condizioni: restituisce una sessione
     */
    public Sessione creaSessione(LocalDate data, LocalTime time, Palestra palestra){
        return new Sessione(data, time, palestra);
    }

    /***
     *  Pre-condizioni:
     *      -tipo di attività
     *      -quanti giorni alla settimana viene fatta
     *      -sessioni
     *
     *  Post-condizioni:
     *      - pianifica un'iniziativa con i parametri inseriti
     */

    /*
        sessione1 = g.creaSessione(LocalData.of(4), LocalTime.of(13, 10), SUD);
        sessione2 = g.creaSessione(LocalData.of(4), LocalTime.of(15, 10), SUD);
        sessione3 = g.creaSessione(LocalData.of(4), LocalTime.of(17, 10), SUD);
        List<Sessione> l_sessioni= new ArrayList<>();
        l_sessioni.add(sessione1);
        l_sessioni.add(sessione2);
        l_sessioni.add(sessione3);


        Iniziativa i = g.creaIniziativa(CORPO_LIBERO_LV3, 3, l_sessioni)

        sessione4 = g.creaSessione(LocalData.of(4), LocalTime.of(18, 10), SUD);

        i.aggiungiSessione(sessione4)
     */

    public Iniziativa creaIniziativa(AttivitaMotoria attivita, int frequenzaSettimanale, Sessione ...sessioni) {
        Iniziativa iniziativa = new Iniziativa(attivita, frequenzaSettimanale);
        for (Sessione sessione : sessioni)
            iniziativa.aggiungiSessione(sessione);

        this.iniziative.add(iniziativa);

        return iniziativa;
    }

    /***
     *  Pre-condizione: paziente e sessione
     *
     *  Post-condizione: iscrive il paziente alla sessione desiderata della rispettiva iniziativa
     *
     *  throw
     *      - SessioneNonTrovata, se la sessione non è stata trovata all'interno di nessuna iniziativa
     *
     * @throws SessioneNonTrovata
     */


    public void iscriviPartecipante(Paziente paziente, Sessione sessione) {
        Iterator<Iniziativa> it = iniziative.iterator();
        while(it.hasNext()){
            Iniziativa iniziativa = it.next();
            Iterator<Sessione> it_2 = iniziativa.getSessioniIterator();
            while (it_2.hasNext()){
                Sessione sessione_2 = it_2.next();
                if (sessione_2.equals(sessione)){
                    sessione_2.registraPaziente(paziente);
                    return;
                }
            }
        }
        throw new SessioneNonTrovata("La sessione " + sessione.getDateTime() + " non è strata trova in nessuna iniziativa del gruppo");


    }

    /***
     * Pre-condizioni: iniziativa
     * Post-condizioni: restituisce una mappa contenete la sessione e i relativi pazienti presenti
     *
     */

    public Map<Sessione, Iterator<Paziente>> ottieniDatiPartecipazione(Iniziativa iniziativa){
        Iterator<Sessione> iterator = iniziativa.getSessioniIterator();
        Map<Sessione, Iterator<Paziente>> map = new HashMap<>();

        while(iterator.hasNext()){
            Sessione sessione = iterator.next();
            map.put(sessione, sessione.getPazientiIterator());
        }
        return map;
    }



}
