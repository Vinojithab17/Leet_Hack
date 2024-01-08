import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

class MyTask implements Runnable {
    public void run() {
        // Code to be executed in the new thread
        for (int i = 0; i < 5; i++) {
            System.out.println(Thread.currentThread().getId() + " Value " + i);
        }
    }
}

public class ExecutorExample {
    public static void main(String args[]) {
        ExecutorService executor = Executors.newFixedThreadPool(2);

        for (int i = 0; i < 5; i++) {
            Runnable myTask = new MyTask();
            executor.execute(myTask);  // Submit the task for execution
        }

        executor.shutdown();  // Shut down the executor when done
    }
}
