#!/usr/bin/env fish

function usage
    echo "Usage: ./flatten_pdfs.fish /path/to/input /path/to/output"
    echo "Flattens all PDFs from input dir into output dir."
    echo "Keeps the larger version in case of name collisions."
end

# --- Validate arguments ---
if test (count $argv) -ne 2
    usage
    exit 1
end

set src_root $argv[1]
set dest_dir $argv[2]

if not test -d "$src_root"
    echo "Error: input path '$src_root' is not a directory."
    usage
    exit 1
end

mkdir -p "$dest_dir"

# --- Process PDFs ---
for pdf in (find "$src_root" -type f -name '*.pdf')
    set filename (basename "$pdf")
    set target "$dest_dir/$filename"

    if test -e "$target"
        set existing_size (stat -f '%z' "$target")
        set new_size (stat -f '%z' "$pdf")

        if test $new_size -gt $existing_size
            cp "$pdf" "$target"
        end
    else
        cp "$pdf" "$target"
    end
end

echo "Done. PDFs flattened into: $dest_dir"
