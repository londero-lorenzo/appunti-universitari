#include <stdio.h> // for i/o
#include <stdlib.h> // for exit declaration
#include <unistd.h> // for process operations
#include <sys/wait.h> // for waitpid 
#include <signal.h>
#include <sys/types.h>

int main(int argc, char *argv[]) {
	pid_t cpid, w;
	int status;

	cpid = fork();
	if (cpid == -1) {
		perror("fork");
		exit(EXIT_FAILURE);
	}

	if (cpid == 0) { /* Code executed by child */
		printf("Chid PID is %ld\n", (long) getpid());
		if (argc == 1)
			pause();
		exit(atoi(argv[1]));
	} else {
		do {
			w = waitpid(cpid, &status, WUNTRACED | WCONTINUED);
			if (w == -1) {
				perror("waitpid"); exit(EXIT_FAILURE);
			}
			if (WIFEXITED(status))
				printf("exited, status=%d\n", WEXITSTATUS(status));
			else if (WIFSIGNALED(status))
				printf("killed by signal %d\n", WTERMSIG(status));
			else if (WIFSTOPPED(status))
				printf("stopped by signal %d\n", WSTOPSIG(status));
			else if (WIFCONTINUED(status))
				printf("continued\n");
		} while(!WIFEXITED(status) && !WIFSIGNALED(status));
		exit(EXIT_SUCCESS);
		}
}
