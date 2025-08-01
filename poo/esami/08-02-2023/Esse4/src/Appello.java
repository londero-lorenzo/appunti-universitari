import java.time.LocalDate;
import java.time.LocalTime;
import java.util.Objects;

/***
 * Mission: gestire l'appello di un corso
 * Conosce: modalità di erogazione (di persona o remoto), tipo (prova finale, parziale), orale si o no
 */


public class Appello {
    private LocalDate data;
    private LocalTime ora;
    private ModalitaErogazione modalitaErogazione;
    private TipoEsame tipoEsame;
    private boolean orale;

    public Appello(LocalDate data, LocalTime ora, ModalitaErogazione modalitaErogazione, TipoEsame tipoEsame, boolean orale) {
        Objects.requireNonNull(data, "Devi inserire una data");
        Objects.requireNonNull(ora, "Devi inserire una ora");
        Objects.requireNonNull(tipoEsame, "Devi inserire una tipo esame");
        Objects.requireNonNull(modalitaErogazione, "Devi inserire una modalitaErogazione");
        this.data = data;
        this.orale = orale;
        this.modalitaErogazione = modalitaErogazione;
        this.tipoEsame = tipoEsame;
        this.orale = orale;
    }

    public LocalDate getData() {
        return data;
    }
}
