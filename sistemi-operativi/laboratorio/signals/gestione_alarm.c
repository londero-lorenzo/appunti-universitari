#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>

void miagestione(int signo) {
    if (signo == SIGINT) {
        printf("\n[Handler] Received SIGINT (%d)\n", signo);
    } else if (signo == SIGALRM) {
        printf("\n[Handler] Received SIGALRM (%d) -> alarm triggered!\n", signo);
    } else if(signo == SIGCONT) {
	printf("\n[Handler] Process resumed after a STOP\n");
    } else {
        printf("\n[Handler] Received signal: %d\n", signo);
    }
}

int main() {
    struct sigaction sigac;
    sigset_t set;
    int sleeping_time = 30;

    printf("Process PID: %ld\n", (long)getpid());

    sigfillset(&set);

    memset(&sigac, 0, sizeof(sigac));
    sigac.sa_handler = miagestione;
    sigac.sa_mask = set;
    sigac.sa_flags = 0;

    // handler per SIGINT
    if (sigaction(SIGINT, &sigac, NULL) == -1) {
        perror("sigaction");
        return 1;
    }
    // handler per SIGALRM
    if (sigaction(SIGALRM, &sigac, NULL) == -1) {
        perror("sigaction");
        return 1;
    }

    // handler per SIGCONT
    if (sigaction(SIGCONT, &sigac, NULL) == -1) {
        perror("sigaction");
        return 1;
    }

    printf("\n--- Countdown (%ds): waiting for a signal ---", sleeping_time);

    // imposta un alarm dopo metà sleep time secondi
    alarm((int) sleeping_time / 2);

    for (int i = 0; i < sleeping_time; i++) {
        printf("\n [%2d] second passed", i + 1);
        sleep(1);
    }

    printf("\n--- Countdown finished ---\n\n");

    printf("Program ended\n");
    return 0;
}
