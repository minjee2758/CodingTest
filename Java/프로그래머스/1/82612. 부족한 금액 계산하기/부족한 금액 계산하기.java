class Solution {
    public long solution(int price, int money, int count) {
        long answer = -1;
        long total = 0;

        for (int i=0; i< count; i++) {
            int priceIncre = price * (i+1);
            total += priceIncre;
        }

        answer = total - money;
        if (answer <= 0) {
            answer = 0;
        }

        return answer;
    }
}