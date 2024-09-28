// Leetcode: 150. Evaluate Reverse Polish Notation
// Runtime 12ms, Beats 22.85%
// Memory 15.70 MB, Beats 83.89%

// Evaluates string of inputs in Reverse Polish Notation
// (https://en.wikipedia.org/wiki/Reverse_Polish_notation)

int evalRPN(vector<string>& tokens) {
    stack<int> stk;
    for (const string& c : tokens) {
        // If operation, performs operation on top 2 elements in stack
        if (c == "+") {
            int add = stk.top();
            stk.pop();
            add = add + stk.top();
            stk.pop();
            stk.push(add);
        }
        else if (c == "-") {
            int sub = stk.top();
            stk.pop();
            sub = stk.top() - sub;
            stk.pop();
            stk.push(sub);
        }
        else if (c == "*") {
            int mult = stk.top();
            stk.pop();
            mult = mult * stk.top();
            stk.pop();
            stk.push(mult);
        }
        else if (c == "/") {
            int div = stk.top();
            stk.pop();
            div = stk.top() / div;
            stk.pop();
            stk.push(div);
        }
        // Otherwise push number onto stack
        else {
            stk.push(stoi(c));
        }
        cout << stk.top();
    }
    // Returns remaining number on stack
    return stk.top();
}
