import java.util.Arrays;

public class Staircase {
    //There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase.
    //The order of the steps matters. What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
    //For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.

    public static void main(String[] args){
        Staircase staircase = new Staircase();
        Integer[][] stepsList = {{1,3,5},{1,2},{2,3},{1,3}};
        Integer[] nList = {5,4,6,5};
        for(int i = 0; i < nList.length; i++){
            System.out.println("N = " + nList[i]);
            System.out.println("X steps = " + Arrays.toString(stepsList[i]));
            System.out.println("Ways = " + staircase.staircase_ways(nList[i], stepsList[i]));
            System.out.println();
        }
        
    }
    
    public int staircase_ways(int n, Integer[] steps){
        if(n == 0){
            return 1;
        }
        if(n < 0){
            return 0; 
        }
        int total = 0;
        for(int i: steps){
            total += staircase_ways(n-i, steps);
        }
        return total;
    }
}
