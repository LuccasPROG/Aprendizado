package locadora;

// Main.java
public class Main {

    public static void main(String[] args) {

        Carro carro = new Carro(50);
        Moto moto = new Moto(25);

        System.out.println("Valor do carro: R$ "
                + carro.calcularValorTotal(10));

        System.out.println("Valor da moto: R$ "
                + moto.calcularValorTotal(10));
    }
}