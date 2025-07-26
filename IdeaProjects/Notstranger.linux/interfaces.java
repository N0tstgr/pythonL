package Notstranger.linux;


interface bicycle{
   int a = 5;
    void applyBrake(int decrement);
    void speedUp(int increment);
}
interface lightbicycle{
    int a = 5;
    void lightdeeper();
    void lightheadlight();
}
 class AvonCycle implements bicycle{
    void blowHorn(){
        System.out.println("pee pee, pooon pooon");
    }
     public void applyBrake(int decrement){
        System.out.println("applying brake");
    }
    public void speedUp(int increment){
        System.out.println("Applying speedup");
    }
     public void lightdeeper(){
         System.out.println("click, click");
     }
   public void lightheadlight(){
        System.out.println("teeen, teeen");
    }
}
public class interfaces {
    public static void main(String[] args) {
AvonCycle vikashcycle = new AvonCycle();
vikashcycle.applyBrake(3);

//you can create properties in the interfaces
        System.out.println(vikashcycle.a);
//        //you can not modify the interfaces as they are final
////        vikashcycle.a = 90;
//        System.out.println(vikashcycle.a);

        vikashcycle.lightdeeper();
        vikashcycle.lightheadlight();

    }
}
