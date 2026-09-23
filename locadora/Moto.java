package locadora;

// Moto.java
public class Moto extends Veiculo {

    public Moto(double taxa) {
        this.taxaDiaria = taxa;
    }

    @Override
    public double calcularValorTotal(int numDiarias) {
        return taxaDiaria * numDiarias;
    }
}