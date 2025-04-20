import difflib
import os
import time
from time import sleep
import shutil
import configparser
import semantic_version
import requests
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.progress import track
from pyfiglet import Figlet
from win10toast import ToastNotifier

# Initialize Console and Figlet
console = Console()
Render = Figlet(font="smshadow")

# Globals
x = 0
version_file = "version.txt"
config_file = "config.ini"
changelog_content = ""


def create_default_config():
    config = configparser.ConfigParser()
    config["Settings"] = {"check_delay": "10"}
    config["Webhook"] = {"url": ""}
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


def BeginWebhookProcessing():
    global changelog_content

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        console.print("[yellow] This function will send a webhook to a url of your choosing [/yellow]")

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Option", justify="center")
        table.add_column("Action")
        table.add_row("1", "Configure Webhook URL")
        table.add_row("2", "Make Changelog (In Terminal)")
        table.add_row("3", "Load Changelog (from a MD or TXT file)")
        table.add_row("4", "[red]SEND CHANGELOG[/red]")
        table.add_row("5", "Back to Main Menu")
        console.print(table)

        choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4", "5"])

        if choice == "1":
            config = configparser.ConfigParser()
            if os.path.exists(config_file):
                config.read(config_file)

            webhook = Prompt.ask("Enter webhook URL")
            config["Webhook"] = {"url": webhook}
            with open(config_file, "w") as configfile:
                config.write(configfile)
            console.print("[green]Webhook URL saved.[/green]")

        elif choice == "2":
            console.print("[cyan]Write your changelog below. End input with a single line containing only 'END'.[/cyan]")
            lines = []
            while True:
                line = input()
                if line.strip().upper() == "END":
                    break
                lines.append(line)
            changelog_content = "\n".join(lines)
            console.print("[green]Changelog content updated![/green]")
            sleep(2)

        elif choice == "3":
            file_path = Prompt.ask("Enter path to changelog file")
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    changelog_content = file.read()

                console.print("[green]Changelog loaded![/green]")
                sleep(3)
            else:
                console.print("[red]File not found.[/red]")
                sleep(3)

        elif choice == "4":
            if not changelog_content:
                console.print("[red]No changelog content found. Please create or load one first.[/red]")
                sleep(2)
                continue

            config = configparser.ConfigParser()
            if os.path.exists(config_file):
                config.read(config_file)
                webhook_url = config.get("Webhook", "url", fallback="")

                if webhook_url:
                    try:
                        toast = ToastNotifier()
                        response = requests.post(
                        webhook_url,
                        json={"content": changelog_content},
                        headers={"Content-Type": "application/json"})
                        if response.status_code == 204 or response.ok:
                            #console.print("[bold green]Changelog sent successfully![/bold green]")
                            toast.show_toast(
                                "Quarrelsome"
                                "Webhook Sent!!",
                                "Haiya .. Webhook has be been sent successfully ;3",
                                duration = 20,
                                icon_path = "icon.ico",
                                threaded = True,
                                )
                        else:
                            console.print(f"[red]Failed to send webhook. Status code: {response.status_code}[/red]")
                    except Exception as e:
                        console.print(f"[red]Error sending webhook: {e}[/red]")
                else:
                    console.print("[red]Webhook URL is not configured.[/red]")
                    sleep(3)
            else:
                console.print("[red]Config file not found.[/red]")

        elif choice == "5":
            break


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
        console.print(Render.renderText("// Q u a r r e l s o m e"), "version : 1.5.2")
        console.print(Panel("[bold cyan]This tool is used to semanticly version software. One of my actual useful tools...[/bold cyan]", subtitle="Made with ♥ by NeoDymium/SherkBoi :3"))

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Option", justify="center")
        table.add_column("Action")
        table.add_row("1", "Start Monitor")
        table.add_row("2", "Information")
        table.add_row("3", "Current Version")
        table.add_row("4", "Configure")
        table.add_row("5", "Send Webhook")
        table.add_row("6", "Exit")
        console.print(table)

        choice = Prompt.ask("\nChoose an option", choices=["1", "2", "3", "4", "5", "6"], default="1")

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
            BeginWebhookProcessing()

        elif choice == "6":
            console.print("[cyan]Goodbye! Thankie for using ^>w<^..![/cyan]")
            break


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        console.print("\n[bold red]Exited by user.[/bold red]")
