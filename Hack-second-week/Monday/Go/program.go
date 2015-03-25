package main

import (
    "fmt"
    "net/http"
    "os"
    )

func main() {
    response, err := http.Get("http://golang.org/")
    if err != nil {
        fmt.Printf("%s", err)
        os.Exit(1)
    } else {
        fmt.Printf("%s\n", "Here is your answer from the new language from Google:")
        fmt.Printf("%s\n", string(response.Status))
    }
}
