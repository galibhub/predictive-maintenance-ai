import { createBrowserRouter } from "react-router-dom";

import Home from "../pages/Home";
import Predict from "../pages/Predict";
import Dashboard from "../pages/Dashboard";
import About from "../pages/About";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
  },
  {
    path: "/predict",
    element: <Predict />,
  },
  {
    path: "/dashboard",
    element: <Dashboard />,
  },
  {
    path: "/about",
    element: <About />,
  },
]);

export default router;