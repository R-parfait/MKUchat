# MKUchat
Social Media to connect MKU Students

<!DOCTYPE html>
<html>
<head>
    <title>profile page</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">


<style>
* {
  box-sizing: border-box;
}

/*banner*/
.banner {
    background-image:
    url();
    background-size: cover;
    height: 30vh;
  }

  .banner h1{
    color: blue;
    text-align: center;
    font-family:cursive;
    font-size: 50px;
    padding-top: 0px;
  }
  .logo img {
    float: right;
    width: 300px;
    height: 150px;
    background: #555;
  
  }
/*Navigation Bar*/
.topnav {
    overflow: hidden;
    background-color:blueviolet;
  }
  
  .topnav a {
    float:left;
    display: block;
    color: #f2f2f2;
    text-align: center;
    padding: 10px 20px;
    text-decoration: none;
    font-size: 18px;
    font-family: Arial;
  }
  
  .active {
    background-color: purple;
    color: white;
  }
  
  .topnav .icon {
    display: none;
  }
  
  .dropdown {
    float: left;
    overflow: hidden;
  }
  
  .dropdown .dropbtn {
    font-size: 18px; 
    border: none;
    outline: none;
    color: white;
    font-family: Arial;   
    padding: 12px 16px;
    background-color: inherit;
    margin: 0;
  }
  
  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 130px;
    box-shadow: 0px 8px 16px 0px rgba(173, 158, 158, 0.2);
    z-index: 1;
  }
  
  .dropdown-content a {
    float: none;
    color: blueviolet;
    padding: 10px 16px;
    text-decoration: none;
    font-family: Arial;   
    display: block;
    text-align: left;
  }
  
  .topnav a:hover, .dropdown:hover .dropbtn {
    background-color: #555;
    color: white;
  }
  
  .dropdown-content a:hover {
    background-color: #ddd;
    color: black;
  }
  
  .dropdown:hover .dropdown-content {
    display: block;
  }
  

  @media screen and (max-width: 600px) {
    .topnav a, .topnav input[type=text] {
      float: none;
      display: block;
      text-align: left;
      width: 100%;
      margin: 0;
      padding: 14px;
    }
    .topnav input[type=text] {
      border: 1px solid #ccc;
    }
  }
  
  
  /*responsiveness in navbar*/
  @media screen and (max-width: 600px) {
    .topnav a:not(:first-child), .dropdown .dropbtn {
      display: none;
    }
    .topnav a.icon {
      float: right;
      display: block;
    }
  }
  
  @media screen and (max-width: 600px) {
    .topnav.responsive {position: relative;}
    .topnav.responsive .icon {
      position: absolute;
      right: 0;
      top: 0;
    }
    .topnav.responsive a {
      float: none;
      display: block;
      text-align: left;
    }
    .topnav.responsive .dropdown {float: none;}
    .topnav.responsive .dropdown-content {position: relative;}
    .topnav.responsive .dropdown .dropbtn {
      display: block;
      width: 100%;
      text-align: left;
    }
  }

  
/* Create three unequal columns that floats next to each other */
.column {
  float: left;
  padding: 10px;
  height: ; /* Should be removed. Only for demonstration */
}

.left, .right {
  width: 25%;
}

.middle {
  width: 50%;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}
.portrait img {
    width: 100%;
    height: auto;
  }
/*CATEGORIES*/
.categories h2{
    color:blueviolet;
    text-align: center;
    font-family: Arial;
  }
  .categories p{
    margin-left: 40px;
    margin-top: 20px;
    border: 2px solid;
    border-radius: 5px;
    border-style: outset;
    width: 85%;
    text-align: center;
    font-family: Arial;
    background-color: blueviolet;
    padding: 5px;   
    }
    .categories a{
    text-decoration:none;
    color:white;
    }
    .trend h3{
      color:blueviolet;
      text-align: center;
      font-family: Arial;

    }
    .trend p{
      margin-left: 40px;
      margin-top: 20px;
      border: 2px solid;
      border-radius: 5px;
      border-style: outset;
      width: 85%;
      text-align: center;
      font-family: Arial;
      background-color: blueviolet;
      padding: 5px;   
      }
      .trend a{
      text-decoration:none;
      color:white;
      }
  
  .remark p{
    text-align: center;
    font-family: Georgia;
    color: black;
    font-size: 30px;
  }

  @media only screen and (max-width: 700px) {
    .categories, .remark,.trend {
      width: 49.99999%;
      margin: 6px 0;
    }
  }
  
  @media only screen and (max-width: 500px) {
    .categories, .remark,.trend {
        width: 100%;
    }
  }
.introduction h1{
    font-family: Helvetica;
    color: blue;
    
}
.introduction h3{
    font-family: Helvetica;
    color: blueviolet;
}
.introduction p{
    font-family: Helvetica;
    color: black;
    text-align: justify;
    
}
/*button edit profile*/
.button {
    background-color: #962cd4; 
    border: none;
    color: white;
    padding: 5px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
  }


  /*COLUMN 3*/
  /*social media*/

  .fa {
    padding: 16px;
    font-size: 20px;
    width: 50px;
    text-align: center;
    text-decoration: none;
    margin: 5px 2px;
    border-radius: 50%;
  }
  
  .fa:hover {
      opacity: 0.7;
  }
  
  .fa-twitter {
    background: #55ACEE;
    color: white;
  }
  
  .fa-youtube {
    background: #bb0000;
    color: white;
  }
  
  .fa-instagram {
    background: #125688;
    color: white;
  }

  .fa-skype {
    background: #00aff0;
    color: white;
  }
  .fa-google {
    background: #dd4b39;
    color: white;
  }

  /*Gallery
  div.gallery {
    border: 1px solid #ccc;
  }
  
  div.gallery:hover {
    border: 1px solid #777;
  }
  
  div.gallery img {
    width: 100%;
    height: auto;
  }
  
  div.responsive h3 {
    text-align: center;
    font-family: Helvetica;
    color: #962cd4;
  }
  .responsive {
    padding: 0 6px;
    float: left;
    width: 100%;
  }
  
  @media only screen and (max-width: 700px) {
    .responsive {
      width: 49.99999%;
      margin: 6px 0;
    }
  }
  
  @media only screen and (max-width: 500px) {
    .responsive {
      width: 100%;
    }
  }
  
  .clearfix:after {
    content: "";
    display: table;
    clear: both;
  } */
  /*Carousel*/
.mySlides {
  display: none
}
img {
  vertical-align: middle;
}

/* Slideshow container */
.slideshow-container {
max-width: 800px;
position: relative;
margin: auto;
}

/* Next & previous buttons */
.prev, .next {
cursor: pointer;
position: absolute;
top: 50%;
width: auto;
padding: 16px;
margin-top: -22px;
color: white;
font-weight: bold;
font-size: 18px;
transition: 0.6s ease;
border-radius: 0 3px 3px 0;
user-select:auto;
}

/* Position the "next button" to the right */
.next {
right: 0;
border-radius: 3px 0 0 3px;
}

/* On hover, add a black transparent background color */
.prev:hover, .next:hover {
background-color: blueviolet;
}



/* Number text (1/3 etc) */
.numbertext {
color: yellow;
font-size: 12px;
padding: 8px 12px;
position: absolute;
top: 0;
}

/* The dots/bullets/indicators */
.dot {
cursor: pointer;
height: 15px;
width: 15px;
margin: 0 2px;
background-color: #bbb;
border-radius: 50%;
display: inline-block;
transition: background-color 0.6s ease;
}

.active, .dot:hover {
background-color: hotpink;
}

/* Fading animation */
.fade {
-webkit-animation-name: fade;
-webkit-animation-duration: 1.5s;
animation-name: fade;
animation-duration: 2.0s;
}

@-webkit-keyframes fade {
from {opacity: .4} 
to {opacity: 1}
}

@keyframes fade {
from {opacity: .4} 
to {opacity: 1}
}
.gallery p{
color: blueviolet;
text-align: center;
font-size: 20px;
font-weight: bold;
font-family:  Helvetica;
}
 .advertisements{
  font-family: Arial;
  color:blueviolet;
  text-align: center;

 } 
  /* Footer */
  .footer {
    padding: 20px;
    text-align: center;
    background: #ddd;
    padding-left: 5px;
    padding-right: 10px;
  }

  .footer{
    color:white;
    font-size: 14px;
    background-color: blue;
  }

  .footer a{
    color:gold;
  }
</style>
</head>
<body>
<!---banner-->
<div class="banner">
    <div class="logo">
        <img src="images/MKU CHAT LOGO.jpg"/>
    </div>
    <h1>Chat...Unite...Prosper</h1>  
</div>
<!---Navigation bar-->

<div class="topnav" id="myTopnav">
    <a href="#" class="active">Home</a>
    <a href="#">About</a>
    <a href="#">Photos</a>
    <a href="#">Videos</a>
    <a href="#">Business</a>
    <a href="#">Stories</a>
    <a href="#">Blog</a>
    <a href="#">Events</a>
    <a href="#">Market</a>
    <a href="#">Places</a>
    <a href="#">Academics</a>
    <a href="#">Memes</a>
    <div class="dropdown">
      <button class="dropbtn">More 
        <i class="fa fa-caret-down"></i>
      </button>
      <div class="dropdown-content">
        <a href="#">Hobbies</a>
        <a href="#">Games</a>
        <a href="#">Chat</a>
        <a href="#">Friends</a>
        <a href="#">Trends</a>
      </div>
    </div> 
   
    <marquee style="font-size:30px; font-family:Arial;color:gold;">VISION: TO BE THE LEADING SOCIAL MEDIA PLATFORM. MISSION: MKUCHAT ENSURES MKU FRATERNITY IS CONNECTED IN ORDER TO DISCOVER WHAT IS GOING ON IN THE WORLD, AND TO SHARE AND EXPRESS WHAT MATTERS TO THEM.</marquee>

  <!-----Java script-->
    <a href="javascript:void(0);" style="font-size:15px;" class="icon" onclick="myFunction()">&#9776;</a>
  </div>
  <script>
  function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }
  </script>
<!--Three Unequal Columns-->
<div class="row">
  <div class="column left" style="background-color:white;">
    <div class="portrait">
    <img src="images/portrait 3.png" width="460" height="345">
    </div>
<!--content-->
<div class="categories">
    <h2>Useful Links</h2>
    <p><a href="#" target="_blank">Send message </a><br></p>
    <p><a href="#" target="_blank">Send E-mail</a></p>
    <p><a href="#" target="_blank">Programming</a></p>
    <p><a href="#" target="_blank">Networking</a></p>
    <p><a href="#" target="_blank">System Design</a></p>

  
  </div>
<div class="remark"><p> Chat <br>Unite <br>Prosper</p></div>
<div class="trend">
  <h3>RECENT UPDATES</h3>
  <p><a href="#" target="_blank">Posts</a></p>
  <p><a href="#" target="_blank">Messages</a></p>
  <p><a href="#" target="_blank">Profile</a></p>
  <p><a href="#" target="_blank">News Feed</a></p>
</div>
<!---end content-->
    
  </div>
  <!---end of column-left--->
  <div class="column middle" style="background-color:white;">
    <!---introduction-->
    <div class="introduction">
        <h1>GERALD MUCHIRA</h1>
        <h3>Introduction</h3>
        <p> Internally motivated professional programer, well versed in designing of systems, programs, software, and websites, having demonstrated high level of self-drive, motivation and passion. <br><br>
            Programmer ay heart from the time I was 10 years old frequenting my uncle who was a programmer since I was eager to create “things” using a computer. Little did I know that those “things” were programs. <br><br>
            Looking for better ways of doing programming in e- commerce particularly in this digital era and establishing relationships with thought leaders and other like-minded individuals. <br><br>
        </p> 
    </div>
      <!----personal information-->
      <div class="introduction">
        <h3>Personal Information</h3>
        <table>
            <tr>
                <td>GENDER</td>
                <td>:</td>
                <td>Male</td>
            </tr>
            <tr>
                <td>RELIGION</td>
                <td>:</td>
                <td>Christian</td>
            </tr>
                <td>TRIBE</td>
                <td>:</td>
                <td>Kenyan</td>
            </tr>
              
          </table>
        </div>
        <!----Address information-->
        <div class="introduction">
            <h3>Address Information</h3>
            <table>
                <tr>
                    <td>COUNTRY</td>
                    <td>:</td>
                    <td>Kenya</td>
                </tr>
                <tr>
                    <td>COUNTY</td>
                    <td>:</td>
                    <td>Kiambu</td>
                </tr>
                    <td>SUB-COUNTY</td>
                    <td>:</td>
                    <td>Thika</td>
                </tr>
                <tr>
                    <td>CONSTITUENCY</td>
                    <td>:</td>
                    <td>Thika Town</td>
                </tr>
                <tr>
                    <td>LOCATION</td>
                    <td>:</td>
                    <td>Ngoingwa</td>
                </tr>
                    <td>SUB-LOCATION</td>
                    <td>:</td>
                    <td>Ngoingwa</td>
                </tr>
                <tr>
                    <td>TOWN</td>
                    <td>:</td>
                    <td>Thika</td>
                </tr>
                <tr>
                    <td>ROAD</td>
                    <td>:</td>
                    <td>Mang'u Road</td>
                </tr>
                    <td>VILLAGE/ESTATE</td>
                    <td>:</td>
                    <td>Tora</td>
                </tr>
              </table>
            </div>
 <!----schools attended-->
 <div class="introduction">
    <h3>Schools Attended </h3>
    <table>
        <tr>
            <td>PRIMARY SCHOOL</td>
            <td>:</td>
            <td>Bidii Primary School</td>
        </tr>
        <tr>
            <td>HIGH SCHOOL 2</td>
            <td>:</td>
            <td>Alliance Boys High School</td>
        </tr>
            <td>COLLEGE/UNIVERSITY</td>
            <td>:</td>
            <td>Mount Kenya University</td>
        </tr>
      </table>
    </div>
     <!----work experience -->
     <div class="introduction">
        <h3>Work Experience </h3>
        <table>
            <tr>
                <td>G&M GENERAL MERCHANTS <br>P.O. Box 698, Naivasha</td>
                <td>:</td>
                <td>(2015 upto date)<br>Branch Manager</td>
            </tr>
            <tr>
                <td>QUEENSTAR COMPUTERS <br>P.O. Box 698, Naivasha</td>
                <td>:</td>
                <td>(2012-2015)<br>Computer Tutor & computer hardware maintenance</td>
            </tr>
          </table>
        </div>
     <!----Contact information-->
     <div class="introduction">
        <h3>Contact Information</h3>
        <table>
            <tr>
                <td>MOBILE 1</td>
                <td>:</td>
                <td>0705608609</td>
            </tr>
            <tr>
                <td>MOBILE 2</td>
                <td>:</td>
                <td>0705608609</td>
            </tr>
                <td>E-MAIL 1</td>
                <td>:</td>
                <td>xyz@gmail.com</td>
            </tr>
            <tr>
                <td>E-MAIL 2</td>
                <td>:</td>
                <td>abc@gmail.com Town</td>
            </tr>
          </table>
        </div>
<!----interests -->
<div class="introduction">
    <h3>Interests </h3>
    <table>
        <tr>
            <td>GAMES</td>
            <td>:</td>
            <td>Bandminton, tabletennis</td>
        </tr>
        <tr>
            <td>MUSIC</td>
            <td>:</td>
            <td>Classic soul and RNB</td>
        </tr>
            <td>BOOKS</td>
            <td>:</td>
            <td>Fiction</td>
        </tr>
        <tr>
            <td>MOVIES</td>
            <td>:</td>
            <td>Documentary, Investigative</td>
        </tr>
        <tr>
            <td>FOOD</td>
            <td>:</td>
            <td>Ugali Greens and meat</td>
        </tr>
        <tr>
            <td>CLOTHES</td>
            <td>:</td>
            <td>Casual </td>
        </tr>
        <tr>
            <td>VEHICLE</td>
            <td>:</td>
            <td>Toyota Hilux Double Cabin (4WD)</td>
        </tr>
      </table>
    </div>
<!--button/edit profile-->
<a href="#" class="button"> Edit Profile</a>

         
  </div>
  <!--end of column middle-->

  <div class="column right" style="background-color:white;">
    <div class="social">
<!-- Add font awesome icons -->
<a href="#" class="fa fa-twitter"></a>
<a href="#" class="fa fa-instagram"></a>
<a href="#" class="fa fa-youtube"></a>
<a href="#" class="fa fa-skype"></a>
<a href="#" class="fa fa-google"></a>

    </div>
<!--slideshow/carousel-->
<div class="gallery">
  <p>GALLERY</p>
</div>
<div class="slideshow-container">

    <div class="mySlides fade">
      <div class="numbertext">1 / 10</div>
      <img src="images/MKULOGO.jpg" style="width:100%">
    </div>
    
    <div class="mySlides fade">
      <div class="numbertext">2 / 10</div>
      <img src="images/Africa-Scholarship-Programme.jpg" style="width:100%">
    </div>
    
    <div class="mySlides fade">
      <div class="numbertext">3 / 10</div>
      <img src="images/mku cc.jpg" style="width:100%">
    </div>

    <div class="mySlides fade">
        <div class="numbertext">4 / 10</div>
        <img src="images/MKU2.jpg" style="width:100%">
      </div>

      <div class="mySlides fade">
        <div class="numbertext">5 / 10</div>
        <img src="images/mku3.jpg" style="width:100%">
      </div>
    
      <div class="mySlides fade">
        <div class="numbertext">6 / 10</div>
        <img src="images/MKUbridge.jpg" style="width:100%">
      </div>

      <div class="mySlides fade">
        <div class="numbertext">7 / 10</div>
        <img src="images/portrait 3.png" style="width:100%">
      </div>
    
      <div class="mySlides fade">
        <div class="numbertext">8 / 10</div>
        <img src="images/PORTRAIT.jpg 3.png" style="width:100%">
      </div>
    
      <div class="mySlides fade">
        <div class="numbertext">9 / 10</div>
        <img src="images/STUDENTS.jpg" style="width:100%">
      </div>
    
      <div class="mySlides fade">
        <div class="numbertext">10 / 10</div>
        <img src="images/MKU CHAT LOGO.jpg" style="width:100%">
      </div>



    <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
    <a class="next" onclick="plusSlides(1)">&#10095;</a>
    
    </div>
    <br>
    
    <div style="text-align:center">
      <span class="dot" onclick="currentSlide(1)"></span> 
      <span class="dot" onclick="currentSlide(2)"></span> 
      <span class="dot" onclick="currentSlide(3)"></span> 
    </div>
    
    <script>
    var slideIndex = 1;
    showSlides(slideIndex);
    
    function plusSlides(n) {
      showSlides(slideIndex += n);
    }
    
    function currentSlide(n) {
      showSlides(slideIndex = n);
    }
    
    function showSlides(n) {
      var i;
      var slides = document.getElementsByClassName("mySlides");
      var dots = document.getElementsByClassName("dot");
      if (n > slides.length) {slideIndex = 1}    
      if (n < 1) {slideIndex = slides.length}
      for (i = 0; i < slides.length; i++) {
          slides[i].style.display = "none";  
      }
      for (i = 0; i < dots.length; i++) {
          dots[i].className = dots[i].className.replace(" active", "");
      }
      slides[slideIndex-1].style.display = "block";  
      dots[slideIndex-1].className += " active";
    }
    </script>

    <div class="advertisements">
      <h3>ADVERTISEMENT</h3>
    </div>

  </div>


</div>

<!---footer-->
<div class="footer">
    <p>Copyright @2022 All Rights Reserved by:<a href="homepage.html">MKUCHAT</a></p>
</div>



</body>
</html>
