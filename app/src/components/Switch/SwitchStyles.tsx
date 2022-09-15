import { createStyles } from "@mantine/core";

export const useStyles = createStyles((theme) => ({
    root: {
        display: "flex",
        alignItems: "center",
        position: "relative",
        "& *": {
            cursor: "pointer",
        },
        marginTop: 0,
    },

    icon: {
        pointerEvents: "none",
        position: "absolute",
        zIndex: 1,
        top: 3,
    },

    iconLight: {
        left: 4,
        color: theme.white,
    },

    iconDark: {
        right: 4,
        color: theme.colors.gray[6],
    },
}));
