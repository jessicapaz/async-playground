package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"time"
)

func downloadImage(status int) {
	resp, err := http.Get(fmt.Sprintf("https://http.cat/%d.jpg", status))
	check(err)
	defer resp.Body.Close()

	if resp.StatusCode == http.StatusOK {
		file, err := os.Create(fmt.Sprintf("imgs/%d.jpg", status))
		check(err)
		defer file.Close()
		_, err = io.Copy(file, resp.Body)
		check(err)
	}
}

func downloadAllImages() {
	status := []int{100, 101, 102, 200, 201, 202, 203, 204, 205, 206, 207, 208, 226, 300, 301, 302, 303, 304, 305, 307, 308, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 421, 422, 423, 424, 426, 428, 429, 431, 451, 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511}
	for _, s := range status {
		downloadImage(s)
	}
}

func check(e error) {
	if e != nil {
		log.Panic(e)
	}
}

func main() {
	err := os.Mkdir("imgs", 0755)
	check(err)

	start := time.Now()
	downloadAllImages()
	t := time.Now()
	elapsed := t.Sub(start)
	log.Printf("Elapsed: %s", elapsed)
}
