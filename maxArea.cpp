//LeetCode: 11. Container With Most Water
//Runtime: 53ms, Beats 83.88%
//Memory: 61.75MB, Beats 22.48%

//Given array of integers representing heights of bars on a graph, return 
//the maximum area possible of the box created with the bars and the graph

int maxArea(vector<int>& height) {
    int max = 0;
    //Create pointers to the leftmost and rightmost bars
    int* left = &height[0];
    int* right = &height[height.size()-1];
    
    while(left != right) {                        //Loop until pointers meet
        if(*left > *right) {                      //If left bar is taller
            if(*right * (right-left) > max){      //If box is greater than max
                max = *right * (right-left);
            }
            right--;                              //Move pointer of smaller bar
        }
        else {
            if(*left * (right-left) > max){
                max = *left * (right-left);
            }
            left++;
        }
    }

    return max;
}
