for path in /input/*.mkv; do
    fname=$(basename "$path")
    # echo /output/$fname
    ffmpeg -i "$path" -c:v copy -c:a copy -vf "transpose=1" "/output/$fname"
done
