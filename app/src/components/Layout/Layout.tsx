import { NavbarMinimal } from "../Navbar/Navbar";
import { useStyles } from "./LayoutStyles";

interface LayoutInterface {
    children: React.ReactNode;
}

export const Layout = (props: LayoutInterface) => {
    const { classes } = useStyles();
    return (
        <div className={classes.wrapper}>
            <NavbarMinimal />
            {props.children}
        </div>
    );
};
