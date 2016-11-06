import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.util.Scanner;

/**
 * Created by mgm on 11/6/16.
 */

public class Main {

    static int n;

    //READ
    static Scanner fin = new Scanner(System.in);
    //WRITE
    static PrintStream out = null;

    public static void fileInput(String nameOfFile) {
        try {
            fin = new Scanner(new File(nameOfFile));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static void reading() {

    }

    public static void fileOutput(String nameOfFile) {
        try {
            out = new PrintStream(new FileOutputStream(nameOfFile));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        System.setOut(out);
    }

    public static void writing() {

    }

    //SOLVE
    public static void main(String[] args) {
        fileInput("input.txt");
        fileOutput("output.txt");

    }
}