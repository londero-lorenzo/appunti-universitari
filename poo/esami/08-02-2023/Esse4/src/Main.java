public class Main {
    public static void main(String[] args) {
        Studente stud = new Studente("Giovanni", "Fabro", 149182, AnnoCorso.SECONDO);
        stud.aggiungiCorsiAttuali(new Corso("POO", "Brajnik", 9, AnnoCorso.SECONDO));

    }
}
