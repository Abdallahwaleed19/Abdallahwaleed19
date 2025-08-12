// Theme System
let currentTheme = 'light';

// Function to set theme
function setTheme(theme) {
    currentTheme = theme;
    document.documentElement.setAttribute('data-theme', theme);

    console.log('Theme set to:', theme); // Debug log

    // Update theme button
    const themeIcon = document.getElementById('themeIcon');
    const themeText = document.getElementById('currentTheme');

    if (theme === 'dark') {
        themeIcon.className = 'fas fa-sun';
        themeText.textContent = 'Light';
    } else {
        themeIcon.className = 'fas fa-moon';
        themeText.textContent = 'Dark';
    }

    // Save theme preference
    localStorage.setItem('portfolioTheme', theme);

    // Show notification
    const message = theme === 'dark' ? 'تم تفعيل الوضع المظلم' : 'Light mode activated';
    showNotification(message, 'info');

    // Force a repaint to ensure CSS variables are applied
    document.body.offsetHeight;
}

// Function to toggle theme
function toggleTheme() {
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
}

// Initialize theme
function initializeTheme() {
    // Check for saved theme preference or default to 'light'
    const savedTheme = localStorage.getItem('portfolioTheme') || 'light';

    // Check if user prefers dark mode
    if (savedTheme === 'auto') {
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        setTheme(prefersDark ? 'dark' : 'light');
    } else {
        setTheme(savedTheme);
    }
}

// Demo Modal System
function initializeDemoModal() {
    const modal = document.getElementById('demoModal');
    const video = document.getElementById('projectVideo');
    const pdf = document.getElementById('projectPDF');
    const closeBtn = document.querySelector('.close-demo');
    const demoLinks = document.querySelectorAll('.project-demo');

    // Open demo modal
    demoLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const fileSrc = this.getAttribute('data-file');
            const fileType = this.getAttribute('data-file-type');
            const projectTitle = this.getAttribute('data-project-title');

            // Hide both video and PDF initially
            video.style.display = 'none';
            pdf.style.display = 'none';

            if (fileType === 'video') {
                video.src = fileSrc;
                video.style.display = 'block';
            } else if (fileType === 'pdf') {
                pdf.src = fileSrc;
                pdf.style.display = 'block';
            }

            document.getElementById('demoTitle').textContent = projectTitle;
            modal.style.display = 'block';
            document.body.style.overflow = 'hidden'; // Prevent background scrolling
        });
    });

    // Close modal when clicking X
    closeBtn.addEventListener('click', function () {
        modal.style.display = 'none';
        video.pause();
        video.src = '';
        pdf.src = '';
        document.body.style.overflow = 'auto';
    });

    // Close modal when clicking outside
    modal.addEventListener('click', function (e) {
        if (e.target === modal) {
            modal.style.display = 'none';
            video.pause();
            video.src = '';
            pdf.src = '';
            document.body.style.overflow = 'auto';
        }
    });

    // Close modal with Escape key
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && modal.style.display === 'block') {
            modal.style.display = 'none';
            video.pause();
            video.src = '';
            pdf.src = '';
            document.body.style.overflow = 'auto';
        }
    });
}

// Theme switcher functionality will be set up in DOMContentLoaded

// Navigation scroll effect
function handleNavbarScroll() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
}

// Active navigation highlighting
function highlightActiveNav() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-menu a');

    let current = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (window.scrollY >= (sectionTop - 200)) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
}

// Language Translation System
let currentLanguage = 'en';
const translations = {
    en: {
        // Navigation
        'Home': 'Home',
        'About': 'About',
        'Education': 'Education',
        'Skills': 'Skills',
        'Experience': 'Experience',
        'Services': 'Services',
        'Projects': 'Projects',
        'Contact': 'Contact',

        // Hero Section
        'Welcome to My Portfolio': 'Welcome to My Portfolio',
        'I\'m Abdallah Waleed Kamal Mousa': 'I\'m Abdallah Waleed Kamal Mousa',
        'IoT Engineer & Big Data Analytics Specialist': 'IoT Engineer & Big Data Analytics Specialist',
        'I create cutting-edge IoT and Big Data solutions with robust security at their core, enabling smarter decisions, optimizing operations, and ensuring trusted, secure systems': 'I create cutting-edge IoT and Big Data solutions with robust security at their core, enabling smarter decisions, optimizing operations, and ensuring trusted, secure systems',
        'View My Work': 'View My Work',
        'Get In Touch': 'Get In Touch',

        // About Section
        'About Me': 'About Me',
        'Years Experience': 'Years Experience',
        'IoT Projects': 'IoT Projects',
        'Data Projects': 'Data Projects',
        'Web Projects': 'Web Projects',

        // Education Section
        'Education': 'Education',
        'Level 3, Faculty of Computers and Artificial Intelligence': 'Level 3, Faculty of Computers and Artificial Intelligence',
        'Menoufia National University': 'Menoufia National University',

        // Skills Section
        'Skills': 'Skills',
        'IoT & Hardware': 'IoT & Hardware',
        'Big Data & Analytics': 'Big Data & Analytics',
        'Web Developer': 'Web Developer',
        'Security': 'Security',

        // Experience Section
        'Work Experience': 'Work Experience',
        'Senior IoT Solutions Architect': 'Senior IoT Solutions Architect',
        'Tech Innovations Corp': 'Tech Innovations Corp',
        'Big Data Engineer': 'Big Data Engineer',
        'DataFlow Systems': 'DataFlow Systems',
        'IoT Developer': 'IoT Developer',
        'Smart Solutions Ltd': 'Smart Solutions Ltd',

        // Services Section
        'Services Offered': 'Services Offered',
        'IoT System Design': 'IoT System Design',
        'Big Data Architecture': 'Big Data Architecture',
        'Data Analytics & ML': 'Data Analytics & ML',
        'Cloud IoT Solutions': 'Cloud IoT Solutions',

        // Projects Section
        'Featured Projects': 'Featured Projects',
        'Smart City IoT Platform': 'Smart City IoT Platform',
        'Industrial IoT Monitoring': 'Industrial IoT Monitoring',
        'Big Data Analytics Dashboard': 'Big Data Analytics Dashboard',

        // Achievements Section
        'Achievements': 'Achievements',
        'IoT Innovation Award': 'IoT Innovation Award',
        'Data Science Excellence': 'Data Science Excellence',
        'Patent Filed': 'Patent Filed',

        // Testimonials Section
        'Client Testimonials': 'Client Testimonials',

        // Contact Section
        'Get In Touch': 'Get In Touch',
        'Phone': 'Phone',
        'Email': 'Email',
        'LinkedIn': 'LinkedIn',
        'GitHub': 'GitHub',
        'Full Name': 'Full Name',
        'Email Address': 'Email Address',
        'Subject': 'Subject',
        'Message': 'Message',
        'Send Message': 'Send Message',

        // Thank You Section
        'Thank You!': 'Thank You!',
        'Let\'s Connect': 'Let\'s Connect',
        'View Projects': 'View Projects',
        'Dedication': 'Dedication',
        'Support': 'Support',
        'Innovation': 'Innovation',

        // Testimonials Submission
        'Submit Your Feedback': 'Submit Your Feedback',
        'Your Name': 'Your Name',
        'Your Feedback': 'Your Feedback',
        'Submit Feedback': 'Submit Feedback',

        // Footer
        'Connecting Devices, Analyzing Data, and Security': 'Connecting Devices, Analyzing Data, and Security',
        '&copy; 2025 Portfolio. All rights reserved.': '&copy; 2025 Portfolio. All rights reserved.'
    },
    ar: {
        // Navigation
        'Home': 'الرئيسية',
        'About': 'حول',
        'Education': 'التعليم',
        'Skills': 'المهارات',
        'Experience': 'الخبرة',
        'Services': 'الخدمات',
        'Projects': 'المشاريع',
        'Contact': 'اتصل بنا',

        // Hero Section
        'Welcome to My Portfolio': 'مرحباً بكم في ملفي الشخصي',
        'I\'m Abdallah Waleed Kamal Mousa': 'أنا عبدالله وليد كمال موسى',
        'IoT Engineer & Big Data Analytics Specialist': 'مهندس إنترنت الأشياء ومتخصص في تحليل البيانات الضخمة',
        'I create cutting-edge IoT and Big Data solutions with robust security at their core, enabling smarter decisions, optimizing operations, and ensuring trusted, secure systems': 'أقوم بإنشاء حلول متطورة لإنترنت الأشياء وتحليل البيانات الضخمة مع أمان قوي في جوهرها، مما يتيح قرارات أكثر ذكاءً وتحسين العمليات وضمان أنظمة موثوقة وآمنة',
        'View My Work': 'شاهد أعمالي',
        'Get In Touch': 'تواصل معي',

        // About Section
        'About Me': 'حول',
        'Years Experience': 'سنوات الخبرة',
        'IoT Projects': 'مشاريع إنترنت الأشياء',
        'Data Projects': 'مشاريع البيانات',
        'Web Projects': 'مشاريع الويب',

        // Education Section
        'Education': 'التعليم',
        'Level 3, Faculty of Computers and Artificial Intelligence': 'المستوى الثالث، كلية الحاسبات والذكاء الاصطناعي',
        'Menoufia National University': 'جامعة المنوفية الوطنية',

        // Skills Section
        'Skills': 'المهارات',
        'IoT & Hardware': 'إنترنت الأشياء والأجهزة',
        'Big Data & Analytics': 'البيانات الضخمة والتحليل',
        'Web Developer': 'مطور الويب',
        'Security': 'الأمان',

        // Experience Section
        'Work Experience': 'الخبرة العملية',
        'Senior IoT Solutions Architect': 'مهندس معماري أول لحلول إنترنت الأشياء',
        'Tech Innovations Corp': 'شركة الابتكارات التقنية',
        'Big Data Engineer': 'مهندس البيانات الضخمة',
        'DataFlow Systems': 'أنظمة تدفق البيانات',
        'IoT Developer': 'مطور إنترنت الأشياء',
        'Smart Solutions Ltd': 'الحلول الذكية المحدودة',

        // Services Section
        'Services Offered': 'الخدمات المقدمة',
        'IoT System Design': 'تصميم نظام إنترنت الأشياء',
        'Big Data Architecture': 'هندسة البيانات الضخمة',
        'Data Analytics & ML': 'تحليل البيانات والتعلم الآلي',
        'Cloud IoT Solutions': 'حلول إنترنت الأشياء السحابية',

        // Projects Section
        'Featured Projects': 'المشاريع المميزة',
        'Smart City IoT Platform': 'منصة إنترنت الأشياء للمدينة الذكية',
        'Industrial IoT Monitoring': 'مراقبة إنترنت الأشياء الصناعية',
        'Big Data Analytics Dashboard': 'لوحة تحكم تحليل البيانات الضخمة',

        // Achievements Section
        'Achievements': 'الإنجازات',
        'IoT Innovation Award': 'جائزة الابتكار في إنترنت الأشياء',
        'Data Science Excellence': 'التميز في علم البيانات',
        'Patent Filed': 'براءة اختراع مقدمة',

        // Testimonials Section
        'Client Testimonials': 'آراء العملاء',

        // Contact Section
        'Get In Touch': 'تواصل معنا',
        'Phone': 'الهاتف',
        'Email': 'البريد الإلكتروني',
        'LinkedIn': 'لينكد إن',
        'GitHub': 'جيت هب',
        'Full Name': 'الاسم الكامل',
        'Email Address': 'عنوان البريد الإلكتروني',
        'Subject': 'الموضوع',
        'Message': 'الرسالة',
        'Send Message': 'إرسال الرسالة',

        // Thank You Section
        'Thank You!': 'شكراً لك!',
        'Let\'s Connect': 'دعنا نتواصل',
        'View Projects': 'شاهد المشاريع',
        'Dedication': 'الالتزام',
        'Support': 'الدعم',
        'Innovation': 'الابتكار',

        // Testimonials Submission
        'Submit Your Feedback': 'أرسل ملاحظاتك',
        'Your Name': 'اسمك',
        'Your Feedback': 'ملاحظاتك',
        'Submit Feedback': 'إرسال الملاحظات',

        // Footer
        'Connecting Devices, Analyzing Data, and Security': 'ربط الأجهزة وتحليل البيانات والأمان',
        '&copy; 2025 Portfolio. All rights reserved.': '&copy; 2025 ملف شخصي. جميع الحقوق محفوظة.'
    }
};

// Function to translate the page
function translatePage(language) {
    currentLanguage = language;

    // Update HTML dir attribute for RTL support
    document.documentElement.dir = language === 'ar' ? 'rtl' : 'ltr';

    // Update language button text
    const currentLangElement = document.getElementById('currentLang');
    if (currentLangElement) {
        currentLangElement.textContent = language.toUpperCase();
    }

    // Save language preference to localStorage
    localStorage.setItem('portfolioLanguage', language);

    // Translate all elements with data attributes
    const elementsToTranslate = document.querySelectorAll('[data-en][data-ar]');
    elementsToTranslate.forEach(element => {
        if (language === 'ar') {
            element.textContent = element.getAttribute('data-ar');
        } else {
            element.textContent = element.getAttribute('data-en');
        }
    });

    // Translate placeholders
    const inputsWithPlaceholders = document.querySelectorAll('[data-en-placeholder][data-ar-placeholder]');
    inputsWithPlaceholders.forEach(input => {
        const placeholder = language === 'ar' ? input.getAttribute('data-ar-placeholder') : input.getAttribute('data-en-placeholder');
        if (placeholder) {
            input.placeholder = placeholder;
        }
    });

    // Update dynamic testimonials display
    updateTestimonialsDisplay();
    updateTestimonialVariables();

    // Update modal language if it's open
    updateModalLanguage();
    updateAdminModalLanguage();

    // Show notification
    const message = language === 'ar' ? 'تم تغيير اللغة إلى العربية' : 'Language changed to English';
    showNotification(message, 'info');
}

// Language switcher functionality
const languageToggle = document.getElementById('languageToggle');
if (languageToggle) {
    languageToggle.addEventListener('click', () => {
        const newLanguage = currentLanguage === 'en' ? 'ar' : 'en';
        translatePage(newLanguage);
    });
}

// Load saved preferences on page load
document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM loaded, initializing theme system...'); // Debug log

    // Initialize theme
    initializeTheme();

    // Set up theme switcher functionality
    const themeToggle = document.getElementById('themeToggle');
    console.log('Theme toggle button found:', themeToggle); // Debug log

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            console.log('Theme button clicked!'); // Debug log
            toggleTheme();
        });
        console.log('Theme toggle event listener added'); // Debug log
    } else {
        console.error('Theme toggle button not found!'); // Debug log
    }

    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (localStorage.getItem('portfolioTheme') === 'auto') {
            setTheme(e.matches ? 'dark' : 'light');
        }
    });

    // Load saved language preference
    const savedLanguage = localStorage.getItem('portfolioLanguage');
    if (savedLanguage && savedLanguage !== 'en') {
        translatePage(savedLanguage);
    }

    console.log('Theme system initialization complete'); // Debug log

    // Set up delete button event listeners for existing testimonials
    setupDeleteButtonListeners();
    setupDeleteButtonListenersSimple();
    setupDeleteButtonListenersDelegated();

    // Initialize admin system
    initializeAdminSystem();

    // Initialize demo modal system
    initializeDemoModal();

    // Initialize testimonials system
    initializeTestimonials();

    // Initialize contact form
    setupContactForm();
});

// Mobile Navigation Toggle
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-menu a').forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
    });
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Enhanced navigation functionality
window.addEventListener('scroll', () => {
    handleNavbarScroll();
    highlightActiveNav();
});

// Initialize navigation features
document.addEventListener('DOMContentLoaded', () => {
    // Set initial active navigation
    highlightActiveNav();

    // Add smooth scrolling with offset for fixed navbar
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const navbarHeight = document.querySelector('.navbar').offsetHeight;
                const targetPosition = target.offsetTop - navbarHeight - 20;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
});

// Skills animation on scroll
const skillBars = document.querySelectorAll('.skill-progress');
const skillsSection = document.querySelector('.skills');

const animateSkills = () => {
    skillBars.forEach(bar => {
        const width = bar.style.width;
        bar.style.width = '0%';
        setTimeout(() => {
            bar.style.width = width;
        }, 100);
    });
};

// Intersection Observer for skills animation
const skillsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateSkills();
            skillsObserver.unobserve(entry.target);
        }
    });
});

if (skillsSection) {
    skillsObserver.observe(skillsSection);
}

// Initialize EmailJS
(function () {
    emailjs.init("og6W1oZLy7gT0DFzt");
})();

// Email configuration
const EMAIL_CONFIG = {
    serviceId: "service_e1n8403",
    templateId: "template_pl26356",
    feedbackTemplateId: "template_kgre7jp",
    toEmail: "waleedabdallah238@gmail.com"
};

// Send email function
async function sendEmail(templateParams, templateId) {
    try {
        const response = await emailjs.send(
            EMAIL_CONFIG.serviceId,
            templateId,
            templateParams
        );
        return { success: true, response };
    } catch (error) {
        console.error('Email sending failed:', error);
        return { success: false, error };
    }
}

// Setup contact form with email functionality
function setupContactForm() {
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', async function (e) {
            e.preventDefault();

            const formData = new FormData(this);
            const name = formData.get('name');
            const email = formData.get('email');
            const subject = formData.get('subject');
            const message = formData.get('message');

            // Simple validation
            if (!name || !email || !subject || !message) {
                showNotification('Please fill in all required fields', 'error');
                return;
            }

            // Show loading state
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
            submitBtn.disabled = true;

            try {
                // Prepare email parameters
                const emailParams = {
                    to_email: EMAIL_CONFIG.toEmail,
                    from_name: name,
                    from_email: email,
                    subject: `Portfolio Contact: ${subject}`,
                    message: message,
                    reply_to: email
                };

                // Send email
                const result = await sendEmail(emailParams, EMAIL_CONFIG.templateId);

                if (result.success) {
                    showNotification('Message sent successfully! I will get back to you soon.', 'success');
                    this.reset();
                } else {
                    throw new Error('Email sending failed');
                }
            } catch (error) {
                console.error('Contact form error:', error);
                showNotification('Failed to send message. Please try again.', 'error');
            } finally {
                // Reset button state
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            }
        });
    }
}

// Feedback form handling - Add testimonials dynamically
const feedbackForm = document.getElementById('feedbackForm');
if (feedbackForm) {
    feedbackForm.addEventListener('submit', function (e) {
        e.preventDefault();

        // Get form data
        const formData = new FormData(this);
        const name = formData.get('name');
        const title = formData.get('title');
        const message = formData.get('message');
        const language = formData.get('language');

        // Simple validation
        if (!name || !title || !message) {
            alert('Please fill in all required fields');
            return;
        }

        // Create new testimonial
        addNewTestimonial(name, title, message, language);

        // Reset form
        this.reset();
    });
}

// Simple translation function (replace with real API)
async function simpleTranslate(text, fromLanguage) {
    // This is a placeholder - replace with actual translation API
    // For now, we'll just return the original text with a note
    return new Promise((resolve) => {
        setTimeout(() => {
            if (fromLanguage === 'en') {
                resolve(`[Translated to Arabic: ${text}]`);
            } else {
                resolve(`[Translated to English: ${text}]`);
            }
        }, 1000);
    });
}

// Add new testimonial
async function addNewTestimonial(name, title, message, language) {
    const testimonial = {
        id: Date.now(),
        name: name,
        title: title,
        message: message,
        language: language,
        translatedText: null,
        date: new Date().toISOString()
    };

    testimonials.push(testimonial);
    saveTestimonialsToStorage();
    updateTestimonialsDisplay();

    // Send email notification for new feedback
    try {
        const emailParams = {
            to_email: EMAIL_CONFIG.toEmail,
            from_name: name,
            subject: "New Portfolio Feedback",
            message: `New feedback received from ${name} (${title}):
            
Feedback: "${message}"
Language: ${language === 'en' ? 'English' : 'Arabic'}
Date: ${new Date().toLocaleString()}`,
            reply_to: "noreply@portfolio.com"
        };

        await sendEmail(emailParams, EMAIL_CONFIG.feedbackTemplateId);
    } catch (error) {
        console.error('Failed to send feedback notification email:', error);
        // Don't show error to user as feedback was still saved
    }

    const successMessage = currentLanguage === 'en'
        ? 'Thank you! Your feedback has been added to testimonials.'
        : 'شكراً لك! تم إضافة تقييمك إلى التوصيات.';
    showNotification(successMessage, 'success');
}

// Delete testimonial function removed - using the one defined later in the file

// Update testimonial variables for translation
function updateTestimonialVariables() {
    const testimonialCards = document.querySelectorAll('.testimonial-card');

    testimonialCards.forEach(card => {
        const testimonialText = card.querySelector('.testimonial-text p');
        const authorInfo = card.querySelector('.author-info span');

        if (testimonialText && testimonialText.hasAttribute('data-en')) {
            testimonialText.textContent = currentLanguage === 'en'
                ? `"${testimonialText.getAttribute('data-en')}"`
                : `"${testimonialText.getAttribute('data-ar')}"`;
        }

        if (authorInfo && authorInfo.hasAttribute('data-en')) {
            authorInfo.textContent = currentLanguage === 'en'
                ? authorInfo.getAttribute('data-en')
                : authorInfo.getAttribute('data-ar');
        }
    });
}

// Function to save testimonial to localStorage
function saveTestimonialToStorage(name, message) {
    let testimonials = JSON.parse(localStorage.getItem('portfolioTestimonials') || '[]');

    // Limit to 10 testimonials to prevent clutter
    if (testimonials.length >= 10) {
        testimonials.shift(); // Remove oldest testimonial
    }

    testimonials.push({
        name: name,
        message: message,
        date: new Date().toISOString()
    });

    localStorage.setItem('portfolioTestimonials', JSON.stringify(testimonials));
}

// Function to load testimonials from localStorage
function loadTestimonialsFromStorage() {
    const testimonials = JSON.parse(localStorage.getItem('portfolioTestimonials') || '[]');
    const testimonialsSlider = document.querySelector('.testimonials-slider');

    // Keep the original testimonials (first 2)
    const originalTestimonials = testimonialsSlider.querySelectorAll('.testimonial-card');

    // Add stored testimonials after the original ones
    testimonials.forEach((testimonial, index) => {
        const newTestimonial = document.createElement('div');
        newTestimonial.className = 'testimonial-card';
        const date = new Date(testimonial.date);
        const formattedDate = date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric'
        });

        // Create translatable testimonial content
        newTestimonial.innerHTML = `
            <div class="testimonial-content">
                <div class="testimonial-text">
                    <p data-en="${testimonial.message}" data-ar="${testimonial.message}">"${testimonial.message}"</p>
                </div>
                <div class="testimonial-author">
                    <div class="author-info">
                        <h4 data-en="${testimonial.name}" data-ar="${testimonial.name}">${testimonial.name}</h4>
                        <span data-en="Feedback Contributor • ${formattedDate}" data-ar="مساهم في التقييم • ${formattedDate}">Feedback Contributor • ${formattedDate}</span>
                    </div>
                </div>
                <button class="delete-testimonial-btn" title="Delete testimonial" data-en-title="Delete testimonial" data-ar-title="حذف التوصية" onclick="deleteTestimonial(this)">
                    <i class="fas fa-trash"></i>
                </button>
            </div>
        `;

        testimonialsSlider.appendChild(newTestimonial);
    });

    // Update navigation if we have more testimonials
    if (testimonials.length > 0) {
        updateTestimonialNavigation();
        updateTestimonialVariables();
    }

    // Set up delete button listeners for newly loaded testimonials
    setTimeout(() => {
        setupDeleteButtonListeners();
        setupDeleteButtonListenersSimple(); // Also try the simple method
        setupDeleteButtonListenersDelegated(); // Also try event delegation
    }, 100);
}

// Function to show notifications
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existingNotifications = document.querySelectorAll('.notification');
    existingNotifications.forEach(notification => notification.remove());

    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-info-circle'}"></i>
            <span>${message}</span>
        </div>
    `;

    // Add styles
    let background;
    let icon;

    switch (type) {
        case 'success':
            background = 'linear-gradient(135deg, #00ff00, #00cc00)';
            icon = 'fa-check-circle';
            break;
        case 'error':
            background = 'linear-gradient(135deg, #ff4444, #cc0000)';
            icon = 'fa-exclamation-circle';
            break;
        default:
            background = 'linear-gradient(135deg, #00ffff, #0099cc)';
            icon = 'fa-info-circle';
    }

    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${background};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
        z-index: 10000;
        transform: translateX(400px);
        transition: transform 0.3s ease;
        max-width: 300px;
        font-weight: 500;
    `;

    // Update icon
    notification.querySelector('i').className = `fas ${icon}`;

    // Add to page
    document.body.appendChild(notification);

    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);

    // Auto-remove after 5 seconds
    setTimeout(() => {
        notification.style.transform = 'translateX(400px)';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.remove();
            }
        }, 300);
    }, 5000);
}

// Function to update testimonial navigation
function updateTestimonialNavigation() {
    const testimonialCards = document.querySelectorAll('.testimonial-card');
    const testimonialNav = document.querySelector('.testimonial-nav');

    // Clear existing navigation
    testimonialNav.innerHTML = '';

    // Create new navigation dots
    testimonialCards.forEach((_, index) => {
        const navBtn = document.createElement('button');
        navBtn.className = 'nav-btn';
        navBtn.setAttribute('data-slide', index);

        if (index === 0) {
            navBtn.classList.add('active');
        }

        navBtn.addEventListener('click', () => {
            showTestimonial(index);
        });

        testimonialNav.appendChild(navBtn);
    });
}

// Function to update JavaScript variables after adding testimonials
function updateTestimonialVariables() {
    // Re-query elements since new ones were added
    window.testimonialCards = document.querySelectorAll('.testimonial-card');
    window.navBtns = document.querySelectorAll('.nav-btn');

    // Reset current slide
    window.currentSlide = 0;

    // Show first slide
    showTestimonial(0);
}

// Animate elements on scroll
const animateOnScroll = () => {
    const elements = document.querySelectorAll('.education-card, .service-card, .project-card, .achievement-card');

    elements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const elementVisible = 150;

        if (elementTop < window.innerHeight - elementVisible) {
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }
    });
};

// Initialize animation states
document.addEventListener('DOMContentLoaded', () => {
    const elements = document.querySelectorAll('.education-card, .service-card, .project-card, .achievement-card');
    elements.forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(30px)';
        element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    });

    // Load testimonials from localStorage
    loadTestimonialsFromStorage();
});

// Add scroll event listener
window.addEventListener('scroll', animateOnScroll);

// Trigger initial animation check
animateOnScroll();

// Typing effect for hero section
const typeWriter = (element, text, speed = 100) => {
    let i = 0;
    element.innerHTML = '';

    const timer = setInterval(() => {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
        } else {
            clearInterval(timer);
        }
    }, speed);
};

// Initialize typing effect when page loads
document.addEventListener('DOMContentLoaded', () => {
    const heroTitle = document.querySelector('.hero-text h1');
    if (heroTitle) {
        const originalText = heroTitle.textContent;
        typeWriter(heroTitle, originalText, 150);
    }
});

// Parallax effect for hero section
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero');
    if (hero) {
        const rate = scrolled * -0.5;
        hero.style.transform = `translateY(${rate}px)`;
    }
});

// Add loading animation
window.addEventListener('load', () => {
    document.body.classList.add('loaded');

    // Set up delete button listeners after page is fully loaded
    setTimeout(() => {
        setupDeleteButtonListeners();
        setupDeleteButtonListenersSimple();
        setupDeleteButtonListenersDelegated();
    }, 500);
});

// Add CSS for loading state
const style = document.createElement('style');
style.textContent = `
    body:not(.loaded) {
        opacity: 0;
        transition: opacity 0.5s ease;
    }
    
    body.loaded {
        opacity: 1;
    }
    
    .fade-in {
        animation: fadeIn 1s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
`;
document.head.appendChild(style);

// Add fade-in class to sections when they come into view
const fadeInObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in');
        }
    });
}, {
    threshold: 0.1
});

// Observe all sections
document.querySelectorAll('section').forEach(section => {
    fadeInObserver.observe(section);
});

// Counter animation for stats
const animateCounters = () => {
    const counters = document.querySelectorAll('.stat h3');

    counters.forEach(counter => {
        const target = parseInt(counter.textContent);
        const increment = target / 100;
        let current = 0;

        const updateCounter = () => {
            if (current < target) {
                current += increment;
                counter.textContent = Math.ceil(current) + '+';
                setTimeout(updateCounter, 20);
            } else {
                counter.textContent = target + '+';
            }
        };

        updateCounter();
    });
};

// Trigger counter animation when about section is visible
const aboutObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateCounters();
            aboutObserver.unobserve(entry.target);
        }
    });
});

const aboutSection = document.querySelector('.about');
if (aboutSection) {
    aboutObserver.observe(aboutSection);
}

// Add hover effects for interactive elements
document.querySelectorAll('.btn, .service-card, .project-card, .education-card').forEach(element => {
    element.addEventListener('mouseenter', function () {
        this.style.transform = 'translateY(-5px) scale(1.02)';
    });

    element.addEventListener('mouseleave', function () {
        this.style.transform = 'translateY(0) scale(1)';
    });
});

// Smooth reveal animation for timeline items
const timelineObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateX(0)';
        }
    });
}, {
    threshold: 0.5
});

// Initialize timeline items
document.querySelectorAll('.timeline-item').forEach((item, index) => {
    item.style.opacity = '0';
    item.style.transform = index % 2 === 0 ? 'translateX(-50px)' : 'translateX(50px)';
    item.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    timelineObserver.observe(item);
});

// Add scroll progress indicator
const createScrollProgress = () => {
    const progressBar = document.createElement('div');
    progressBar.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 0%;
        height: 3px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        z-index: 9999;
        transition: width 0.1s ease;
    `;
    document.body.appendChild(progressBar);

    window.addEventListener('scroll', () => {
        const scrollTop = document.documentElement.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
        const progress = (scrollTop / scrollHeight) * 100;
        progressBar.style.width = progress + '%';
    });
};

// Initialize scroll progress bar
createScrollProgress();

// Add back to top button
const createBackToTop = () => {
    const backToTop = document.createElement('button');
    backToTop.innerHTML = '<i class="fas fa-arrow-up"></i>';
    backToTop.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 50px;
        height: 50px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 50%;
        cursor: pointer;
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s ease;
        z-index: 1000;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
    `;

    document.body.appendChild(backToTop);

    // Show/hide button based on scroll position
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            backToTop.style.opacity = '1';
            backToTop.style.visibility = 'visible';
        } else {
            backToTop.style.opacity = '0';
            backToTop.style.visibility = 'hidden';
        }
    });

    // Scroll to top when clicked
    backToTop.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Hover effects
    backToTop.addEventListener('mouseenter', () => {
        backToTop.style.transform = 'translateY(-3px) scale(1.1)';
    });

    backToTop.addEventListener('mouseleave', () => {
        backToTop.style.transform = 'translateY(0) scale(1)';
    });
};

// Initialize back to top button
createBackToTop();

// Add keyboard navigation support
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        // Close mobile menu
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
    }

    // Navigate sections with arrow keys
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        e.preventDefault();
        const sections = Array.from(document.querySelectorAll('section[id]'));
        const currentSection = sections.find(section => {
            const rect = section.getBoundingClientRect();
            return rect.top <= 100 && rect.bottom >= 100;
        });

        if (currentSection) {
            const currentIndex = sections.indexOf(currentSection);
            let nextIndex;

            if (e.key === 'ArrowDown') {
                nextIndex = Math.min(currentIndex + 1, sections.length - 1);
            } else {
                nextIndex = Math.max(currentIndex - 1, 0);
            }

            sections[nextIndex].scrollIntoView({ behavior: 'smooth' });
        }
    }
});

// Add touch support for mobile
let touchStartY = 0;
let touchEndY = 0;

document.addEventListener('touchstart', (e) => {
    touchStartY = e.changedTouches[0].screenY;
});

document.addEventListener('touchend', (e) => {
    touchEndY = e.changedTouches[0].screenY;
    handleSwipe();
});

const handleSwipe = () => {
    const swipeThreshold = 50;
    const diff = touchStartY - touchEndY;

    if (Math.abs(diff) > swipeThreshold) {
        const sections = Array.from(document.querySelectorAll('section[id]'));
        const currentSection = sections.find(section => {
            const rect = section.getBoundingClientRect();
            return rect.top <= 100 && rect.bottom >= 100;
        });

        if (currentSection) {
            const currentIndex = sections.indexOf(currentSection);
            let nextIndex;

            if (diff > 0) {
                // Swipe up - next section
                nextIndex = Math.min(currentIndex + 1, sections.length - 1);
            } else {
                // Swipe down - previous section
                nextIndex = Math.max(currentIndex - 1, 0);
            }

            sections[nextIndex].scrollIntoView({ behavior: 'smooth' });
        }
    }
};

// Admin state management
let isAdminMode = false;
const ADMIN_PASSCODE = '2112004'; // You can change this to any password you want

// Function to check if admin mode is enabled
function isAdminEnabled() {
    return isAdminMode;
}

// Function to delete testimonial
function deleteTestimonial(button) {
    console.log('deleteTestimonial function called with button:', button);
    console.log('Button element:', button);
    console.log('Button HTML:', button.outerHTML);

    // Check if admin mode is enabled
    if (!isAdminEnabled()) {
        console.log('Admin mode not enabled, showing admin modal');
        showAdminModal();
        return;
    }

    const testimonialCard = button.closest('.testimonial-card');
    const testimonialId = testimonialCard.getAttribute('data-testimonial-id');

    // Store reference to testimonial card for deletion
    window.pendingTestimonialDeletion = {
        card: testimonialCard,
        id: testimonialId
    };

    // Show modern confirmation modal
    showConfirmationModal();
}

// Function to show confirmation modal
function showConfirmationModal() {
    const modal = document.getElementById('confirmationModal');
    if (modal) {
        modal.classList.add('show');

        // Update modal text based on current language
        updateModalLanguage();

        // Add event listeners to modal buttons
        const cancelBtn = modal.querySelector('.modal-btn-cancel');
        const deleteBtn = modal.querySelector('.modal-btn-delete');

        // Remove existing listeners to prevent duplicates
        cancelBtn.replaceWith(cancelBtn.cloneNode(true));
        deleteBtn.replaceWith(deleteBtn.cloneNode(true));

        // Get fresh references after cloning
        const newCancelBtn = modal.querySelector('.modal-btn-cancel');
        const newDeleteBtn = modal.querySelector('.modal-btn-delete');

        newCancelBtn.addEventListener('click', hideConfirmationModal);
        newDeleteBtn.addEventListener('click', confirmTestimonialDeletion);

        // Add click outside to close functionality
        const overlay = modal.querySelector('.modal-overlay');
        if (overlay) {
            overlay.addEventListener('click', hideConfirmationModal);
        }

        // Add ESC key functionality
        document.addEventListener('keydown', handleModalKeydown);
    }
}

// Function to show admin modal
function showAdminModal() {
    console.log('showAdminModal called');
    const modal = document.getElementById('adminModal');
    if (modal) {
        console.log('Admin modal found, showing it');
        console.log('Modal element:', modal);
        console.log('Modal HTML:', modal.outerHTML);
        modal.classList.add('show');
        console.log('Modal show class added. Modal display style:', window.getComputedStyle(modal).display);
        console.log('Modal opacity:', window.getComputedStyle(modal).opacity);

        // Update modal text based on current language
        updateAdminModalLanguage();

        // Add event listeners to modal buttons
        const cancelBtn = modal.querySelector('.modal-btn-cancel');
        const unlockBtn = modal.querySelector('#adminUnlockBtn');
        const passInput = modal.querySelector('#adminPassInput');

        // Remove existing listeners to prevent duplicates
        cancelBtn.replaceWith(cancelBtn.cloneNode(true));
        unlockBtn.replaceWith(unlockBtn.cloneNode(true));

        // Get fresh references after cloning
        const newCancelBtn = modal.querySelector('.modal-btn-cancel');
        const newUnlockBtn = modal.querySelector('#adminUnlockBtn');
        const newPassInput = modal.querySelector('#adminPassInput');

        newCancelBtn.addEventListener('click', hideAdminModal);
        newUnlockBtn.addEventListener('click', () => validateAdminPasscode(newPassInput.value));

        // Add click outside to close functionality
        const overlay = modal.querySelector('.modal-overlay');
        if (overlay) {
            overlay.addEventListener('click', hideAdminModal);
        }

        // Add ESC key functionality
        document.addEventListener('keydown', handleAdminModalKeydown);

        // Focus on input and handle Enter key
        newPassInput.focus();
        newPassInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                validateAdminPasscode(newPassInput.value);
            }
        });
    }
}

// Function to hide admin modal
function hideAdminModal() {
    const modal = document.getElementById('adminModal');
    if (modal) {
        modal.classList.remove('show');

        // Clear input
        const passInput = modal.querySelector('#adminPassInput');
        if (passInput) passInput.value = '';

        // Remove event listeners
        document.removeEventListener('keydown', handleAdminModalKeydown);
    }
}

// Function to handle admin modal keyboard events
function handleAdminModalKeydown(event) {
    if (event.key === 'Escape') {
        hideAdminModal();
    }
}

// Function to update admin modal language
function updateAdminModalLanguage() {
    const modal = document.getElementById('adminModal');
    if (!modal) return;

    const title = modal.querySelector('.modal-title');
    const message = modal.querySelector('.modal-message');
    const cancelBtn = modal.querySelector('.modal-btn-cancel');
    const unlockBtn = modal.querySelector('#adminUnlockBtn');
    const passInput = modal.querySelector('#adminPassInput');

    if (currentLanguage === 'ar') {
        title.textContent = title.getAttribute('data-ar');
        message.textContent = message.getAttribute('data-ar');
        cancelBtn.textContent = cancelBtn.getAttribute('data-ar');
        unlockBtn.textContent = unlockBtn.getAttribute('data-ar');
        passInput.placeholder = passInput.getAttribute('data-ar-placeholder');
    } else {
        title.textContent = title.getAttribute('data-en');
        message.textContent = message.getAttribute('data-en');
        cancelBtn.textContent = cancelBtn.getAttribute('data-en');
        unlockBtn.textContent = unlockBtn.getAttribute('data-en');
        passInput.placeholder = passInput.getAttribute('data-en-placeholder');
    }
}

// Function to validate admin passcode
function validateAdminPasscode(passcode) {
    if (passcode === ADMIN_PASSCODE) {
        // Enable admin mode
        isAdminMode = true;

        // Update UI
        document.body.classList.add('admin-enabled');
        const adminBtn = document.getElementById('adminToggle');
        const adminIcon = document.getElementById('adminIcon');
        const adminState = document.getElementById('adminState');

        if (adminBtn) adminBtn.classList.add('active');
        if (adminIcon) adminIcon.className = 'fas fa-unlock';
        if (adminState) {
            adminState.textContent = currentLanguage === 'ar' ? 'مفعل' : 'Active';
        }

        // Hide admin modal
        hideAdminModal();

        // Show success message
        const successMessage = currentLanguage === 'ar' ?
            'تم تفعيل وضع المشرف بنجاح' :
            'Admin mode activated successfully';
        showNotification(successMessage, 'success');

        // Save admin state to localStorage
        localStorage.setItem('portfolioAdminMode', 'true');

    } else {
        // Show error message
        const errorMessage = currentLanguage === 'ar' ?
            'رمز المرور غير صحيح' :
            'Incorrect passcode';
        showNotification(errorMessage, 'error');

        // Clear input and focus
        const passInput = document.getElementById('adminPassInput');
        if (passInput) {
            passInput.value = '';
            passInput.focus();
        }
    }
}

// Function to initialize admin system
function initializeAdminSystem() {
    // Check if admin mode was previously enabled
    const savedAdminMode = localStorage.getItem('portfolioAdminMode');
    if (savedAdminMode === 'true') {
        isAdminMode = true;
        document.body.classList.add('admin-enabled');

        const adminBtn = document.getElementById('adminToggle');
        const adminIcon = document.getElementById('adminIcon');
        const adminState = document.getElementById('adminState');

        if (adminBtn) adminBtn.classList.add('active');
        if (adminIcon) adminIcon.className = 'fas fa-unlock';
        if (adminState) {
            adminState.textContent = currentLanguage === 'ar' ? 'مفعل' : 'Active';
        }
    }

    // Add admin button click handler
    const adminToggle = document.getElementById('adminToggle');
    if (adminToggle) {
        adminToggle.addEventListener('click', () => {
            if (isAdminMode) {
                // Disable admin mode
                isAdminMode = false;
                document.body.classList.remove('admin-enabled');

                adminToggle.classList.remove('active');
                const adminIcon = document.getElementById('adminIcon');
                const adminState = document.getElementById('adminState');

                if (adminIcon) adminIcon.className = 'fas fa-lock';
                if (adminState) {
                    adminState.textContent = currentLanguage === 'ar' ? 'مشرف' : 'Admin';
                }

                // Remove from localStorage
                localStorage.removeItem('portfolioAdminMode');

                // Show notification
                const message = currentLanguage === 'ar' ?
                    'تم إلغاء تفعيل وضع المشرف' :
                    'Admin mode deactivated';
                showNotification(message, 'info');
            } else {
                // Show admin modal to enter passcode
                showAdminModal();
            }
        });
    }
}

// Function to handle modal keyboard events
function handleModalKeydown(event) {
    if (event.key === 'Escape') {
        hideConfirmationModal();
    }
}

// Function to hide confirmation modal
function hideConfirmationModal() {
    const modal = document.getElementById('confirmationModal');
    if (modal) {
        modal.classList.remove('show');
        // Clear pending deletion
        window.pendingTestimonialDeletion = null;

        // Remove event listeners
        document.removeEventListener('keydown', handleModalKeydown);
    }
}

// Function to update modal language
function updateModalLanguage() {
    const modal = document.getElementById('confirmationModal');
    if (!modal) return;

    const title = modal.querySelector('.modal-title');
    const message = modal.querySelector('.modal-message');
    const cancelBtn = modal.querySelector('.modal-btn-cancel');
    const deleteBtn = modal.querySelector('.modal-btn-delete');

    if (currentLanguage === 'ar') {
        title.textContent = title.getAttribute('data-ar');
        message.textContent = message.getAttribute('data-ar');
        cancelBtn.textContent = cancelBtn.getAttribute('data-ar');
        deleteBtn.textContent = deleteBtn.getAttribute('data-ar');
    } else {
        title.textContent = title.getAttribute('data-en');
        message.textContent = message.getAttribute('data-en');
        cancelBtn.textContent = cancelBtn.getAttribute('data-en');
        deleteBtn.textContent = deleteBtn.getAttribute('data-en');
    }
}

// Function to confirm testimonial deletion
function confirmTestimonialDeletion() {
    const pendingDeletion = window.pendingTestimonialDeletion;
    if (!pendingDeletion) return;

    const { card: testimonialCard, id: testimonialId } = pendingDeletion;

    // Hide modal
    hideConfirmationModal();

    // Remove from DOM with animation
    testimonialCard.style.transition = 'all 0.3s ease';
    testimonialCard.style.opacity = '0';
    testimonialCard.style.transform = 'scale(0.8)';

    setTimeout(() => {
        testimonialCard.remove();

        // Update navigation and variables
        updateTestimonialNavigation();
        updateTestimonialVariables();

        // If it was a dynamic testimonial, remove from localStorage
        if (!testimonialId || !testimonialId.startsWith('static-')) {
            removeTestimonialFromStorage(testimonialCard);
        }

        // Show success message
        const successMessage = currentLanguage === 'ar' ?
            'تم حذف التوصية بنجاح' :
            'Testimonial deleted successfully';
        showNotification(successMessage, 'success');

        // If no testimonials left, show message
        const remainingTestimonials = document.querySelectorAll('.testimonial-card');
        if (remainingTestimonials.length === 0) {
            const testimonialsSlider = document.querySelector('.testimonials-slider');
            testimonialsSlider.innerHTML = `
                <div class="no-testimonials" style="text-align: center; padding: 3rem; color: var(--text-secondary);">
                    <i class="fas fa-comments" style="font-size: 3rem; margin-bottom: 1rem; opacity: 0.5;"></i>
                    <h3 data-en="No Testimonials Yet" data-ar="لا توجد توصيات بعد">No Testimonials Yet</h3>
                    <p data-en="Be the first to share your feedback!" data-ar="كن أول من يشارك ملاحظاته!">Be the first to share your feedback!</p>
                </div>
                <div class="testimonial-nav">
                    <button class="nav-btn active" data-slide="0"></button>
                </div>
            `;
        }

        // Clear pending deletion
        window.pendingTestimonialDeletion = null;
    }, 300);
}

// Function to remove testimonial from localStorage
function removeTestimonialFromStorage(testimonialCard) {
    const testimonials = JSON.parse(localStorage.getItem('portfolioTestimonials') || '[]');
    const testimonialText = testimonialCard.querySelector('.testimonial-text p').textContent.replace(/"/g, '');
    const testimonialName = testimonialCard.querySelector('.author-info h4').textContent;

    // Find and remove the matching testimonial
    const updatedTestimonials = testimonials.filter(testimonial =>
        testimonial.message !== testimonialText || testimonial.name !== testimonialName
    );

    localStorage.setItem('portfolioTestimonials', JSON.stringify(updatedTestimonials));
}

// Function to set up delete button event listeners for existing testimonials
function setupDeleteButtonListeners() {
    console.log('Setting up delete button listeners...');

    // Check if testimonials container exists
    const testimonialsContainer = document.getElementById('testimonialsContainer');
    if (testimonialsContainer) {
        console.log('Testimonials container found');
        console.log('Container HTML:', testimonialsContainer.innerHTML);
    } else {
        console.log('Testimonials container not found!');
        return;
    }

    const deleteButtons = document.querySelectorAll('.delete-testimonial-btn');
    console.log('Found delete buttons:', deleteButtons.length);

    if (deleteButtons.length === 0) {
        console.log('No delete buttons found. Checking testimonials...');
        const testimonialCards = document.querySelectorAll('.testimonial-card');
        console.log('Testimonial cards found:', testimonialCards.length);

        testimonialCards.forEach((card, index) => {
            console.log(`Card ${index}:`, card.innerHTML);
        });
    }

    deleteButtons.forEach((button, index) => {
        console.log(`Processing delete button ${index}:`, button);

        // Remove any existing listeners by cloning the button
        const newButton = button.cloneNode(true);
        button.parentNode.replaceChild(newButton, button);

        // Add the event listener to the new button
        newButton.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            console.log('Delete button clicked!');
            deleteTestimonial(this);
        });

        console.log(`Event listener added to delete button ${index}`);
    });

    // Add a global test to see if any delete buttons exist
    console.log('Final check - all delete buttons on page:', document.querySelectorAll('.delete-testimonial-btn').length);
}

// Alternative simpler function to set up delete button listeners
function setupDeleteButtonListenersSimple() {
    console.log('Setting up delete button listeners (simple method)...');

    // Remove all existing event listeners by removing and re-adding the buttons
    const testimonialCards = document.querySelectorAll('.testimonial-card');
    testimonialCards.forEach((card, cardIndex) => {
        const deleteBtn = card.querySelector('.delete-testimonial-btn');
        if (deleteBtn) {
            console.log(`Found delete button in card ${cardIndex}`);

            // Create a new button to replace the old one
            const newDeleteBtn = deleteBtn.cloneNode(true);
            deleteBtn.parentNode.replaceChild(newDeleteBtn, deleteBtn);

            // Add click event listener
            newDeleteBtn.addEventListener('click', function (e) {
                e.preventDefault();
                e.stopPropagation();
                console.log(`Delete button clicked in card ${cardIndex}!`);
                deleteTestimonial(this);
            });

            console.log(`Event listener added to delete button in card ${cardIndex}`);
        }
    });
}

// Event delegation approach - more reliable
function setupDeleteButtonListenersDelegated() {
    console.log('Setting up delete button listeners (event delegation)...');

    const testimonialsContainer = document.getElementById('testimonialsContainer');
    if (!testimonialsContainer) {
        console.log('Testimonials container not found for event delegation');
        return;
    }

    // Remove any existing event listener
    testimonialsContainer.removeEventListener('click', handleDeleteButtonClick);

    // Add event listener to the container (event delegation)
    testimonialsContainer.addEventListener('click', handleDeleteButtonClick);

    console.log('Event delegation listener added to testimonials container');
}

// Event handler for delete button clicks using event delegation
function handleDeleteButtonClick(e) {
    if (e.target.closest('.delete-testimonial-btn')) {
        e.preventDefault();
        e.stopPropagation();

        const deleteButton = e.target.closest('.delete-testimonial-btn');
        console.log('Delete button clicked via event delegation!');
        console.log('Button element:', deleteButton);

        deleteTestimonial(deleteButton);
    }
}

// Global test function - you can call this from the console
window.testDeleteFunctionality = function () {
    console.log('=== Testing Delete Functionality ===');
    console.log('Admin mode enabled:', isAdminMode);
    console.log('Delete buttons found:', document.querySelectorAll('.delete-testimonial-btn').length);
    console.log('Testimonials found:', document.querySelectorAll('.testimonial-card').length);

    const deleteButtons = document.querySelectorAll('.delete-testimonial-btn');
    deleteButtons.forEach((btn, index) => {
        console.log(`Button ${index}:`, btn);
        console.log(`Button HTML:`, btn.outerHTML);
    });

    // Try to manually trigger a delete
    if (deleteButtons.length > 0) {
        console.log('Attempting to manually trigger delete on first button...');
        const firstButton = deleteButtons[0];
        firstButton.click();
    }
};

// Make deleteTestimonial function globally accessible
window.deleteTestimonial = deleteTestimonial;

// Performance optimization: Throttle scroll events
let ticking = false;

const updateOnScroll = () => {
    animateOnScroll();
    ticking = false;
};

const requestTick = () => {
    if (!ticking) {
        requestAnimationFrame(updateOnScroll);
        ticking = true;
    }
};

window.addEventListener('scroll', requestTick);

// Add preloader
const addPreloader = () => {
    const preloader = document.createElement('div');
    preloader.innerHTML = `
        <div style="
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            transition: opacity 0.5s ease;
        ">
            <div style="
                width: 50px;
                height: 50px;
                border: 3px solid rgba(255,255,255,0.3);
                border-top: 3px solid white;
                border-radius: 50%;
                animation: spin 1s linear infinite;
            "></div>
        </div>
        <style>
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        </style>
    `;

    document.body.appendChild(preloader);

    // Remove preloader after page loads
    window.addEventListener('load', () => {
        setTimeout(() => {
            preloader.style.opacity = '0';
            setTimeout(() => {
                preloader.remove();
            }, 500);
        }, 1000);
    });
};

// Initialize preloader
addPreloader();

// Dynamic Testimonials System
let testimonials = [];
let currentTestimonialIndex = 0;

// Initialize testimonials system
function initializeTestimonials() {
    loadTestimonialsFromStorage();

    // Add a sample testimonial if none exist (for testing)
    if (testimonials.length === 0) {
        console.log('No testimonials found, adding sample testimonial for testing');
        testimonials.push({
            name: 'Test User',
            message: 'This is a test testimonial for testing delete functionality',
            date: new Date().toISOString()
        });
        saveTestimonialsToStorage();
    }

    updateTestimonialsDisplay();
    setupTestimonialNavigation();
    setupFeedbackForm();
}

// Load testimonials from localStorage
function loadTestimonialsFromStorage() {
    const savedTestimonials = localStorage.getItem('portfolioTestimonials');
    if (savedTestimonials) {
        testimonials = JSON.parse(savedTestimonials);
    }
}

// Save testimonials to localStorage
function saveTestimonialsToStorage() {
    localStorage.setItem('portfolioTestimonials', JSON.stringify(testimonials));
}

// Update testimonials display
function updateTestimonialsDisplay() {
    const container = document.getElementById('testimonialsContainer');
    const noTestimonials = document.getElementById('noTestimonials');

    if (testimonials.length === 0) {
        noTestimonials.style.display = 'block';
        return;
    }

    noTestimonials.style.display = 'none';

    // Clear existing dynamic testimonials
    const existingCards = container.querySelectorAll('.testimonial-card:not(.static)');
    existingCards.forEach(card => card.remove());

    // Add dynamic testimonials
    testimonials.forEach((testimonial, index) => {
        const testimonialCard = createTestimonialCard(testimonial, index);
        container.appendChild(testimonialCard);
    });

    // Show first testimonial
    showTestimonial(0);
}

// Create testimonial card
function createTestimonialCard(testimonial, index) {
    const card = document.createElement('div');
    card.className = 'testimonial-card';
    card.dataset.index = index;
    card.dataset.testimonialId = testimonial.id;

    const originalLanguage = testimonial.language || 'en';
    const translatedText = testimonial.translatedText || testimonial.message;

    card.innerHTML = `
        <div class="testimonial-translation">
            ${originalLanguage === 'en' ? 'EN' : 'AR'} → ${currentLanguage === 'en' ? 'EN' : 'AR'}
        </div>
        <div class="testimonial-content">
            <div class="testimonial-text">
                <p data-en="${testimonial.message}" data-ar="${translatedText}" data-original-language="${originalLanguage}">
                    "${currentLanguage === 'en' ? testimonial.message : translatedText}"
                </p>
            </div>
            <div class="testimonial-author">
                <div class="author-info">
                    <h4>${testimonial.name}</h4>
                    <span data-en="${testimonial.title}" data-ar="${testimonial.title}">${testimonial.title}</span>
                </div>
            </div>
            <div class="testimonial-actions">
                <button class="delete-testimonial-btn" title="Delete testimonial" 
                        data-en-title="Delete testimonial" data-ar-title="حذف التوصية" onclick="deleteTestimonial(this)">
                    <i class="fas fa-trash"></i>
                </button>
            </div>
        </div>
    `;

    return card;
}

// Show specific testimonial
function showTestimonial(index) {
    const cards = document.querySelectorAll('.testimonial-card');
    cards.forEach(card => card.classList.remove('active'));

    if (cards[index]) {
        cards[index].classList.add('active');
        currentTestimonialIndex = index;
    }

    updateNavigationDots();
}

// Update navigation dots
function updateNavigationDots() {
    const nav = document.getElementById('testimonialNav');
    const cards = document.querySelectorAll('.testimonial-card');

    if (cards.length <= 1) {
        nav.style.display = 'none';
        return;
    }

    nav.style.display = 'flex';
    nav.innerHTML = '';

    cards.forEach((_, index) => {
        const dot = document.createElement('button');
        dot.className = `nav-btn ${index === currentTestimonialIndex ? 'active' : ''}`;
        dot.dataset.slide = index;
        dot.addEventListener('click', () => showTestimonial(index));
        nav.appendChild(dot);
    });
}

// Setup testimonial navigation
function setupTestimonialNavigation() {
    // Auto-advance testimonials
    setInterval(() => {
        const cards = document.querySelectorAll('.testimonial-card');
        if (cards.length > 1) {
            const nextIndex = (currentTestimonialIndex + 1) % cards.length;
            showTestimonial(nextIndex);
        }
    }, 5000);
}

// Setup feedback form
function setupFeedbackForm() {
    const feedbackForm = document.getElementById('feedbackForm');
    if (feedbackForm) {
        feedbackForm.addEventListener('submit', function (e) {
            e.preventDefault();

            const formData = new FormData(this);
            const name = formData.get('name');
            const title = formData.get('title');
            const message = formData.get('message');
            const language = currentLanguage; // Use current page language

            if (!name || !title || !message) {
                showNotification('Please fill in all fields', 'error');
                return;
            }

            addNewTestimonial(name, title, message, language);
            this.reset();
        });
    }
}

// Translate single testimonial function - REMOVED 