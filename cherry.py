import random
import string
import cherrypy
class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        #return """<html>
#<head> </head>
#<body>
#<form method="get" action="generate">
#<input type="text" value="8" name="length" />
#<button type="submit">Give it now!</button>
#</form> 
#</body>
#</html>
          return """
<!DOCTYPE html>
<html>
    <head>
        <title>
            First Web Page
        </title>
        <link rel="stylesheet" href="static/css/style.css">

<link href='https://fonts.googleapis.com/css?family=Roboto' rel='stylesheet'> 

    </head>
    <body>
        <!--Header menu of the page-->
        <header class="container">
             <!--Top header menu containing logo and Navigation bar-->

             <div id="top-header">
                 <!--Logo-->
                 <div id="logo">
                 	<p>Meet Anshika</p>
                         
                 </div>
                 <!--Navigation Menu-->
                 <nav id="menu">
                 	<ul>
                 		<li class = "active"><a href="#">Home</a></li> 
                        <li><a href="#">About Us</a></li> 
                        <li><a href="#">Our Products</a></li> 
                        <li><a href="#">Careers</a></li> 
                        <li><a href="#">Contact us</a></li>
                    </ul>
                 </nav>
             </div>
             <div id="header-image-menu">
             	<img src="static/images/slider.jpg">
             	<h2 id="image-text">Meet Er.Anshika Bhatnagar</h2>
                <h2 id="image2-text">Python Developer</h2>
             </div>
        </header>
        <main>
        	<section>
        		<div id='welcome'>
        			<h1 class = "title">Welcome to my website</h1>
        			<p>This is a <strong>Sample Webpage</strong>, a HTML  
                and CSS template designed by the <a href="https://www.geeksforgeeks.org" 
                target="_blank" rel="nofollow">GeeksforGeeks Team</a>.  
                The photos in this template are designed by our 
                <b>Graphic Desgin Team</b>. This template is desgined  
                to explain the basics of HTML and CSS in our first 
                Web Design course. 
        			</p>
        		</div>

        	</section>

        	
    <section class="container" id="section-2"> 
    <div class="row"> 
        <div id="column1"> 
            <div class="column-title"> 
                <h2>GFG Content</h2> 
            </div> 
                      
            <p> 
                A Computer Science portal for geeks. It  
                contains well written, well thought and  
                well explained computer science and  
                programming articles, quizzes and ... 
            </p>
            <a href="https://www.geeksforgeeks.org" 
                target="_blank" class="button"> 
                Learn More 
            </a> 
        </div> 
                  
        <div id="column2"> 
            <div class="column-title"> 
                <h2>GFG Practice</h2> 
            </div> 
                      
            <p> 
                A practice poratal to test your knowledge  
                of data structures and algorithms by solving  
                problems asked in interviews of many tech giants  
                like, Amazon, Microsoft etc. 
            </p> 
          
            <a href="https://practice.geeksforgeeks.org" 
                target="_blank" class="button"> 
                Learn More 
            </a> 
        </div> 
                      
        <div id="column3"> 
            <div class="column-title"> 
                <h2>GFG IDE</h2> 
            </div> 
                      
            <p> 
                An integrated development environment to  
                run and test your codes in almost all of  
                the popular and widely used programming  
                languages. 
            </p> 
              
            <a href="https://ide.geeksforgeeks.org" 
                target="_blank" class="button"> 
                Learn More 
            </a> 
        </div> 
    </div> 
</section> 

        	<section class="container" id="section-3">
        		<div class="row">
        			<div id="column21">
        				<img src="static/images/writer.jpg" class="image image-full"> 
                          
            <div class="img-title"> 
                <h3>Technical Content Writer</h3> 
            </div> 
                          
            <p> 
                The work requires understanding of Computer  
                Science concepts. Candidates who are active  
                on Practice Portal will be preferred. 
            </p> 
                          
            <a href="https://www.geeksforgeeks.org/careers/" 
                target="_blank" class="button"> 
                    Apply Here 
            </a> 
        			</div>
        			<div id="column22">
        				<img src="static/images/developer.jpg" class="image image-full"> 
                          
            <div class="img-title"> 
                <h3>Software Developer</h3> 
            </div> 
                          
            <p> 
                Good knowledge of PHP, JavaScript, Amazon AWS  
                and Web Development in general. Candidates who  
                are active on Practice Portal will be  
                preferred. 
            </p> 
                          
            <a href="https://www.geeksforgeeks.org/careers/" 
                target="_blank" class="button"> 
                    Apply Here 
            </a> 
        			</div>
        			<div id="column23">
        				<img src="static/images/support.jpg" class="image image-full"> 
                          
            <div class="img-title"> 
                <h3>Teaching Assistant</h3> 
            </div> 
                          
            <p> 
                It involves taking the doubt sessions,  
                coordinating with mentors and requires  
                in-depth knowledge of Data Structures  
                and Algorithms. 
            </p> 
                          
            <a href="https://www.geeksforgeeks.org/careers/" 
                target="_blank" class="button"> 
                    Apply Here 
            </a> 
        			</div>
        			<div id="column24">
        				<img src="static/images/teacher.jpg" class="image image-full"> 
                  
            <div class="img-title"> 
                <h3>Mentor / Tutor</h3> 
            </div> 
                          
            <p> 
                Job involves teaching, problem solving  
                in classes as well as doubt sessions and  
                thus requires in-depth knowledge of Data  
                Structures and Algorithms. 
            </p> 
                          
            <a href="https://www.geeksforgeeks.org/careers/" 
                target="_blank" class="button"> 
                    Apply Here 
            </a> 
        			</div>
        		<div>

        	</section>
        </main>

        <footer>

        </footer>
    </body>
</html>
"""
















    @cherrypy.expose
    def generate(self, length=8):
          return ''.join(random.sample(string.hexdigits, int(length)))
if __name__ == '__main__':
    import os
    conf={
        "/":{"tools.sessions.on":True,"tools.staticdir.root":os.path.abspath(os.getcwd())},
        "/static":{"tools.staticdir.on":True,"tools.staticdir.dir":'./public'}}
    cherrypy.quickstart(StringGenerator(),'/',conf)
