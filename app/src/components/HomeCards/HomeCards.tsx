import { SimpleGrid } from "@mantine/core";
import { IconAppWindow, IconNews, IconUsers } from "@tabler/icons";
import { useStyles } from "./HomeCardsStyles";
import { CardItem } from "./CardItem";
import { CardLink } from "./CardLink";

export const Cards = () => {
    const { classes } = useStyles();
    return (
        <SimpleGrid
            className={classes.grid}
            cols={3}
            spacing="lg"
            breakpoints={[
                { maxWidth: 1400, cols: 3, spacing: "md" },
                { maxWidth: 1200, cols: 1, spacing: 50 },
                { maxWidth: 800, cols: 1, spacing: 50 },
            ]}
        >
            <CardLink link="users">
                <CardItem text="Users">
                    <IconUsers size={150} stroke={0.2} />
                </CardItem>
            </CardLink>
            <CardLink link="news">
                <CardItem text="News">
                    <IconNews size={150} stroke={0.2} />
                </CardItem>
            </CardLink>
            <CardLink link="projects">
                <CardItem text="Projects">
                    <IconAppWindow size={150} stroke={0.2} />
                </CardItem>
            </CardLink>
        </SimpleGrid>
    );
};
