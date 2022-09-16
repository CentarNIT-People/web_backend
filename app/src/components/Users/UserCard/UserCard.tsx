import { Avatar, Text, Button, Paper } from "@mantine/core";
import { useStyles } from "./UserCardStyles";

interface UserInfoActionProps {
    avatar: string;
    name: string;
    email: string;
    job: string;
}

export function UserCard(props: UserInfoActionProps) {
    const { classes } = useStyles();
    return (
        <Paper withBorder className={classes.wrapper}>
            <Avatar src={props.avatar} size={120} radius={120} mx="auto" />
            <Text className={classes.title}>{props.name}</Text>
            <Text className={classes.desc}>
                {props.email} • {props.job}
            </Text>
            <Button className={classes.button}>Send message</Button>
        </Paper>
    );
}
