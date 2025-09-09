self.addEventListener("install", function(event) {
    console.log("Service Worker: Kuruluyor...");
    event.waitUntil(
        caches.open("v1").then(function(cache) {
            return cache.addAll([
                "/",
                "/assets/manifest.json",
                "/assets/images/logo.png",
                "/assets/images/logo.png"
            ]);
        })
    );
});

self.addEventListener("fetch", function(event) {
    event.respondWith(
        caches.match(event.request).then(function(response) {
            return response || fetch(event.request);
        })
    );
});
