import Canali.Canale;
import Canali.Distributore;
import device.Televisore;
import device.Televisore2in1;
import device.TelevisoreNormale;


public class main {

    public static void main(String[] args) {
        try {
            Distributore distributore = new Distributore();
            Canale italia1 = new Canale("Italia1", 6);
            Canale canale5 = new Canale("Canale5", 5);
            Canale rai2 = new Canale("Rai2", 2);
            distributore.AggiungiCanale(italia1);

            Televisore televisore2in1 = new Televisore2in1();

            televisore2in1.setLuminosita(100);
            televisore2in1.cambiaCanale(italia1);
            //api.cambiaCanale(televisore2in1, canale5, 1);

            Televisore televisoreNormale = new TelevisoreNormale();

            televisoreNormale.setLuminosita(100);
            televisoreNormale.cambiaCanale(rai2);


            ((Televisore2in1) televisore2in1).attiva_2in1();
            televisore2in1.cambiaCanale(rai2, 1);

        }catch (Exception e) {
            e.printStackTrace();
            System.out.println(e.getMessage());
        }
    }
}
