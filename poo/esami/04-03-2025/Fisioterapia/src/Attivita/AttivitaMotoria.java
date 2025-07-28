package Attivita;

public enum AttivitaMotoria {
    GINNASTICA_ANTALGICA {
        public String toString() {
            return "GINNASTICA_ANTALGICA";
        }
    },
    PILATES{
        public String toString() {
            return "Pilates";
        }
    },
    CORPO_LIBERO_LV1{
        public String toString() {
            return "Corpo libero livello 1";
        }
    },
    CORPO_LIBERO_LV2{
        public String toString() {
            return "Corpo libero livello 2";
        }
    },
    CORPO_LIBERO_LV3{
        public String toString() {
            return "Corpo libero livello 3";
        }
    },
    TRX{
        public String toString() {
            return "Trx";
        }
    };

    public abstract String toString();
}
