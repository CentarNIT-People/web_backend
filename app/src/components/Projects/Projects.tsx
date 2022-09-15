import { useData } from "../../hooks/useData";
import { Layout } from "../Layout/Layout";

interface ItemInterface {
    key: string;
    language: string;
    link: string;
    name: string;
}

export const Project = () => {
    const data: any = useData({ name: "projects" });
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
