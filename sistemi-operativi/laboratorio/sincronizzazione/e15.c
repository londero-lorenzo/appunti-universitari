/*

=============== INTESTAZIONE ESERCIZIO ===================

Si considerino tre processi P1, P2 e S. Il processo P1 ripete indefinitamente un ciclo in cui genera un
numero x (con una chiamata ad una data funzione: x = genera();) e poi comunica il valore x cos`ı ottenuto
al processo S. Il processo P2 opera come il processo P1.
Il processo S ripete indefinitamente un ciclo in cui acquisisce i due valori generati da P1 e P2, li somma e
consuma il risultato chiamando una funzione consuma(somma);. Poi ripete il ciclo per sommare altri due
numeri.
Realizzare la sincronizzazione e la comunicazione tra i tre processi in modo che nessun numero generato vada
perso e che il numero prodotto da P1 nel suo ciclo i-esimo sia sommato con il numero prodotto da P2 nel suo
ciclo i-esimo.


*/


#include <stdlib.h>
#include <stdio.h>

#include <time.h>
#include <unistd.h>     // fork, getpid, sleep
#include <sys/mman.h>   // wait
#include <semaphore.h>  // sem_t, sem_init, sem_wait, sem_post


sem_t *gen_p1, *gen_p2, *gen;

int *x; //shared

int genera(){
    return rand() % 100;
}

void consuma(int somma){
    printf("La somma è %d\n", somma);

}

// Processo P1
void P1() {
    srand(time(NULL) ^ getpid());
    printf("Processo 1 avviato. PID: %d\n", getpid());
    while (1) {
        printf("[P1] Waiting...\n");
        sem_wait(gen_p1);            // aspetta segnale dal collettore
        *x = genera();           // genera valore
        printf("[P1] Generato: %d\n", *x);
        sem_post(gen);               // segnala al collettore
    }
}

// Processo P2
void P2() {
    srand(time(NULL) ^ getpid());
    printf("Processo 2 avviato. PID: %d\n", getpid());
    while (1) {
        printf("[P2] Waiting...\n");
        sem_wait(gen_p2);            // aspetta segnale dal collettore
        *x = genera();           // genera valore
        printf("[P2] Generato: %d\n", *x);
        sem_post(gen);               // segnala al collettore
    }
}

// Processo collettore S
void S() {
    while (1) {
        int somma = 0;

        printf("[S] Invio segnale a P1...\n");
        sem_post(gen_p1);
        sem_wait(gen);      // aspetta P1
        somma += *x;

        printf("[S] Invio segnale a P2...\n");
        sem_post(gen_p2);
        sem_wait(gen);      // aspetta P2
        somma += *x;

        printf("[S] Somma ricevuta = %d\n\n", somma);
        sleep(1);
    }
}

int main(){
    
    gen_p1 = mmap(NULL, sizeof(sem_t), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
    gen_p2 = mmap(NULL, sizeof(sem_t), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
    gen    = mmap(NULL, sizeof(sem_t), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
    x      = mmap(NULL, sizeof(int), PROT_READ | PROT_WRITE,  MAP_SHARED | MAP_ANONYMOUS, -1, 0);


    if (gen_p1 == MAP_FAILED || gen_p2 == MAP_FAILED || gen == MAP_FAILED || x == MAP_FAILED) {
        perror("mmap");
        exit(1);
    }

    sem_init(gen_p1, 1, 0);
    sem_init(gen_p2, 1, 0);
    sem_init(gen, 1, 0);

    // Creiamo i figli
    for (int i = 0; i < 2; i++) {
        if (fork() == 0) {
            if (i == 0) P1();
            if (i == 1) P2();
            exit(0);
        }
    }
    printf("Invocazione processo collettore. PID: %d\n", getpid());
    S();
}
