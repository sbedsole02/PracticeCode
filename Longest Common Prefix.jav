// Write a function to find the longest common prefix string amongst an array of strings.
// If there is no common prefix, return an empty string "".

// Example 1:
// Input: strs = ["flower","flow","flight"]
// Output: "fl"

//I recognize that this solution is sub-optimal but it was a proof of concept looking at different approaches to the same problem.

class Solution {
  public String longestCommonPrefix(String[] strs) {
    Arrays.sort(strs, (a, b) -> Integer.compare(a.length(), b.length()));
    String temp = "";
    ArrayList < Character > temp2 = new ArrayList < Character > ();
    for (int i = 0; i < strs[0].length(); i++) {
      for (int x = 0; x < strs.length; x++) {

        temp2.add(strs[x].charAt(i));
      }
      String res = letterchecker(temp2, temp);
      if (!res.equals("false")) {
        temp = res;
        temp2.clear();
      }
    }
    return temp;
  }
  public static String letterchecker(ArrayList < Character > checkedarray, String finaloutput) {
    Character mainletter = checkedarray.get(0);
    for (int index2 = 1; index2 < checkedarray.size(); index2++) {
      Character letter2 = checkedarray.get(index2);
      if (letter2 != mainletter) {
        return "false";
      }
    }
    finaloutput = finaloutput + mainletter;
    return finaloutput;
  }
}
