import { useData } from "../../hooks/useData";
import { Layout } from "../Layout/Layout";
import { NewsCard } from "./NewsCard/NewsCard";
import { useStyles } from "./NewsStyles";

interface ItemInterface {
    author: string;
    description: string;
    image: string;
    key: string;
    title: string;
}

export const News = () => {
    const { classes } = useStyles();
    const data: any = useData({ name: "news" });
    return (
        <Layout>
            <div className={classes.wrapper}>
                {data.length > 0 &&
                    data.map((item: ItemInterface, index: number) => {
                        return <NewsCard key={item.key} />;
                    })}
            </div>
        </Layout>
    );
};

// index % 2
