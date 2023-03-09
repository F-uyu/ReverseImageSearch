//Background picture
import Paper from '@mui/material/Paper'
import image from "../Images/SciFi.jpeg"
import './TopPage.css'
const TopPage = () => {
    return (
        <>
            <div style = {{
                backgroundImage: `url(${image})`,
                backgroundPosition: 'center',
                backgroundSize: 'cover',
                backgroundRepeat: 'no-repeat',
                width: '100vw',
                height: '100vh'

            }}>

                Hello World
            </div>
        </>
    )
}

export default TopPage