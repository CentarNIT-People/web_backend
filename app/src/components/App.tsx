import { BrowserRouter, Routes, Route } from "react-router-dom";
import { NavbarMinimal } from "./Navbar/Navbar";

export const App = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<NavbarMinimal />} />
            </Routes>
        </BrowserRouter>
    );
};
