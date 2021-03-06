import React, { useContext } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { Context } from "./store/appContext.js";

import { Home } from "./pages/home";

import injectContext from "./store/appContext";
import { Registro } from "./pages/registro.jsx";

import { Header } from "./component/partials/header.jsx";
import { Footer } from "./component/footer";
import { Login } from "./pages/login.jsx";
import { Profile } from "./component/profile.jsx";
import { Template2 } from "./pages/templates/template-two.jsx"; //
import { AddMenu } from "./pages/admin/addMenu.jsx";
import { Template1 } from "./pages/templates/template1.jsx";

import { Error404 } from "./pages/404.jsx";

const Layout = () => {
	const basename = process.env.BASENAME || "";
	const { store, actions } = useContext(Context);
	return (
		<BrowserRouter basename={basename}>
			{store.showNavigation ? <Header /> : null}
			<Switch>
				<Route exact path="/">
					<Home />
				</Route>
				<Route exact path="/place/:id">
					<Profile />
				</Route>
				<Route exact path="/register">
					<Login />
				</Route>
				<Route exact path="/login">
					<Login />
				</Route>
				<Route exact path="/place/:id/addmenu">
					<AddMenu />
				</Route>
				<Route exact path="/place/:id/menu/1">
					<Template1 />
				</Route>
				<Route exact path="/place/:id/menu/2">
					<Template2 />
				</Route>
				<Route>
					<h1>Not found!</h1>
				</Route>
			</Switch>
			{store.showNavigation ? <Footer /> : null}
		</BrowserRouter>
	);
};

export default injectContext(Layout);
