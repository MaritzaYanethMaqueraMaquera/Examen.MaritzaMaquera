int   main (void)
 {


    int contadorA; //contador de lineas
    int contadorB;  //contador de hashes #
    int contadorC;  //contador de espacios =num total de lineas - 2
    int n;
   
    {
       do 
    
          {
           printf("Ingrese la Altura de la Piramide: ");
           scanf("%d", &n);
           }
           while (n>23 || n<=0);
           }

               for(contadorA= 1; contadorA <= n-1; contadorA ++ ) 

              {
                  {
               
                    for ( contadorC = n-2 ; contadorC >= contadorA ; contadorC-- )
    
                   printf(" ");
                       
                  }
                           
            {   
                      for (contadorB = 0 ; contadorB <= contadorA ;   contadorB++)
           
            printf("#");  // imprime hash
           
          }   
      
       
                 printf ("\n");    //imprime espacio
           
      }    
           
                
                
    } // fin de main