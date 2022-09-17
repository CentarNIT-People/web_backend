import { useState } from "react";
import { AdminLogin } from "./AdminComponents/AdminLogin/AdminLogin";

export const Admin = () => {
    const [login, setLogin] = useState(false);
    return (
        <>
            {login === false ? (
                <AdminLogin login={login} setLogin={setLogin} />
            ) : (
                <h1>Admin</h1>
            )}
        </>
    );
};
