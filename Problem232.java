import java.util.Stack;

public class Problem232 {
    public static void main(String[] args) {
        // Create a MyQueue object
        MyQueue myqueue = new MyQueue();

        // Define the input operations as specified
        String[] operations = {
            "MyQueue", "push", "push", "peek", "pop", "empty"
        };
        Integer[][] values = {
            {}, {1}, {2}, {}, {}, {}
        };

        // Array to store the results
        Object[] results = new Object[operations.length];

        // Execute the operations
        for (int i = 0; i < operations.length; i++) {
            String operation = operations[i];
            Integer[] params = values[i];

            switch (operation) {
                case "MyQueue":
                    // Instantiate MyQueue (already done)
                    results[i] = null;
                    break;
                case "push":
                    int x = params[0];
                    myqueue.push(x);
                    results[i] = null;
                    break;
                case "peek":
                    int peekResult = myqueue.peek();
                    results[i] = peekResult;
                    break;
                case "pop":
                    int popResult = myqueue.pop();
                    results[i] = popResult;
                    break;
                case "empty":
                    boolean isEmpty = myqueue.empty();
                    results[i] = isEmpty;
                    break;
                default:
                    results[i] = null;
                    break;
            }
        }

        // Print the results as an array
        System.out.print("[");
        for (int i = 0; i < results.length; i++) {
            if (i > 0) {
                System.out.print(",");
            }
            System.out.print(results[i]);
        }
        System.out.println("]");
    }
}

class MyQueue {
    Stack<Integer> in;
    Stack<Integer> out;

    public MyQueue() {
        this.in = new Stack<>();
        this.out = new Stack<>();
    }
    
    public void push(int x) {
        in.push(x);
    }
    
    public int pop() {
        if (out.isEmpty()) {
            while (!in.isEmpty()) {
                out.push(in.pop());
            }
        }
        return out.pop();
    }
    
    public int peek() {
        if (out.isEmpty()) {
            while (!in.isEmpty()) {
                out.push(in.pop());
            }
        }
        return out.peek();
    }
    
    public boolean empty() {
        return in.isEmpty() && out.isEmpty();
    }
}
