//LeetCode: 2843. Count Symmetric Integers

//Count number of integers where first half of digits added together
//equal the second half of digits, odd numbers not symmetric

int countSymmetricIntegers(int low, int high) {
    int count = 0;
    for (int num = low; num <= high; num++) {
        string temp = to_string(num);
        int first = 0, second = 0, len = temp.length();
        if (len % 2 != 0) continue;
        for (auto& x : temp.substr(0,len/2)) {          //add up first half of digits
            first += int(x);
        }
        for (auto& x : temp.substr(len/2, len/2)) {     //add up second half of digits
            second += int(x);
        }
        if (first == second) {
                count++;
        }
    }
    return count;
}
