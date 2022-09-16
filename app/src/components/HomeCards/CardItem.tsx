import { Button, Card, Text, Group } from "@mantine/core";
import { useStyles } from "./HomeCardsStyles";

interface CardItemInterface {
    children: React.ReactNode | React.ReactNode[];
    text: string;
}

export const CardItem = (props: CardItemInterface) => {
    const { classes } = useStyles();
    return (
        <Card withBorder className={classes.wrapper}>
            <Card.Section className={classes.section}>
                <div className={classes.iconDiv}>{props.children}</div>
            </Card.Section>
            <Group className={classes.text}>
                <Text className={classes.name}>{props.text}</Text>
                <Button className={classes.button}>Visit</Button>
            </Group>
        </Card>
    );
};
