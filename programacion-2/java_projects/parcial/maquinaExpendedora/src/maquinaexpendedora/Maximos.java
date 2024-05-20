package maquinaexpendedora;

public interface Maximos {
      int maxCafe = 1500;
      int maxTe = 1000;
      int maxLeche = 600;
      int maxCacao = 600;
      int maxCrema = 600;
      int cantIngredientes [][]= {
    		  {40,30,0,0,0,30},
    		  {0,0,0,40,0,10},
    		  {0,0,35,0,20,0},
    		  {0,20,0,50,20,0},
    		  {0,0,0,0,0,30}
      };
      String nomIngredientes []= {"cafe", "te","leche","cacao","crema"};
}
