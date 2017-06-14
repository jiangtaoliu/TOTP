#include <stdio.h>

int process_int(int sum, int remain_time)
{
	int a;

	if(remain_time == 0)
		return sum;

	scanf("%d", &a);
	if(a < 0)
		return process_int(sum, remain_time-1);
	else
		return process_int(sum + a*a, remain_time-1);
}

void process_case(int remain_time)
{
	int X;
	int ans;

	if(remain_time == 0)
		return;

	scanf("%d", &X);
	ans = process_int(0, X);
	printf("%d\n", ans);

	process_case(remain_time-1);
}



int main()
{
	int N;
	scanf("%d", &N);
	process_case(N);

	return 0;
}