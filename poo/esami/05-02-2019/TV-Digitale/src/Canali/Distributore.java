package Canali;

import java.util.HashMap;
import java.util.Map;

/***
 * Missione: gestire tutti quanti i canali in modo tale da poter aggiornare la lista
 * Conosce: i canali e il numero di riferimento
 * Cosa sa fare: aggiunge, aggiorna ed elimina determinati canali
 */

public class Distributore {
    private Map<Integer, Canale> canali = new HashMap<>();

    /***
     * Pre-condizioni:
     *  il numero del canale da aggiungere non deve essere già utilizzato da un altro canale
     *
     */
    public void AggiungiCanale(Canale canale) {
        this.canali.put(canale.getNumero(), canale);
    }


}
