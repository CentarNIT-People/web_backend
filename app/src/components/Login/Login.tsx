import {
    TextInput,
    PasswordInput,
    Checkbox,
    Anchor,
    Paper,
    Title,
    Text,
    Container,
    Group,
    Button,
} from "@mantine/core";
import { useState } from "react";
import axios from "axios";
import { useStyles } from "./LoginStyles";
export function Login() {
    const { classes } = useStyles();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [remember, setRemember] = useState("");

    const handleClick = () => {
        axios
            .get(
                `https://hvjvme.deta.dev/account/login?username=${username}&password=${password}`
            )
            .then((r) => {
                if (remember === "true") {
                    localStorage.setItem("username", username);
                } else {
                    sessionStorage.setItem("username", username);
                }
                window.location.reload();
            })
            .catch((msg) => {
                alert("Invalid Credentials!");
            });
    };

    return (
        <Container size={420} my={40} className={classes.wrapper}>
            <Title align="center" className={classes.title}>
                Welcome back!
            </Title>
            <Text color="dimmed" size="sm" align="center" mt={5}>
                Do not have an account yet?{" "}
                <Anchor<"a"> href="register" size="sm">
                    Create account
                </Anchor>
            </Text>

            <Paper withBorder shadow="md" p={30} mt={30} radius="md">
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
                <Group position="apart" mt="md">
                    <Checkbox
                        label="Remember me"
                        value={remember}
                        onClick={() => setRemember("true")}
                    />
                    <Anchor<"a"> href="/" size="sm">
                        Back to dashboard
                    </Anchor>
                </Group>
                <Button fullWidth mt="xl" onClick={handleClick}>
                    Login
                </Button>
            </Paper>
        </Container>
    );
}
