import sys
import pylnk3

def main():
    if len(sys.argv) != 2:
        print(f"\n>> Usage: python {sys.argv[0]} <path_to_lnk_file>")
        sys.exit(1)

    lnk_path = sys.argv[1]

    try:
        with open(lnk_path, "rb") as f:
            lnk = pylnk3.parse(f)

        print("\n🔍 Extracted .lnk Attributes and Values:\n")
        for attr in dir(lnk):
            if not attr.startswith("__") and not callable(getattr(lnk, attr)):
                try:
                    value = getattr(lnk, attr)
                    print(f"{attr:<20}: {value}")
                except Exception as e:
                    print(f"{attr:<20}: [Error reading value]")

    except Exception as e:
        print("Error reading .lnk file:", e)

if __name__ == "__main__":
    main()