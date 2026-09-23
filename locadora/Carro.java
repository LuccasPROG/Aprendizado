package locadora;

// Carro.java
public class Carro extends Veiculo {

    public Carro(double taxa) {
        this.taxaDiaria = taxa;
    }

    @Override
    public double calcularValorTotal(int numDiarias) {
        return taxaDiaria * numDiarias;
    }
}