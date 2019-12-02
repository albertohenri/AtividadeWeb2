<template>
<div>
    <h1>ESTÁDIOS</h1>

    <div class="meucarro">
      <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
          <div class="carousel-inner">
          
            <div class="carousel-item active">
                <img src="../assets/img/arena1.jpeg" class="d-block w-100" alt="arena">
            </div>
                  
            <div class="carousel-item">
                <img src="../assets/img/arena2.jpeg" class="d-block w-100" alt="arena">
            </div>
                  
            <div class="carousel-item">
                <img src="../assets/img/arena3.jpeg" class="d-block w-100" alt="arena">
            </div>
                 
            <div class="carousel-item">
                <img src="../assets/img/olimpico1.jpeg" class="d-block w-100" alt="olimpico">
            </div>
                 
            <div class="carousel-item">
                <img src="../assets/img/olimpico2.jpeg" class="d-block w-100" alt="olimpico">
            </div>
                 
            <div class="carousel-item">
                <img src="../assets/img/olimpico3.jpeg" class="d-block w-100" alt="olimpico">
            </div>
                 
            <div class="carousel-item">
                <img src="../assets/img/baixada.jpg" class="d-block w-100" alt="baixada">
            </div>
          </div>
                
          <a class="carousel-control-prev" href="#carouselExampleControls" 
                role="button" data-slide="prev">
              <span class="carousel-control-prev-icon" 
                aria-hidden="true"></span>
              <span class="sr-only">Previous</span>
          </a>
                
          <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="sr-only">Next</span>
          </a>
      </div>
  </div>
            
  <div class="estadios">
    <ul>
      <li>Arena da Baixada;</li>
        <p>Primeiro estádio do Imortal, situado no bairro <br>Moinhos de Vento.</p>
      <li>Estádio Olímpico Monumental</li>
        <p>Construído em 1954, reformado em 1980</p>
      <li>Arena do Grêmio</li>
        <p>Estádio atual, inaugurado em 2012.</p>
    </ul>
  </div>
</div>
</template>

<script>
export default {
    name:"Stadiums",

};
</script>