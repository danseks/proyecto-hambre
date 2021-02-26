import React, { Fragment, useContext } from "react";
import { Link } from "react-router-dom";
import { Navbar, Nav, NavDropdown, Form, FormControl, Button, Container, Jumbotron, Row, Col } from "react-bootstrap";
import { BUTTON } from "../component/button.jsx";
import { Context } from "../store/appContext";

export const Header = () => {
	const { store, actions } = useContext(Context);
	return (
		<>
			<header className="navbar">
				<Container>
					<Navbar expand="lg">
						<Link to="/">
							<Navbar.Brand>
								{" "}
								<img
									alt=""
									src="https://zimwebtech.com/assets/images/media/012.png"
									width="70"
									height="50"
									className="d-inline-block align-top"
								/>{" "}
							</Navbar.Brand>
						</Link>
						<Navbar.Toggle aria-controls="basic-navbar-nav" />
					</Navbar>
					{/* <BUTTON title="Eliminar cuenta" click={() => actions.deleteProfile(store.profile_id)} />
					<BUTTON title="Cerrar Sesion" /> */}
				</Container>
			</header>
		</>
	);
};
