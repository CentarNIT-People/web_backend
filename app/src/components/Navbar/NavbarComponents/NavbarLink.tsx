import { useStyles } from "./NavbarStyles";
import { TablerIcon } from "@tabler/icons";
import { Link } from "react-router-dom";
import { Tooltip, UnstyledButton } from "@mantine/core";

interface NavbarLinkProps {
    icon: TablerIcon;
    label: string;
    active?: boolean;
    onClick?(): void;
    path: string;
}

export function NavbarLink({ path, icon: Icon, label }: NavbarLinkProps) {
    const { classes, cx } = useStyles();
    return (
        <Tooltip label={label} position="right" transitionDuration={400}>
            <UnstyledButton className={cx(classes.link)}>
                <Link to={path} className={classes.path}>
                    <Icon stroke={1} size={25} />
                </Link>
            </UnstyledButton>
        </Tooltip>
    );
}
