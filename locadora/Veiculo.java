package locadora;

// Veiculo.java
public abstract class Veiculo {

    protected double taxaDiaria;

    public abstract double calcularValorTotal(int numDiarias);
}
