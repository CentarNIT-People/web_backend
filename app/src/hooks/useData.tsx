import axios from "axios";
import { useEffect, useState } from "react";

interface useDataInterface {
    name: string;
}

export const useData = (props: useDataInterface) => {
    const [data, setData] = useState([]);
    useEffect(() => {
        axios.get(`https://hvjvme.deta.dev/${props.name}/`).then((r) => {
            setData(r.data);
        });
    }, [props.name]);
    return data;
};
