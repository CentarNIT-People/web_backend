import { Login } from "../Login/Login";
import { Dashboard } from "../Dashboard/Dashboard";
import { useEffect, useState } from "react";
import axios from "axios";

export const Me = () => {
    const [profile, setProfile] = useState({});

    const FetchAPI = () => {
        axios
            .get(
                `https://hvjvme.deta.dev/users/${sessionStorage.getItem(
                    "username"
                )}`
            )
            .then((r) => {
                setProfile(r.data);
            });
    };
    useEffect(() => {
        FetchAPI();
    }, []);

    return !sessionStorage.getItem("username") &&
        !localStorage.getItem("username") ? (
        <Login />
    ) : (
        <Dashboard />
    );
};
