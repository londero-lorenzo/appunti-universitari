import java.time.LocalDate;
import java.time.LocalTime;

public class Orale {
    private LocalTime ora;
    private LocalDate data;
    private boolean oraleSiNo;

    public Orale(LocalDate data, LocalTime ora, boolean oraleSiNo) {
        if (data == null ||  ora == null) throw new IllegalArgumentException("Data e ora devono sempre essere definiti");
        this.ora = ora;
        this.data = data;
        this.oraleSiNo = oraleSiNo;
    }

    public LocalTime getOra() {
        return ora;
    }

    public LocalDate getData() {
        return data;
    }

    public boolean isOraleSiNo() {
        return oraleSiNo;
    }

}
