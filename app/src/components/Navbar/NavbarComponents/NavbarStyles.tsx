import { createStyles } from "@mantine/core";

export const useStyles = createStyles((theme, _params) => ({
    link: {
        transition: "ease-in-out 0.2s all",
        width: 50,
        height: 50,
        borderRadius: theme.radius.md,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        color:
            theme.colorScheme === "dark"
                ? theme.colors.gray[1]
                : theme.colors.gray[9],

        "& child, &:hover": {
            transform: "translateY(-1px)",
            scale: "1.05",
        },
    },
    path: {
        transition: "ease-in-out 0.1s all",
        borderRadius: theme.radius.md,
        width: "100%",
        height: "100%",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        color:
            theme.colorScheme === "dark"
                ? theme.colors.dark[0]
                : theme.colors.gray[7],

        "&:hover": {
            transition: "ease-in-out all 0.3s",
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
    },
    nav: {
        width: "100%",
        display: "flex",
        height: "80px",
        flexDirection: "row",
        justifyContent: "space-around",
        marginTop: 20,
    },
    nav_section: {
        width: "100%",
        display: "flex",
        margin: 0,
    },
    stack: {
        display: "flex",
        flexDirection: "row",
        width: "100%",
    },
}));
