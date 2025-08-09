import java.util.ArrayList;

class Solution {
    public int solution(int[] numbers) {

        ArrayList<Integer> list = new ArrayList<>();

        int len = numbers.length;
        for (int i=0; i<(len-1); i++) {
            for(int j=i+1; j<len; j++) {
                int multi = numbers[i]*numbers[j];
                list.add(multi);
            }
        }
        list.sort(Integer::compare);    

        return list.get(list.size()-1);
    }
}