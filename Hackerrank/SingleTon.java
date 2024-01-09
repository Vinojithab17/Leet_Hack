// Double Checked Locking based Java implementation of
// singleton design pattern
class Singleton {
    private static volatile Singleton obj = null;
    private Singleton() {}
 
    public static Singleton getInstance()
    {
        if (obj == null) {
            // To make thread safe
            synchronized (Singleton.class)
            {
                // check again as multiple threads
                // can reach above step
                if (obj == null)
                    obj = new Singleton();
            }
        }
        return obj;
    }
}


class Singletons{
    
    private static volatile Singletons singleton;

    private Singletons(){}

    public static Singletons getInstance(){
     if(singleton==null){
        synchronized(Singletons.class){
            if(singleton==null){
                singleton = new Singletons();
            }
        }
     }
        
        return singleton;
    }
}

// We have declared the obj volatile which ensures that 
// multiple threads offer the obj variable correctly
// when it is being initialized to the Singleton instance.
//  This method drastically reduces the overhead of calling the synchronized method every time.