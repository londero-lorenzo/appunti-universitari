package Sessione;

import Palestra.Palestra;
import Paziente.Paziente;
import exceptions.PazienteGiaPresente;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.util.*;

/***
 * Mission: gestire una sessione relativa a un'iniziativa
 * Conosce: data e ora di inizio e fine, la palestra
 * Cosa sa fare: registrare un paziente nella sessione
 */
public class Sessione {
    private LocalDate data;
    private LocalTime ora;
    private Palestra palestra;
    private Map<Paziente, Boolean> iscritti = new HashMap<Paziente, Boolean>();

    public Sessione(LocalDate data, LocalTime ora, Palestra palestra) {
        this.data = data;
        this.ora = ora;
        this.palestra = palestra;
    }


    /**
     * Pre-condizione:
     *  - paziente è un oggetto valido Paziente
     *
     * Post-condizione:
     *  - viene aggiunto il paziente nella lista degli iscritti e la sua presenza viene impostata a false
     *
     * Throws:
     *  - PazienteGiaPresente, se il paziente è già stato iscritto nella sessione
     * @param paziente oggetto Paziente valido
     * @throws PazienteGiaPresente se il paziente è già stato inserito
     */
    public void registraPaziente(Paziente paziente) throws PazienteGiaPresente {
        if (this.iscritti.containsKey(paziente))
            throw new PazienteGiaPresente("Il paziente " + paziente.getCodiceFiscale() + " è già presente nella sessione del " + this.getDateTime());
        this.iscritti.put(paziente, false);
    }

    /**
     * Override del metodo equals
     *  - utilizzato come nuovo metodo di uguaglianza
     * @param object
     * @return
     */

    @Override
    public boolean equals(Object object) {
        if (object instanceof Sessione) {
            return this.getDateTime().equals(( (Sessione) object).getDateTime());
        }
        return false;
    }

    @Override
    public int hashCode() {
        return this.getDateTime().hashCode();
    }

    public Iterator<Paziente> getPazientiIterator() {
        return iscritti.keySet().iterator();
    }

    /**
     * Pre-condizione:
     *  - Paziente: oggetto Paziente valido,
     *  - presente: valore booleano che indica se il paziente è presente o meno
     *
     * Post-condizione:
     *  - sovrascrive la voce paziente nella lista dei pazienti iscritti con il nuovo valore di presenza
     *
     * @param paziente oggetto Paziente, valido
     * @param presente boolean, nuovo valore di presenza
     */

    public void impostaPresenza(Paziente paziente, boolean presente){
        this.iscritti.put(paziente, presente);
    }

    /***
     * Pre-condizione: paziente
     * Post-condizione: non modifica la sessione e restituisce la presenza del paziente
     * @param paziente
     * @return
     */

    public Boolean ottieniPresenza(Paziente paziente) {
        return iscritti.get(paziente);
    }

    public LocalDate getData() {
        return data;
    }
    public LocalTime getOra() {
        return ora;
    }
    public Palestra getPalestra() {
        return palestra;
    }

    public LocalDateTime getDateTime() {
        return LocalDateTime.of(data, ora);

    }






}
