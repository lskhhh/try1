public class Day1Java{
    public static void main(String[] args){
        //1.变量
        String name = "张三";
        int age = 20;
        double height = 1.75;
        //2.输出
        System.out.println("姓名："+name);
        System.out.println("年龄："+age);
        System.out.println("身高："+height);
        //3.计算
        int brithYear = 2026 - age;
        System.out.println("出生年份："+brithYear);
        //4.运算符练习
        int a = 10;
        int b = 3;
        System.out.println("a + b = " + (a + b));
        System.out.println("a - b = " + (a - b));
        System.out.println("a * b = " + (a * b));
        System.out.println("a / b = " + (a / b));
        System.out.println("a % b = " + (a % b));
        System.out.println("a++ = " + a+","+b);


    }
}