import sys

from modules.utils.create_all_tables import create_all_tables


def aneel_controller(command):
    if command == "enterprise_gd_information_technical_wind":
        from modules.aneel.enterprise_gd_information_technical_wind import run
        run()

    if command == "venture_gd_photovoltaic_technical_information":
        from modules.aneel.venture_gd_photovoltaic_technical_information import run
        run()

    if command == "enterprise_gd_technical_information_hydroelectric":
        from modules.aneel.enterprise_gd_technical_information_hydroelectric import run
        run()

    if command == "enterprise_gd_technical_information_thermoelectric":
        from modules.aneel.enterprise_gd_technical_information_thermoelectric import run
        run()

    if command == "distributed_generation_enterprise":
        from modules.aneel.distributed_generation_enterprise import run
        run()


def database_controller(command):
    if command == "create_all_tables":
        create_all_tables()


def main(argv):
    args_split = argv[1].split(":")
    group = args_split[0]
    if group == "aneel":
        aneel_controller(args_split[1])
    if group == "database":
        database_controller(args_split[1])


if __name__ == "__main__":
    main(sys.argv)
