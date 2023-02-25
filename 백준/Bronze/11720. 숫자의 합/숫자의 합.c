#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	char c[100] = { 0, };
	int N = 0, sum = 0;
	scanf("%d", &N);
	scanf("%s", c);
	for (int i = 0; i < N; i++)
	{
		sum += c[i] - 48;
	}
	printf("%d\n", sum);
	return 0;
}