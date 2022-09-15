import { useData } from "../../hooks/useData";
import { Layout } from "../Layout/Layout";

interface ItemInterface {
    key: string;
    language: string;
    link: string;
    name: string;
}

export const Users = () => {
    const data: any = useData({ name: "users" });
    return (
        <Layout>
            <div>
                {data.length > 0 &&
                    data.map((item: ItemInterface) => {
                        return <h1 key={item.key}>{item.name}</h1>;
                    })}
            </div>
        </Layout>
    );
};
