string s = "abcabcbb"


int lengthOfLongestSubstring(string s) {
    string max_subtring = {};
    string substring = {};
    int max_length = 0;
    int length = 0;
    int i,j;
    int step = 0;
    while(step!= s.size()){
        length = 0;
        substring = {};
        for(i = step;i<s.size();i++){
            for(j = 0; j < substring.size(); j++){
                if(s[i] == substring[j])
                    break;
            }
            
            if(j == substring.size()){
                substring += s[i];
                length++;
            }
            else
                break;
        }
        if(length > max_length){
            max_length = length;
            substring += s[i];
        }
        step ++;
        }
    return max_length;
}
