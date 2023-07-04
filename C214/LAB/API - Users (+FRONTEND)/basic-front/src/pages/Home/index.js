import Sidebar from '../../components/Sidebar';
import Lottie from "lottie-react";

import './style.css';

export default function Home() {

    return (
        <div>
            <Sidebar />
            <div className="content">
                <div className="lottie">
                    <Lottie
                    />
                </div>
            </div>
        </div>
    )
}