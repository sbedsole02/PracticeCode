class Solution {
    public boolean isPalindrome(int x) {
    String s=Integer.toString(x);
        for(int i = 0, j = s.length()-1; i < s.length()/2; i++, j--){
            char ch = s.charAt(i);
            char c2 = s.charAt(j);
            System.out.println(Character.compare(ch,c2)==0);
            if(Character.compare(ch,c2)!=0){
                return false;
            }
        }
    return true;
        }
}
