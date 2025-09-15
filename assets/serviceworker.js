const CACHE_NAME = "enufak-cache-v1";

self.addEventListener("install", function(event) {
    event.waitUntil(
        caches.open(CACHE_NAME).then(function(cache) {
            return cache.addAll([
                "/uygulama/kesfet/",
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
            return response || fetch(event.request).catch(() => caches.match("/offline.html"));
        })
    );
});