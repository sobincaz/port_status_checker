
import socket
from datetime import datetime

def check_port(host, port, timeout=1):
    """
    Check TCP port status.
    Returns Open, Closed, or Filtered.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        result = sock.connect_ex((host, port))

        if result == 0:
            return "Open"
        elif result == 111 or result == 10061:
            return "Closed"
        else:
            return "Filtered"

    except socket.timeout:
        return "Filtered"

    except OSError:
        return "Filtered"

    finally:
        sock.close()


def main():
    print("=" * 55)
    print("           TCP PORT STATUS CHECKER")
    print("=" * 55)

    host = input("Enter target IP (127.0.0.1 only): ").strip()

    # Restrict scanning to localhost
    if host != "127.0.0.1":
        print("Error: This educational version supports localhost only.")
        return

    try:
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))

        if not (1 <= start_port <= end_port <= 65535):
            print("Invalid port range.")
            return

    except ValueError:
        print("Please enter valid port numbers.")
        return

    print("\nScan started:", datetime.now())
    print(f"\nTarget Host: {host}")
    print(f"Port Range: {start_port}-{end_port}")
    print("-" * 55)

    print(f"{'PORT':<12}{'STATUS':<18}{'SERVICE'}")
    print("-" * 55)

    services = {
        21: "FTP",
        22: "SSH",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        443: "HTTPS",
        3306: "MySQL",
        5432: "PostgreSQL"
    }

    for port in range(start_port, end_port + 1):
        status = check_port(host, port)

        service = services.get(port, "Unknown")

        print(f"{port:<12}{status:<18}{service}")

    print("-" * 55)
    print("Scan completed:", datetime.now())


if __name__ == "__main__":
    main()
