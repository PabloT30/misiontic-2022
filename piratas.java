/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package piratas;
import java.util.Scanner;

/**
 *
 * @author Ensayos Automotrices
 */
public class Piratas {

    /**
     * @param args the command line arguments
     */
    public static String categoria_viaje(int dias) {
        if (dias <= 20) {
            return "uno";
        } else if (dias <= 30) {
            return "dos";
        } else if (dias <= 50) {
            return "tres";
        } else {
            return "cuatro";
        }
    }
    
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner sc = new Scanner (System.in);
        int dias_a_isla_tortuga = Integer.parseInt(sc.nextLine());
        int dias_a_isla_britanica = 2 * dias_a_isla_tortuga + 4;
        int dias_a_isla_muerte = (dias_a_isla_britanica + dias_a_isla_tortuga) / 5;
        String viaje = String.valueOf(dias_a_isla_tortuga) + " " +
                String.valueOf(dias_a_isla_britanica) + " " +
                String.valueOf(dias_a_isla_muerte);
        System.out.println(viaje);
        System.out.println(categoria_viaje(dias_a_isla_muerte));
    }
    
}
