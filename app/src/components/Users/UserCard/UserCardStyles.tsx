import { createStyles } from "@mantine/core";

export const useStyles = createStyles((theme) => ({
    wrapper: {
        backgroundColor:
            theme.colorScheme === "dark" ? theme.colors.dark[7] : theme.white,
        width: "25%",
        margin: "3% 3%",
        padding: theme.spacing.lg,
        borderRadius: theme.radius.md,
    },
    title: {
        fontSize: theme.fontSizes.lg,
        fontWeight: 500,
        marginTop: theme.spacing.md,
        textAlign: "center",
    },
    button: {
        marginTop: theme.spacing.lg,
        width: "100%",
    },
    desc: {
        textAlign: "center",
        color: theme.colors.gray[6],
        fontSize: theme.fontSizes.sm,
    },
}));
