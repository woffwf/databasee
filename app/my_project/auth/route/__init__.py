from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.available_flight_route import available_flight_bp
    from .orders.airline_route import airline_bp
    from .orders.info_for_buyed_tickets_route import info_for_buyed_tickets_bp
    from .orders.airport_route import airport_bp
    from .orders.avaible_weight_route import avaible_weight_bp
    from .orders.tickets_route import tickets_bp
    from .orders.user_route import user_bp
    from .orders.avaible_flight_has_avaible_weight_route import avaible_flight_has_avaible_weight_bp
    from .orders.user_purchase_history_route import user_purchase_history_bp
    from .orders.connected_flight_route import connected_flight_bp
    from .orders.additional_route import additional_bp

    app.register_blueprint(available_flight_bp)
    app.register_blueprint(airline_bp)
    app.register_blueprint(info_for_buyed_tickets_bp)
    app.register_blueprint(airport_bp)
    app.register_blueprint(avaible_weight_bp)
    app.register_blueprint(tickets_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(avaible_flight_has_avaible_weight_bp)
    app.register_blueprint(user_purchase_history_bp)
    app.register_blueprint(connected_flight_bp)
    app.register_blueprint(additional_bp)
