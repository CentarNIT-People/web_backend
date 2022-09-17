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
            <Avatar
                src={props.avatar}
                className={classes.avatar}
                size={120}
                color="blue"
            />
            <Text className={classes.title}>{props.name}</Text>
            <Text className={classes.desc}>
                {props.email} • {props.job}
            </Text>
            <Button className={classes.button}>Visit Profile</Button>
        </Paper>
    );
}
