#include <iostream>
int main(void)
{
	int a1, a2;
	int b1, b2, b3;
	int a3, a4, a5, a6;

	std::cin >> a1 >> a2;

	b1 = a2 / 100;
	b2 = a2 / 10 - b1 * 10;
	b3 = a2 - (b1 * 100 + b2 * 10);

	a3 = a1 * b3;
	a4 = a1 * b2;
	a5 = a1 * b1;
	a6 = a1 * a2;

	std::cout << a3 << std::endl;
	std::cout << a4 << std::endl;
	std::cout << a5 << std::endl;
	std::cout << a6 << std::endl;

	return 0;
}