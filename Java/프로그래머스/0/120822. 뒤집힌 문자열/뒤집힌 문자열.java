class Solution {
    public String solution(String my_string) {
        String answer = "";
        answer = new StringBuffer(my_string).reverse().toString();
        return answer;
    }
}