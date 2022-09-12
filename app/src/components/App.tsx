import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Home } from "./Home/Home";
import { Login } from "./Login/Login";

export const App = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/account" element={<Login />} />
            </Routes>
        </BrowserRouter>
    );
};
