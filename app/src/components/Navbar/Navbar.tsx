import { Navbar, Stack } from "@mantine/core";
import { useState } from "react";
import { NavbarLink } from "./NavbarComponents/NavbarLink";
import { useStyles } from "./NavbarComponents/NavbarStyles";
import { mockdata } from "./NavbarComponents/NavbarData";

export function NavbarMinimal() {
    const [active, setActive] = useState(2);
    const { classes } = useStyles();

    const links = mockdata.map((link, index) => (
        <NavbarLink
            {...link}
            path={link.path}
            key={link.label}
            active={index === active}
            onClick={() => setActive(index)}
        />
    ));

    return (
        <Navbar p="md" className={classes.nav}>
            <Navbar.Section className={classes.nav_section}>
                <Stack spacing={45} className={classes.stack}>
                    {links}
                </Stack>
            </Navbar.Section>
        </Navbar>
    );
}
