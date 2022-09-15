import { BrowserRouter } from "react-router-dom";
import { AppRoutes } from "./routes";

import {
    MantineProvider,
    ColorSchemeProvider,
    ColorScheme,
} from "@mantine/core";
import { useState } from "react";

export const App = () => {
    const [colorScheme, setColorScheme] = useState<ColorScheme>("light");
    const toggleColorScheme = (value?: ColorScheme) =>
        setColorScheme(value || (colorScheme === "dark" ? "light" : "dark"));

    return (
        <ColorSchemeProvider
            colorScheme={colorScheme}
            toggleColorScheme={toggleColorScheme}
        >
            <MantineProvider
                theme={{ colorScheme }}
                withGlobalStyles
                withNormalizeCSS
            >
                <BrowserRouter>
                    <AppRoutes />
                </BrowserRouter>
            </MantineProvider>
        </ColorSchemeProvider>
    );
};
