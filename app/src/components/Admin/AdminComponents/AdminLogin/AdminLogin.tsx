import {
    TextInput,
    PasswordInput,
    Paper,
    Title,
    Container,
    Button,
} from "@mantine/core";
import React, { useState } from "react";
import axios from "axios";
import { useStyles } from "./AdminLoginStyles";
import { Layout } from "../../../Layout/Layout";

interface AdminLoginInterface {
    login: boolean;
    setLogin: React.Dispatch<React.SetStateAction<boolean>>;
}

export function AdminLogin(props: AdminLoginInterface) {
    const { classes } = useStyles();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleClick = () => {
        axios
            .get(
                `https://hvjvme.deta.dev/admin/login?username=${username}&password=${password}`
            )
            .then((r) => {
                props.setLogin(true);
            })
            .catch((msg) => {
                alert("Invalid Credentials!");
            });
    };

    return (
        <Layout>
            <Container size={420} my={40} className={classes.wrapper}>
                <Title align="center" className={classes.title}>
                    Welcome back!
                </Title>
                <Paper
                    withBorder
                    shadow="md"
                    p={30}
                    mt={30}
                    radius="md"
                    style={{ width: "80%" }}
                >
                    <TextInput
                        label="Username"
                        placeholder="Your username"
                        required
                        onChange={(e) => {
                            setUsername(e.target.value);
                        }}
                        value={username}
                    />
                    <PasswordInput
                        label="Password"
                        onChange={(e) => {
                            setPassword(e.target.value);
                        }}
                        value={password}
                        placeholder="Your password"
                        required
                        mt="md"
                    />
                    <Button fullWidth mt="xl" onClick={handleClick}>
                        Login
                    </Button>
                </Paper>
            </Container>
        </Layout>
    );
}
