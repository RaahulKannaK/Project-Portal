const CACHE_NAME = "coordinator-hub-v1";

/* ✅ Files to cache (basic) */
const urlsToCache = [
  "/",
];

/* ✅ INSTALL */
self.addEventListener("install", (event) => {
  console.log("✅ Service Worker Installing...");

  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log("✅ Caching app shell");
      return cache.addAll(urlsToCache);
    })
  );

  self.skipWaiting(); // 🔥 activate immediately
});

/* ✅ ACTIVATE */
self.addEventListener("activate", (event) => {
  console.log("✅ Service Worker Activated");

  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cache) => {
          if (cache !== CACHE_NAME) {
            console.log("🗑️ Deleting old cache:", cache);
            return caches.delete(cache);
          }
        })
      );
    })
  );

  self.clients.claim(); // 🔥 control pages immediately
});

/* ✅ FETCH (Network First Strategy) */
self.addEventListener("fetch", (event) => {
  event.respondWith(
    fetch(event.request)
      .then((response) => {
        // clone response
        const responseClone = response.clone();

        caches.open(CACHE_NAME).then((cache) => {
          cache.put(event.request, responseClone);
        });

        return response;
      })
      .catch(() => {
        // 🔥 fallback to cache if offline
        return caches.match(event.request);
      })
  );
});