import { NavbarMinimal } from "../Navbar/Navbar";

interface LayoutInterface {
    children: React.ReactNode;
}

export const Layout = (props: LayoutInterface) => {
    return (
        <div>
            <NavbarMinimal />
            {props.children}
        </div>
    );
};
