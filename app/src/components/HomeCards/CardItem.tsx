import { Button, Card, Text, Group } from "@mantine/core";
import { useStyles } from "./HomeCardsStyles";

export const CardItem = ({
    children,
    text,
}: {
    children: React.ReactNode | React.ReactNode[];
    text: string;
}) => {
    const { classes } = useStyles();
    return (
        <Card
            shadow="sm"
            p="lg"
            radius="md"
            withBorder
            style={{
                width: "100%",
                height: "100%",
                padding: 0,
            }}
        >
            <Card.Section className={classes.section}>
                <div className={classes.iconDiv}>{children}</div>
            </Card.Section>

            <Group position="apart" mt="md" mb="xs" className={classes.text}>
                <Text weight={100}>{text}</Text>
                <Button className={classes.button}>Visit</Button>
            </Group>
        </Card>
    );
};
