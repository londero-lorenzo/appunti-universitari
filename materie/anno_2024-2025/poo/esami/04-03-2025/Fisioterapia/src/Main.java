import Attivita.AttivitaMotoria;
import GruppoFisioterapisti.GruppoFisioterapisti;
import Iniziativa.Iniziativa;
import Palestra.Palestra;
import Paziente.Paziente;
import Sessione.Sessione;

import java.time.LocalDate;
import java.time.LocalTime;
import java.util.Iterator;
import java.util.Map;

public class Main {
    public static void main(String[] args) {

        try {

            GruppoFisioterapisti gruppo1 = new GruppoFisioterapisti();

            Iniziativa TRX = gruppo1.creaIniziativa(AttivitaMotoria.TRX, 3);

            Sessione sessione1_Ginnastica = gruppo1.creaSessione(LocalDate.of(2025, 7, 29), LocalTime.of(9, 0), Palestra.PALESTRA_A);

            TRX.aggiungiSessione(sessione1_Ginnastica);

            Paziente lorenzo = new Paziente("Londero", 21, "Maschio", 69.8, 45);
            Paziente giovanni = new Paziente("Fabro", 24, "Maschio", 70, 45);

            gruppo1.iscriviPartecipante(lorenzo, sessione1_Ginnastica);
            gruppo1.iscriviPartecipante(giovanni, sessione1_Ginnastica);

            sessione1_Ginnastica.impostaPresenza(lorenzo, true);

            Sessione sessione2_Ginnastica = gruppo1.creaSessione(LocalDate.of(2025, 7, 29), LocalTime.of(15, 0), Palestra.PALESTRA_A);

            TRX.aggiungiSessione(sessione2_Ginnastica);

            gruppo1.iscriviPartecipante(lorenzo, sessione2_Ginnastica);

            Paziente lorenzo1 = new Paziente("Londero", 21, "Maschio", 69.8, 45);

            sessione2_Ginnastica.impostaPresenza(lorenzo1, true);

            Map<Sessione, Iterator<Paziente>> dati_partecipazione = gruppo1.ottieniDatiPartecipazione(TRX);


            for (Map.Entry<Sessione, Iterator<Paziente>> entry : dati_partecipazione.entrySet()) {
                Sessione sessione = entry.getKey();
                Iterator<Paziente> pazientes = entry.getValue();

                System.out.println("Pazienti registrati nella sessione del: " + sessione1_Ginnastica.getData() + " delle ore " + sessione1_Ginnastica.getOra() + " per " + TRX.getAttivita().toString());
                while (pazientes.hasNext()) {
                    Paziente paziente = pazientes.next();
                    System.out.println(" - " + paziente.getCodiceFiscale() + (sessione.ottieniPresenza(paziente) ? "" : " | (non presente)"));
                }
            }

        }catch (IllegalArgumentException e){
            e.printStackTrace();
            System.out.println(e.getMessage());
        }

    }
}
