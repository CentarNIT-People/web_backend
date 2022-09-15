import { createStyles } from "@mantine/core";

export const useStyles = createStyles((theme) => ({
    wrapper: {
        width: "100%",
        height: "65vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
    },
    title: {
        fontFamily: `Greycliff CF, ${theme.fontFamily}`,
        fontWeight: 900,
    },
}));
