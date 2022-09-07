// Вариант 343749
import java.lang.Math;



public class Lab1 {
    public static void main(String[] args) {

//Создать одномерный массив c типа short. Заполнить его числами от 6 до 17 включительно в порядке возрастания.
        short d[] = new short[12];
        for (int i = 0; i < 12; i++){
            d[i] = (short)(6 + i);
        }

//Создать одномерный массив x типа float. Заполнить его 13-ю случайными числами в диапазоне от -14.0 до 14.0.
        float x[] = new float[13];
        int max = 14;
        int min = -14;
        for (int i = 0; i<13; i++){
            x[i] = (float)((Math.random()) * ((max - min))+ min);
        }

//Создайте двумерный массив b размером 12x13. Вычислите его элементы (где x = x[j]).
        double b[][] = new double[12][13];
        double constant;
        for (int i=0; i<12; i++){
            for (int j=0; j<13; j++){
                if(d[i]==6){
                    constant = Math.pow(x[j],x[j])*((1/4) + Math.sin(x[j]));
                    b[i][j] = Math.asin(Math.sin(Math.pow(constant,3)));
                }
                else if(d[i]==9||d[i]==11||d[i]==12||d[i]==13||d[i]==14||d[i]==15){
                    constant = 3/(Math.log(Math.abs(x[j])));
                    b[i][j] = Math.pow(Math.pow(constant,Math.pow((x[j]/2),3)),(1/3));
                }
                else{
                    constant = Math.cos(Math.tan(Math.tan(x[j])));
                    b[i][j] = Math.pow((Math.cos(Math.cos(Math.cos(x[j])))/6),constant);
                }
            }
        }

//Напечатать полученный в результате массив в формате с двумя знаками после запятой.
        for (int i=0; i<12; i++){
            for (int j=0; j<13; j++){
                System.out.print("b["+i+"]["+j+"]=");
                System.out.format("%.2f",b[i][j]);
                System.out.print("; ");
            }
            System.out.print("\n");
        }
    }
}