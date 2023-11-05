////////////////////////////////////////////////////////////////////////////////
///// CODE
////////////////////////////////////////////////////////////////////////////////

// CPP Program to multiply two matrix using pthreads
#include <bits/stdc++.h>
using namespace std;

// maximum size of matrix
#define MAX 4

// maximum number of threads
#define MAX_THREAD 4

int matA[MAX][MAX];
int matB[MAX][MAX];
int matC[MAX][MAX];
int step_i = 0;

void* multi(void* arg)
{
	int i = step_i++; //i denotes row number of resultant matC

	for (int j = 0; j < MAX; j++) 
	for (int k = 0; k < MAX; k++) 
		matC[i][j] += matA[i][k] * matB[k][j];
}

// Driver Code
int main()
{
	// Generating random values in matA and matB
	for (int i = 0; i < MAX; i++) {
		for (int j = 0; j < MAX; j++) {
			matA[i][j] = rand() % 10;
			matB[i][j] = rand() % 10;
		}
	}

	// Displaying matA
	cout << endl
		<< "Matrix A" << endl;
	for (int i = 0; i < MAX; i++) {
		for (int j = 0; j < MAX; j++) 
			cout << matA[i][j] << " ";
		cout << endl;
	}

	// Displaying matB
	cout << endl
		<< "Matrix B" << endl;
	for (int i = 0; i < MAX; i++) {
		for (int j = 0; j < MAX; j++) 
			cout << matB[i][j] << " ";	 
		cout << endl;
	}

	// declaring four threads
	pthread_t threads[MAX_THREAD];

	// Creating four threads, each evaluating its own part
	for (int i = 0; i < MAX_THREAD; i++) {
		int* p;
		pthread_create(&threads[i], NULL, multi, (void*)(p));
	}

	// joining and waiting for all threads to complete
	for (int i = 0; i < MAX_THREAD; i++) 
		pthread_join(threads[i], NULL); 

	// Displaying the result matrix
	cout << endl
		<< "Multiplication of A and B" << endl;
	for (int i = 0; i < MAX; i++) {
		for (int j = 0; j < MAX; j++) 
			cout << matC[i][j] << " ";	 
		cout << endl;
	}
	return 0;
}

////////////////////////////////////////////////////////////////////////////////
///// OUTPUT
////////////////////////////////////////////////////////////////////////////////

/*

Matrix A
7 2 6 8 
7 0 6 6 
6 1 7 5 
3 7 7 2 
Matrix B
3 5 3 6 
5 7 5 8 
8 9 4 9 
6 5 7 2 
Multiplication of A and B
127 143 111 128 
105 119 87 108 
109 125 86 117 
112 137 86 141 

*/