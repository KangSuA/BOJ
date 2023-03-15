#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int n = 0, a = 0, b = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d,%d", &a, &b); //%d 사이에 콤마가 구분자가 된다
		printf("%d\n", a + b);
	}
	return 0;
}