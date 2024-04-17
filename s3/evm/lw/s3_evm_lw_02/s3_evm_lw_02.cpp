#include <cstdio>
#include <cmath>
#include <ctime>
#include <malloc.h>
#include <xmmintrin.h>
#include <windows.h>
#include <locale.h>


void ComputeArrayCpp(float* pArray1, float* pArray2, float* pArray3, float* pResult, int nSize)
{
	float* pSource1 = pArray1;
	float* pSource2 = pArray2;
	float* pSource3 = pArray3;
	float* pDest = pResult;

	for (int i = 0; i < nSize; i++)
	{
		*pDest = (float)(((3.25f * *pSource1) - *pSource1 * *pSource2 + *pSource2 * *pSource3) * 0.75f);

		pSource1++;
		pSource2++;
		pSource3++;
		pDest++;
	}
}
void ComputeArrayCppSSE(float* pArray1, float* pArray2, float* pArray3, float* pResult, int nSize)
{
	int nLoop = nSize / 4;

	__m128 mul1;
	__m128 mul2;
	__m128 mul3;
	__m128 sum;
	__m128 scops;

	__m128* pSrc1 = (__m128*) pArray1;
	__m128* pSrc2 = (__m128*) pArray2;
	__m128* pSrc3 = (__m128*) pArray3;
	__m128* pDest = (__m128*) pResult;


	__m128 m0_3_25 = _mm_set_ps1(3.25f);
	__m128 m1_0_75 = _mm_set_ps1(0.75f);

	for (int i = 0; i < nLoop; i++)
	{
		mul1 = _mm_mul_ps(m0_3_25, *pSrc1);
		mul2 = _mm_mul_ps(*pSrc1, *pSrc2);
		mul3 = _mm_mul_ps(*pSrc2, *pSrc3);

		sum = _mm_add_ps(mul1, mul3);
		scops = _mm_sub_ps(sum, mul2);
		*pDest = _mm_mul_ps(scops, m1_0_75);

		pSrc1++;
		pSrc2++;
		pSrc3++;
		pDest++;
	}
}

void init(float* a, float* b, float* c, int size)
{
	for (int i = 0; i < size; i++)
	{
		a[i] = (float)(rand() % 200 - 100);
		b[i] = (float)(rand() % 200 - 100);
		c[i] = (float)(rand() % 200 - 100);
	}
}

int main()
{

	setlocale(LC_ALL, "Russian");

	const int SIZE = 10000000;

	float* x = (float*)_aligned_malloc(sizeof(float) * SIZE, 16);
	float* y = (float*)_aligned_malloc(sizeof(float) * SIZE, 16);
	float* z = (float*)_aligned_malloc(sizeof(float) * SIZE, 16);
	float* res = (float*)_aligned_malloc(sizeof(float) * SIZE, 16);

	DWORD startTime, endTime;

	init(x, y, z, SIZE);

	startTime = GetTickCount64();

	ComputeArrayCpp(x, y, z, res, SIZE);

	endTime = GetTickCount64();
	printf("Вычисление средствами C++: %d мс\n", endTime - startTime);

	startTime = GetTickCount64();

	ComputeArrayCppSSE(x, y, z, res, SIZE);

	endTime = GetTickCount64();

	printf("Вычисление средствами SSE: %d мс\n", endTime - startTime);

	_aligned_free(x);
	_aligned_free(y);
	_aligned_free(z);
	_aligned_free(res);

	return 0;
}