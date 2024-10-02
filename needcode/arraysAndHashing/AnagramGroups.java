package arraysAndHashing;

import java.util.*;
import java.util.stream.Collectors;

class AnagramGroups {

    //sort all strings and find the same ones
    //HashMap <String, List> = new HashMap<>()
    // (K, V) = (sortedStr, [list of orginal strings])
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String, List<String>> stringMap = new HashMap<>();
        for(String str: strs){
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);
            String sortedStr = new String(charArray);
            if(!stringMap.containsKey(sortedStr)){
                stringMap.put(sortedStr, new ArrayList<>());

            }
            stringMap.get(sortedStr).add(str);
        }

        return stringMap.values().stream()
                .collect(Collectors.toList());


    };


    public static void main(String[] args) {
        String[] strs = {"act","pots","tops","cat","stop","hat"};
        AnagramGroups anagramGroups = new AnagramGroups();
        List<List<String>> res =  anagramGroups.groupAnagrams(strs);
        System.out.println(res);
    }

}

