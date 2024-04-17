#include <omp.h>
#include <stdlib.h>
#include <iostream>
#include <stdio.h>
#include <cmath>
#include <windows.h>
using namespace std;

double f(double x)
{
	return (x * x + sin(0.48 * (x + 2))) / exp(x * x + 0.38);
}


int main(int argc, char* argv[])
{
	setlocale(LC_ALL, "Russian");

	const int N = 10000000;
	double a = 0.4; //первая точка
	double b = 0.6; //вторая точка
	ULONGLONG startTime0, endTime0;

	double x;
	double sum = 0;

	startTime0 = GetTickCount64();
	for (int i = 0; i < N; i++) {
		x = a + (b - a) * (i - 0.5) / N;
		sum += f(x);
	}
	double res = sum * (b - a) / N;
	endTime0 = GetTickCount64();

	std::cout << "Вермя работы без OpenMP = " << endTime0 - startTime0;
	std::cout << "\nРезультат вычислений без OpenMP = " << res << "\n";

	//обновления переменных
	sum = 0;
	int i;
	omp_set_dynamic(true); //отключение выбора количества потоков (нитей) по умолчанию

	//omp_set_num_threads(1); //задание числа используемых потоков

	//определение типа переменных блока распараллеливания
	int numTheads, theadNum;
#pragma omp parallel private(numTheads, theadNum)
	{
		numTheads = omp_get_num_threads();
		theadNum = omp_get_thread_num();
		//вывод на экран номера и количества используемых потоков
		printf("OpenMP поток №%d из %d потоков\n", theadNum, numTheads);
	}

	//сохраняем время начала теста
	double startTime = omp_get_wtime();
	//начало области распараллеливания цикла переменная i - приватная, переменная sum обновляется всеми потоками

#pragma omp parallel for default(shared)\
	private(i)\
	reduction (+:sum)
	for (i = 0; i < N; i++)
	{
		x = a + (b - a) * (i - 0.5) / N;
		sum += f(x);
	}
	//сохраняем время окончания теста
	double endTime = omp_get_wtime();

	//выводим сообщения об окончании работы потоками
#pragma omp parallel private(theadNum)
	{
		theadNum = omp_get_thread_num();
		printf("Поток №%d окончил вычисления... \n", theadNum);
	}
	//вычисление итогового результата и печать на экран
	sum = sum * (b - a) / N;
	printf("Результат c OpenMP = %f \n", sum);

	//выводим время работы теста на экран
	printf("Время вычисления c OpenMP = %f\n", endTime - startTime);

}
