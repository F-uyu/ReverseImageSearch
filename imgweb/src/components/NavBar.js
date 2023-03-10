//Navbar
import React from "react";
import {useRef} from "react";
import {FaBars, FaTimes} from "react-icons/fa";
import './NavBar.css';
import image from "../Images/SciFi.jpeg"
function NavBar(){
    const navRef = useRef();
    const showNavBar = () => {
        navRef.current.classList.toggle("responsive_nav");
    }
    return (
        <div style = {{
            backgroundImage: `url(${image})`,
            backgroundPosition: 'center',
            backgroundSize: 'cover',
            backgroundRepeat: 'no-repeat',
            width: '100vw',
            height: '100vh'

        }}>
            <header>
                <h3>Logo</h3>
                <nav ref = {navRef}>
                    <a href = "/#">Home</a>
                    <a href = "/#">My works</a>
                    <a href = "/#">Blog</a>
                    <a href = "/#">About me</a>
                    <button className = "nav-btn nav-close-btn" onClick = {showNavBar} >
                        <FaTimes />
                    </button>
                </nav>
                <button className = "nav-btn" onClick = {showNavBar}>
                    <FaBars />
                </button>
            </header>
        </div>
    )
}

export default NavBar;

