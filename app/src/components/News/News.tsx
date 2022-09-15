import { useData } from "../../hooks/useData";
import { Layout } from "../Layout/Layout";

interface ItemInterface {
    author: string;
    description: string;
    image: string;
    key: string;
    title: string;
}

export const News = () => {
    const data: any = useData({ name: "news" });
    return (
        <Layout>
            <div>
                {data.length > 0 &&
                    data.map((item: ItemInterface) => {
                        return <h1 key={item.key}>{item.title}</h1>;
                    })}
            </div>
        </Layout>
    );
};
