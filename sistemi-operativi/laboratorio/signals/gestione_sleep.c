#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>

void miagestione(int signo) {
	    printf("Received signal: %d\n", signo);
}

int main() {
	struct sigaction sigac;
	sigset_t set;
	int sleeping_time = 15;

	printf("Process PID: %ld\n", (long)getpid());

	sigfillset(&set);

	memset(&sigac, 0, sizeof(sigac));
	sigac.sa_handler = miagestione;
	sigac.sa_mask = set;
	sigac.sa_flags = 0;

	if (sigaction(SIGINT, &sigac, NULL) == -1) {
		perror("sigaction");
		return 1;
	}
	

	printf("\n--- Countdown (%ds): waiting for a signal ---", sleeping_time);

	for (int i = 0; i < sleeping_time; i++) {
		    printf("\n [%2d] second passed", i + 1);
		        sleep(1);
	}

	printf("\n--- Countdown finished ---\n\n");


	printf("Program ended\n");
	return 0;
}
