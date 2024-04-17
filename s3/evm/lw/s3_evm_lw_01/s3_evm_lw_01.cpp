#include <iostream>
#include <windows.h>
#include <stdio.h>
#include <cmath>
using namespace std;

double function()
{
	double func = 0;
	int x;
	for (int i = 1; i < 100000000; i++)
	{
		x = rand() % 9 + 1;
		func += pow((x * sin(i * x)), 3);
	}
	return func;
}

int main()
{
	setlocale(LC_ALL, "Russian");
	DWORD startTime, endTime;
	startTime = GetTickCount64();
	function();
	endTime = GetTickCount64();
	cout << "Время вычисления: " << endTime - startTime;
	return 0;
}