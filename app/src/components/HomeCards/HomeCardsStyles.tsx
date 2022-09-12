import { createStyles } from "@mantine/core";

export const useStyles = createStyles((theme) => ({
    iconDiv: {
        background: "white",
        padding: "10%",
        width: "100%",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "100%",
        transition: "ease-in-out 0.25s all",
        borderBottom: "1px solid #dee2e6",
        "&:hover": {
            scale: "1.04",
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
    },
    grid: {
        width: "100%",
        height: "75%",
        marginTop: "3%",
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
}));
