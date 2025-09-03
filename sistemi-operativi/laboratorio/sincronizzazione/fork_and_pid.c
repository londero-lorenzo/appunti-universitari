#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <unistd.h>
#include <semaphore.h>
#include <sys/wait.h>

sem_t *sem;
long *pid;


void P1(){
	*pid = getpid();
	printf("Il mio PID di è: %ld\n", *pid);
	sem_post(sem);
}

void P2(){
	sem_wait(sem);
	printf("Il PID di mio fratello è: %ld\n", *pid);
}


int main(){
	sem = mmap(NULL, sizeof(sem_t), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
	pid = mmap(NULL, sizeof(long), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);

	if (sem == MAP_FAILED || pid == MAP_FAILED){
		perror("mmap");
		exit(1);
	}

	sem_init(sem, 1, 0);

	for (int i = 0; i < 2; i++){
		if (fork() == 0){
			if (i == 0) P1();
			if (i == 1) P2();
			exit(0);
		}
	}
	wait(NULL);
	exit(EXIT_SUCCESS);

}
