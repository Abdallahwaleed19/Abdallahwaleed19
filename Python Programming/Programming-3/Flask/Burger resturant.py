from flask import Flask, render_template_string

app = Flask(__name__)

# ======== RESTAURANT WEBSITE CODE ========
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BurgerJoint | {{ title }}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Fredoka+One&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #FF6B00;  /* Burger orange */
            --secondary: #FFD700; /* Golden fries */
            --dark: #3A2E1D;     /* Bun brown */
            --light: #FFF8E1;    /* Light cream */
            --accent: #C1121F;   /* Ketchup red */
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Poppins', sans-serif;
        }

        body {
            background-color: var(--light);
            color: var(--dark);
            overflow-x: hidden;
        }

        /* Header with sizzling animation */
        header {
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                        url('https://images.unsplash.com/photo-1586190848861-99aa4a171e90?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
            background-size: cover;
            background-position: center;
            height: 100vh;
            position: relative;
            overflow: hidden;
        }

        header::after {
            content: '';
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 100px;
            background: url('data:image/svg+xml;utf8,<svg viewBox="0 0 1200 120" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none"><path d="M0,0V46.29c47.79,22.2,103.59,32.17,158,28,70.36-5.37,136.33-33.31,206.8-37.5C438.64,32.43,512.34,53.67,583,72.05c69.27,18,138.3,24.88,209.4,13.08,36.15-6,69.85-17.84,104.45-29.34C989.49,25,1113-14.29,1200,52.47V0Z" fill="%23FFF8E1" opacity=".25"/><path d="M0,0V15.81C13,36.92,27.64,56.86,47.69,72.05,99.41,111.27,165,111,224.58,91.58c31.15-10.15,60.09-26.07,89.67-39.8,40.92-19,84.73-46,130.83-49.67,36.26-2.85,70.9,9.42,98.6,31.56,31.77,25.39,62.32,62,103.63,73,40.44,10.79,81.35-6.69,119.13-24.28s75.16-39,116.92-43.05c59.73-5.85,113.28,22.88,168.9,38.84,30.2,8.66,59,6.17,87.09-7.5,22.43-10.89,48-26.93,60.65-49.24V0Z" fill="%23FFF8E1" opacity=".5"/><path d="M0,0V5.63C149.93,59,314.09,71.32,475.83,42.57c43-7.64,84.23-20.12,127.61-26.46,59-8.63,112.48,12.24,165.56,35.4C827.93,77.22,886,95.24,951.2,90c86.53-7,172.46-45.71,248.8-84.81V0Z" fill="%23FFF8E1"/></svg>');
            background-size: cover;
            z-index: 1;
        }

        /* Navigation */
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 2rem 5%;
            position: fixed;
            width: 100%;
            z-index: 100;
            transition: all 0.3s ease;
        }

        nav.scrolled {
            background-color: var(--dark);
            padding: 1rem 5%;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .logo {
            font-family: 'Fredoka One', cursive;
            font-size: 2rem;
            color: var(--secondary);
            text-shadow: 2px 2px 0 var(--accent);
            animation: pulse 2s infinite;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
        }

        .nav-links a {
            color: white;
            text-decoration: none;
            font-weight: 600;
            position: relative;
            padding: 0.5rem 0;
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 0;
            height: 3px;
            background: var(--secondary);
            transition: width 0.3s ease;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        /* Hero section */
        .hero-content {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            color: white;
            width: 80%;
        }

        .hero-content h1 {
            font-size: 4rem;
            margin-bottom: 1rem;
            font-family: 'Fredoka One', cursive;
            text-shadow: 3px 3px 0 var(--accent);
            animation: slideIn 1s ease-out;
        }

        .hero-content p {
            font-size: 1.5rem;
            margin-bottom: 2rem;
            animation: slideIn 1s ease-out 0.3s forwards;
            opacity: 0;
        }

        .btn {
            display: inline-block;
            background: var(--accent);
            color: white;
            padding: 1rem 2rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s ease;
            animation: slideIn 1s ease-out 0.6s forwards;
            opacity: 0;
            border: 2px solid var(--accent);
        }

        .btn:hover {
            background: transparent;
            color: var(--secondary);
            border-color: var(--secondary);
            transform: translateY(-5px);
        }

        /* Menu section */
        .menu-section {
            padding: 5rem 5%;
            background-color: var(--light);
        }

        .section-title {
            text-align: center;
            margin-bottom: 3rem;
            position: relative;
        }

        .section-title h2 {
            font-family: 'Fredoka One', cursive;
            font-size: 3rem;
            color: var(--primary);
            display: inline-block;
        }

        .section-title h2::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 100px;
            height: 5px;
            background: var(--secondary);
            border-radius: 5px;
        }

        .menu-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .menu-item {
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            opacity: 0;
            transform: translateY(30px);
        }

        .menu-item.animate {
            opacity: 1;
            transform: translateY(0);
        }

        .menu-item:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        }

        .menu-item img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }

        .item-details {
            padding: 1.5rem;
        }

        .item-details h3 {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
            color: var(--primary);
        }

        .item-details .price {
            font-weight: 700;
            color: var(--accent);
            font-size: 1.2rem;
            margin-bottom: 1rem;
            display: block;
        }

        .item-details p {
            margin-bottom: 1rem;
            color: #666;
        }

        .add-to-cart {
            background: var(--primary);
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .add-to-cart:hover {
            background: var(--accent);
        }

        /* About section */
        .about-section {
            padding: 5rem 5%;
            background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
                        url('https://images.unsplash.com/photo-1555396273-367ea4eb4db5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
            background-size: cover;
            background-attachment: fixed;
            color: white;
            text-align: center;
        }

        /* Contact section */
        .contact-section {
            padding: 5rem 5%;
        }

        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .contact-info {
            background: var(--primary);
            padding: 2rem;
            border-radius: 10px;
            color: white;
        }

        .contact-info h3 {
            margin-bottom: 1.5rem;
            font-size: 1.5rem;
        }

        .contact-info p {
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .contact-form {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
        }

        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 0.8rem;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
        }

        .form-group textarea {
            min-height: 150px;
        }

        /* Footer */
        footer {
            background: var(--dark);
            color: white;
            text-align: center;
            padding: 2rem;
        }

        .social-links {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 1rem;
        }

        .social-links a {
            color: white;
            font-size: 1.5rem;
            transition: all 0.3s ease;
        }

        .social-links a:hover {
            color: var(--secondary);
            transform: translateY(-5px);
        }

        /* Animations */
        @keyframes slideIn {
            from {
                transform: translateY(50px);
                opacity: 0;
            }
            to {
                transform: translateY(0);
                opacity: 1;
            }
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        /* Responsive design */
        @media (max-width: 768px) {
            .hero-content h1 {
                font-size: 2.5rem;
            }
            
            .nav-links {
                display: none;
            }
            
            .menu-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <!-- Header with Navigation -->
    <header>
        <nav id="navbar">
            <div class="logo">BurgerJoint</div>
            <div class="nav-links">
                <a href="#home">Home</a>
                <a href="#menu">Menu</a>
                <a href="#about">About</a>
                <a href="#contact">Contact</a>
            </div>
        </nav>
        
        <div class="hero-content" id="home">
            <h1>Best Burgers in Town</h1>
            <p>Handcrafted with love since 2010</p>
            <a href="#menu" class="btn">View Menu</a>
        </div>
    </header>

    <!-- Menu Section -->
    <section class="menu-section" id="menu">
        <div class="section-title">
            <h2>Our Menu</h2>
        </div>
        
        <div class="menu-grid">
            <div class="menu-item">
                <img src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" alt="Classic Burger">
                <div class="item-details">
                    <h3>Classic Burger</h3>
                    <span class="price">$9.99</span>
                    <p>Our signature beef patty with lettuce, tomato, onion, and special sauce</p>
                    <button class="add-to-cart">Add to Order</button>
                </div>
            </div>
            
            <div class="menu-item">
                <img src="https://images.unsplash.com/photo-1551615593-ef5fe247e8f7?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" alt="Cheeseburger">
                <div class="item-details">
                    <h3>Double Cheeseburger</h3>
                    <span class="price">$12.99</span>
                    <p>Two juicy patties with double cheese, pickles, and mustard</p>
                    <button class="add-to-cart">Add to Order</button>
                </div>
            </div>
            
            <div class="menu-item">
                <img src="https://images.unsplash.com/photo-1596662951482-0c4ba74a6df6?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" alt="Bacon Burger">
                <div class="item-details">
                    <h3>Bacon King</h3>
                    <span class="price">$14.99</span>
                    <p>Beef patty with crispy bacon, cheddar, and BBQ sauce</p>
                    <button class="add-to-cart">Add to Order</button>
                </div>
            </div>
            
            <div class="menu-item">
                <img src="https://images.unsplash.com/photo-1603064752734-4c48eff53d05?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" alt="Chicken Burger">
                <div class="item-details">
                    <h3>Spicy Chicken</h3>
                    <span class="price">$11.99</span>
                    <p>Crispy chicken with spicy mayo, lettuce, and jalapeños</p>
                    <button class="add-to-cart">Add to Order</button>
                </div>
            </div>
            
            <div class="menu-item">
                <img src="https://images.unsplash.com/photo-1606755962773-d324e0a13086?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" alt="Veggie Burger">
                <div class="item-details">
                    <h3>Veggie Delight</h3>
                    <span class="price">$10.99</span>
                    <p>Plant-based patty with avocado, sprouts, and vegan mayo</p>
                    <button class="add-to-cart">Add to Order</button>
                </div>
            </div>
            
            <div class="menu-item">
                <img src="https://images.unsplash.com/photo-1529563021893-cc83c992d00d?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" alt="Fries">
                <div class="item-details">
                    <h3>Golden Fries</h3>
                    <span class="price">$4.99</span>
                    <p>Crispy fries with our special seasoning</p>
                    <button class="add-to-cart">Add to Order</button>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section class="about-section" id="about">
        <h2>Our Story</h2>
        <p>Founded in 2010, BurgerJoint has been serving the community with the juiciest burgers made from locally-sourced ingredients.</p>
        <p>We believe in quality, flavor, and the perfect burger experience.</p>
        <a href="#contact" class="btn">Visit Us</a>
    </section>

    <!-- Contact Section -->
    <section class="contact-section" id="contact">
        <div class="section-title">
            <h2>Contact Us</h2>
        </div>
        
        <div class="contact-grid">
            <div class="contact-info">
                <h3>Find Us</h3>
                <p><i class="fas fa-map-marker-alt"></i> 123 Burger Street, Foodville</p>
                <p><i class="fas fa-phone"></i> (555) 123-4567</p>
                <p><i class="fas fa-envelope"></i> info@burgerjoint.com</p>
                <p><i class="fas fa-clock"></i> Mon-Sun: 11AM - 10PM</p>
            </div>
            
            <form class="contact-form">
                <div class="form-group">
                    <label for="name">Name</label>
                    <input type="text" id="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" required>
                </div>
                <div class="form-group">
                    <label for="message">Message</label>
                    <textarea id="message" required></textarea>
                </div>
                <button type="submit" class="btn">Send Message</button>
            </form>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="social-links">
            <a href="#"><i class="fab fa-facebook"></i></a>
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="#"><i class="fab fa-twitter"></i></a>
            <a href="#"><i class="fab fa-yelp"></i></a>
        </div>
        <p>&copy; 2023 BurgerJoint. All rights reserved.</p>
    </footer>

    <script>
        // Navbar scroll effect
        window.addEventListener('scroll', function() {
            const navbar = document.getElementById('navbar');
            if (window.scrollY > 100) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        // Menu item animation on scroll
        const menuItems = document.querySelectorAll('.menu-item');
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.classList.add('animate');
                    }, index * 200);
                }
            });
        }, { threshold: 0.1 });

        menuItems.forEach(item => {
            observer.observe(item);
        });

        // Smooth scrolling for navigation
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });
    </script>
</body>
</html>
"""

# ======== FLASK ROUTES ========
@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True)