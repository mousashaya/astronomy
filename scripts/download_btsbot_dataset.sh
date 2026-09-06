#!/bin/bash
# Downloads BTSbot's published training/validation/test dataset (images +
# metadata) from Zenodo, to the external volume. Resumable (curl -C -) --
# safe to interrupt and rerun, picks up where it left off.
set -e

DEST="/Volumes/Machine Learning/astronomy/data/btsbot"
mkdir -p "$DEST"

download() {
    local name="$1"
    local url="$2"
    local expected_bytes="$3"
    echo "=== $name ==="
    curl -L -C - -o "$DEST/$name" "$url" \
        --retry 10 --retry-delay 30 --retry-all-errors \
        -w "\n$name: HTTP %{http_code}, %{size_download} bytes downloaded this run\n"

    actual=$(stat -f%z "$DEST/$name")
    echo "$name: $actual / $expected_bytes bytes on disk"
    if [ "$actual" -ge "$expected_bytes" ]; then
        echo "$name: COMPLETE"
    else
        echo "$name: INCOMPLETE -- rerun this script to resume"
        exit 1
    fi
}

download "metadata_v10.zip" "https://zenodo.org/api/records/10839691/files/metadata_v10.zip/content" 209653836
download "images_v10.zip" "https://zenodo.org/api/records/10839691/files/images_v10.zip/content" 19615892972

echo ""
echo "Both files downloaded. Unzipping metadata (small, quick)..."
unzip -o "$DEST/metadata_v10.zip" -d "$DEST/metadata_v10"
echo "Done. images_v10.zip left zipped (19.6GB extracted would roughly double disk use --"
echo "unzip it manually when actually ready to load the .npy files)."
