import { Link } from "react-router-dom";
import { useStyles } from "./HomeCardsStyles";

interface Props {
    link: string;
    children: React.ReactNode | React.ReactNode[];
}

export const CardLink: React.FC<Props> = (props) => {
    const { classes } = useStyles();
    return (
        <Link to={props.link} className={classes.link}>
            {props.children}
        </Link>
    );
};
