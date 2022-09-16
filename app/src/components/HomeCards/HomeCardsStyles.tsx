import { createStyles } from "@mantine/core";

export const useStyles = createStyles((theme) => ({
    iconDiv: {
        background:
            theme.colorScheme === "dark"
                ? theme.colors.dark[6]
                : theme.white[0],
        padding: "10%",
        width: "100%",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "100%",
        transition: "ease-in-out 0.25s all",
        borderBottom:
            theme.colorScheme === "dark"
                ? `1px solid ${theme.colors.gray[5]}`
                : `1px solid ${theme.colors.dark[0]}`,
        "&:hover": {
            scale: "1.03",
            cursor: "pointer",
            backgroundColor: theme.fn.variant({
                variant: "light",
                color: theme.primaryColor,
            }).background,
            color: theme.fn.variant({
                variant: "light",
                color: theme.primaryColor,
            }).color,
        },
        "@media (max-width: 1200px)": {
            padding: "30% 0%",
        },
    },
    link: {
        width: "100%",
        height: "100%",
        textDecoration: "none",
    },
    section: {
        height: "80%",
    },
    text: {
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "20%",
        width: "100%",
        flexDirection: "column",
        marginTop: theme.spacing.md,
        marginBottom: theme.spacing.xs,
    },
    grid: {
        width: "100%",
        height: "78vh",
        marginTop: "2%",
        padding: "0% 2%",
        "@media (max-width: 1200px)": {
            marginTop: "5%",
            padding: "0% 20%",
        },
        "@media (max-width: 800px)": {
            marginTop: "5%",
            padding: "0% 10%",
        },
    },
    button: {
        "@media (max-width: 900px)": {
            display: "none",
        },
    },
    wrapper: {
        width: "100%",
        height: "100%",
        padding: theme.spacing.lg,
        boxShadow: theme.shadows.md,
        borderRadius: theme.radius.md,
    },
    name: {
        fontWeight: 200,
        fontSize: 20,
    },
}));
