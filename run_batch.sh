for path in /input/*.mkv; do
    fname=$(basename "$path")
    # echo /output/$fname
    ffmpeg -i "$path" -vf "transpose=1" "/output/$fname"
done
