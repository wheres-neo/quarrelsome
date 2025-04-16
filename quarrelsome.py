import difflib
import os
import time
import shutil
import configparser
import semantic_version
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.progress import track
from pyfiglet import Figlet

# Initialize Console and Figlet
console = Console()
Render = Figlet(font="smshadow")

# Globals
x = 0
version_file = "version.txt"
config_file = "config.ini"


def create_default_config():
    config = configparser.ConfigParser()
    config["Settings"] = {"check_delay": "10"}
    with open(config_file, "w") as configfile:
        config.write(configfile)


def load_config():
    config = configparser.ConfigParser()
    if os.path.exists(config_file):
        config.read(config_file)
        try:
            return int(config.get("Settings", "check_delay", fallback="10"))
        except ValueError:
            console.print("[yellow]Invalid check_delay in config.ini. Using default of 10 seconds.[/yellow]")
            return 10
    else:
        create_default_config()
        return 10


def update_config():
    config = configparser.ConfigParser()
    if os.path.exists(config_file):
        config.read(config_file)

    current_delay = config.get("Settings", "check_delay", fallback="10")
    console.print(f"Current check delay is [cyan]{current_delay}[/cyan] seconds.")
    new_delay = Prompt.ask("Enter new check delay (in seconds)", default=current_delay)

    try:
        int(new_delay)
    except ValueError:
        console.print("[red]Invalid input. Must be a number.[/red]")
        return

    config["Settings"]["check_delay"] = new_delay
    with open(config_file, "w") as configfile:
        config.write(configfile)

    console.print("[green]Configuration updated![/green]")


def get_current_version():
    if os.path.exists(version_file):
        with open(version_file, "r") as f:
            return f.read().strip()
    return "0.0.0-0"


def load_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except Exception as e:
        console.print(f"[red]Error reading file: {e}[/red]")
        return []


def save_prev(code_file):
    try:
        shutil.copy(code_file, code_file + ".prev")
    except Exception as e:
        console.print(f"[red]Error saving previous copy: {e}[/red]")


def track_code(file_path):
    global x
    delay = load_config()
    version = semantic_version.Version(get_current_version())
    prev_code = load_file(file_path + ".prev")

    while True:
        console.print(f'[bold bright_magenta]Current step: {x}[/bold bright_magenta]')
        for _ in track(range(delay), description="Waiting for next check..."):
            time.sleep(1)
            x += 1
            if x > 10:
                os.system("cls" if os.name == "nt" else "clear")
                x = 0

        curr_code = load_file(file_path)

        if prev_code and curr_code:
            diff = list(difflib.unified_diff(prev_code, curr_code))
            if diff:
                major, minor, patch = version.major, version.minor, version.patch
                build = int(version.build[0]) if version.build else 0

                adds = sum(1 for l in diff if l.startswith('+') and not l.startswith('+++'))
                dels = sum(1 for l in diff if l.startswith('-') and not l.startswith('---'))

                if adds > dels:
                    minor += 1
                    build = 0
                elif dels > adds:
                    major += 1
                    build = 0
                else:
                    patch += 1
                    build += 1

                version = semantic_version.Version(f"{major}.{minor}.{patch}-{build}")
                with open(version_file, 'w') as vf:
                    vf.write(str(version))

                console.print(f"[green]New version detected: {version}[/green]")
                save_prev(file_path)
                prev_code = curr_code
        else:
            console.print("[yellow]Saving base version...[/yellow]")
            save_prev(file_path)
            prev_code = curr_code


def main_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        console.print(Render.renderText("// Q u a r r e l s o m e"), "version : 1.5.1")
        console.print(Panel("[bold cyan]This tool is used to semanticly version software. One of my actual useful tools...[/bold cyan]", subtitle="Made with ♥ by NeoDymium/SherkBoi :3"))

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Option", justify="center")
        table.add_column("Action")
        table.add_row("1", "Start Monitor")
        table.add_row("2", "Information")
        table.add_row("3", "Current Version")
        table.add_row("4", "Configure")
        table.add_row("5", "Exit")
        console.print(table)

        choice = Prompt.ask("\nChoose an option", choices=["1", "2", "3", "4", "5"], default="1")

        if choice == "1":
            path = Prompt.ask("Enter path to code file")
            if os.path.exists(path):
                try:
                    track_code(path)
                except KeyboardInterrupt:
                    console.print("\n[bold red]Stopped Monitoring.[/bold red]")
                    input("\nPress Enter to return to menu...")
            else:
                console.print("[bold red]File not found![/bold red]")
                time.sleep(2)

        elif choice == "2":
            console.print(Panel(
                "[bold cyan]Information[/bold cyan]\n"
                "[white]I was bored and wanted a project to work on — like yeah, just chillin' —\n"
                "and then thought: why not make something *actually* useful?\n\n"
                "Quarrelsome is a semantic version tracker for your code.\n"
                "It checks your files, detects changes, and updates version numbers\n"
                "automagically based on how heavy the edits are. Big brain stuff.\n\n"
                "Why? Because versioning sucks. Forget manually editing version.txt —\n"
                "let this bad boy do it for you.\n\n"
                "Plus, you can tweak how often it checks (check_delay in config),\n"
                "and it even saves previous versions, just in case.\n\n"
                "[bold magenta]So yeah — code, break stuff, and let Quarrelsome keep score.[/bold magenta][/white]",
                subtitle="By NeoDymium / SherkBoi :3"
            ))

            input("\nPress Enter to return to menu...")

        elif choice == "3":
            current = get_current_version()
            console.print(f"[bold green]Current Version:[/bold green] {current}")
            input("\nPress Enter to return to menu...")

        elif choice == "4":
            update_config()
            input("\nPress Enter to return to menu...")

        elif choice == "5":
            console.print("[cyan]Goodbye! Thankie for using ^>w<^..![/cyan]")
            break



if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        console.print("\n[bold red]Exited by user.[/bold red]")
