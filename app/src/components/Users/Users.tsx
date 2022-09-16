import { useData } from "../../hooks/useData";
import { Layout } from "../Layout/Layout";
import { UserCard } from "./UserCard/UserCard";
import { useStyles } from "./UsersStyles";

interface ItemInterface {
    key: string;
    link: string;
    username: string;
    email: string;
}

export const Users = () => {
    const data: any = useData({ name: "users" });
    const { classes } = useStyles();
    return (
        <Layout>
            <div className={classes.wrapper}>
                {data.length > 0 &&
                    data.map((item: ItemInterface) => {
                        return (
                            <UserCard
                                name={item.username}
                                email={item.email}
                                job={"Developer"}
                                avatar=""
                            />
                        );
                    })}
            </div>
        </Layout>
    );
};
