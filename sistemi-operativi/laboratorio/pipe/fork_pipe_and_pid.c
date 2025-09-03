#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int pipefd[2];
int pid;

void P1(){
	close(pipefd[0]);
	pid = getpid();
	printf("[P1] Il mio PID è: %d\n", pid);
	write(pipefd[1], &pid, sizeof(int));
	close(pipefd[1]);
}

void P2(){
	close(pipefd[1]);
	if (read(pipefd[0], &pid, sizeof(int)) < 0){
		perror("read");
		 exit(EXIT_FAILURE);
	}
	printf("[P2] Il PID di mio fratello è: %d\n", pid);
	close(pipefd[0]);
}

int main(){

	if (pipe(pipefd) == -1) {
		perror("pipe");
		return EXIT_FAILURE;
	}
	
	for (int i = 0; i < 2; i++){
		if (fork() == 0){
			if (i == 0) P1();
			if (i == 1) P2();
			return EXIT_SUCCESS;
		}
	}

	wait(NULL);

	return EXIT_SUCCESS;
}
