import { Routes, Route } from "react-router-dom";
import { Home } from "./Home/Home";
import { Me } from "./Me/Me";
import { Project } from "./Projects/Projects";
import { News } from "./News/News";
import { Users } from "./Users/Users";

export const AppRoutes = () => {
    return (
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/account" element={<Me />} />
            <Route path="/projects" element={<Project />} />
            <Route path="/news" element={<News />} />
            <Route path="/users" element={<Users />} />
        </Routes>
    );
};
