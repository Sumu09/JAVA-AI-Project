package com.butterfly.classifier;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.*;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.util.*;

/**
 * Embedded web server for ButterflyAI interactive frontend.
 * Built using JDK com.sun.net.httpserver.HttpServer (zero external dependencies).
 */
public class ButterflyWebServer {

    private final int port;
    private final SpeciesModel model;
    private HttpServer server;

    public ButterflyWebServer(int port, SpeciesModel model) {
        this.port = port;
        this.model = model;
    }

    public void start() throws IOException {
        server = HttpServer.create(new InetSocketAddress(port), 0);

        server.createContext("/", new StaticHandler());
        server.createContext("/api/species", new SpeciesApiHandler());
        server.createContext("/api/classify", new ClassifyApiHandler());
        server.createContext("/api/sample", new SampleImageHandler());

        server.setExecutor(java.util.concurrent.Executors.newFixedThreadPool(8));
        server.start();
        System.out.println("ButterflyAI Web Server started at http://localhost:" + port);
    }

    public void stop() {
        if (server != null) {
            server.stop(0);
        }
    }

    public int getPort() {
        return port;
    }

    /**
     * Handler for static frontend assets (index.html, styles.css, app.js, images).
     */
    private class StaticHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String path = exchange.getRequestURI().getPath();
            if (path.equals("/")) {
                path = "/index.html";
            }

            byte[] content = loadWebAsset(path);
            if (content == null) {
                String response = "404 Not Found";
                exchange.sendResponseHeaders(404, response.length());
                OutputStream os = exchange.getResponseBody();
                os.write(response.getBytes());
                os.close();
                return;
            }

            String contentType = "text/html; charset=UTF-8";
            if (path.endsWith(".css")) {
                contentType = "text/css; charset=UTF-8";
            } else if (path.endsWith(".js")) {
                contentType = "application/javascript; charset=UTF-8";
            } else if (path.endsWith(".png")) {
                contentType = "image/png";
            } else if (path.endsWith(".jpg") || path.endsWith(".jpeg")) {
                contentType = "image/jpeg";
            } else if (path.endsWith(".svg")) {
                contentType = "image/svg+xml";
            }

            exchange.getResponseHeaders().set("Content-Type", contentType);
            exchange.sendResponseHeaders(200, content.length);
            OutputStream os = exchange.getResponseBody();
            os.write(content);
            os.close();
        }
    }

    private byte[] loadWebAsset(String resourcePath) {
        String cleanPath = resourcePath.startsWith("/") ? resourcePath.substring(1) : resourcePath;
        
        try (InputStream is = getClass().getResourceAsStream("/web/" + cleanPath)) {
            if (is != null) {
                return is.readAllBytes();
            }
        } catch (Exception ignored) {}

        File localFile = new File("src/main/resources/web/" + cleanPath);
        if (localFile.exists()) {
            try {
                return Files.readAllBytes(localFile.toPath());
            } catch (Exception ignored) {}
        }

        File targetFile = new File("target/classes/web/" + cleanPath);
        if (targetFile.exists()) {
            try {
                return Files.readAllBytes(targetFile.toPath());
            } catch (Exception ignored) {}
        }

        return null;
    }

    private class SpeciesApiHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            if (!"GET".equalsIgnoreCase(exchange.getRequestMethod())) {
                exchange.sendResponseHeaders(405, -1);
                return;
            }

            StringBuilder json = new StringBuilder("[");
            Species[] speciesArray = Species.values();
            for (int i = 0; i < speciesArray.length; i++) {
                Species s = speciesArray[i];
                SpeciesInfo.Details d = SpeciesInfo.getDetails(s);
                if (i > 0) json.append(",");

                json.append("{")
                    .append("\"id\":\"").append(escapeJson(s.getId())).append("\",")
                    .append("\"commonName\":\"").append(escapeJson(s.getCommonName())).append("\",")
                    .append("\"scientificName\":\"").append(escapeJson(s.getScientificName())).append("\",")
                    .append("\"family\":\"").append(escapeJson(d != null ? d.family : "")).append("\",")
                    .append("\"genus\":\"").append(escapeJson(d != null ? d.genus : "")).append("\",")
                    .append("\"speciesName\":\"").append(escapeJson(d != null ? d.speciesName : "")).append("\",")
                    .append("\"kingdom\":\"").append(escapeJson(d != null ? d.kingdom : "Animalia")).append("\",")
                    .append("\"phylum\":\"").append(escapeJson(d != null ? d.phylum : "Arthropoda")).append("\",")
                    .append("\"className\":\"").append(escapeJson(d != null ? d.className : "Insecta")).append("\",")
                    .append("\"order\":\"").append(escapeJson(d != null ? d.order : "Lepidoptera")).append("\",")
                    .append("\"habitat\":\"").append(escapeJson(d != null ? d.habitat : "")).append("\",")
                    .append("\"distribution\":\"").append(escapeJson(d != null ? d.distribution : "")).append("\",")
                    .append("\"description\":\"").append(escapeJson(d != null ? d.description : "")).append("\",")
                    .append("\"sampleImagePath\":\"").append(escapeJson(d != null ? d.sampleImagePath : "")).append("\"")
                    .append("}");
            }
            json.append("]");

            byte[] responseBytes = json.toString().getBytes(StandardCharsets.UTF_8);
            exchange.getResponseHeaders().set("Content-Type", "application/json; charset=UTF-8");
            exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
            exchange.sendResponseHeaders(200, responseBytes.length);
            OutputStream os = exchange.getResponseBody();
            os.write(responseBytes);
            os.close();
        }
    }

    private class SampleImageHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String query = exchange.getRequestURI().getQuery();
            String path = null;
            if (query != null && query.contains("path=")) {
                path = query.split("path=")[1];
            }

            if (path == null || path.trim().isEmpty()) {
                exchange.sendResponseHeaders(400, -1);
                return;
            }

            File file = new File(path);
            if (!file.exists() || !file.isFile()) {
                exchange.sendResponseHeaders(404, -1);
                return;
            }

            byte[] bytes = Files.readAllBytes(file.toPath());
            String mime = (path.toLowerCase().endsWith(".jpg") || path.toLowerCase().endsWith(".jpeg")) ? "image/jpeg" : "image/png";
            exchange.getResponseHeaders().set("Content-Type", mime);
            exchange.sendResponseHeaders(200, bytes.length);
            OutputStream os = exchange.getResponseBody();
            os.write(bytes);
            os.close();
        }
    }

    private class ClassifyApiHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            if (!"POST".equalsIgnoreCase(exchange.getRequestMethod())) {
                exchange.sendResponseHeaders(405, -1);
                return;
            }

            try {
                InputStream is = exchange.getRequestBody();
                byte[] bodyBytes = is.readAllBytes();

                if (bodyBytes.length == 0) {
                    sendError(exchange, 400, "Empty payload received. Please upload an image file.");
                    return;
                }

                String filenameHeader = exchange.getRequestHeaders().getFirst("X-File-Name");
                String filename = (filenameHeader != null && !filenameHeader.isEmpty()) ? filenameHeader : "uploaded_image.png";

                byte[] imageBytes = extractImageBytes(bodyBytes, exchange.getRequestHeaders().getFirst("Content-Type"));

                ByteArrayInputStream bais = new ByteArrayInputStream(imageBytes);
                BufferedImage image = ImageIO.read(bais);

                if (image == null) {
                    sendError(exchange, 400, "Unsupported or corrupt image format. Please upload a valid JPG, PNG, or WEBP image.");
                    return;
                }

                // Preserve uploaded filename and extension
                String cleanName = filename.replaceAll("[^a-zA-Z0-9._-]", "_");
                if (!cleanName.toLowerCase().endsWith(".png") && !cleanName.toLowerCase().endsWith(".jpg") && !cleanName.toLowerCase().endsWith(".jpeg")) {
                    cleanName += ".png";
                }

                File tempFile = File.createTempFile("bfly_", "_" + cleanName);
                tempFile.deleteOnExit();
                try (FileOutputStream fos = new FileOutputStream(tempFile)) {
                    fos.write(imageBytes);
                }

                List<SpeciesModel.PredictionResult> results = model.predict(tempFile, image);
                tempFile.delete();

                if (results == null || results.isEmpty()) {
                    sendError(exchange, 500, "Could not compute species predictions.");
                    return;
                }

                SpeciesModel.PredictionResult top1 = results.get(0);
                SpeciesInfo.Details topDetails = SpeciesInfo.getDetails(top1.species);

                StringBuilder json = new StringBuilder("{");
                json.append("\"success\":true,");
                json.append("\"imageDimensions\":{\"width\":").append(image.getWidth()).append(",\"height\":").append(image.getHeight()).append("},");
                json.append("\"primary\":{")
                    .append("\"id\":\"").append(escapeJson(top1.species.getId())).append("\",")
                    .append("\"commonName\":\"").append(escapeJson(top1.species.getCommonName())).append("\",")
                    .append("\"scientificName\":\"").append(escapeJson(top1.species.getScientificName())).append("\",")
                    .append("\"confidence\":").append(String.format(Locale.US, "%.1f", top1.confidencePercentage)).append(",")
                    .append("\"family\":\"").append(escapeJson(topDetails != null ? topDetails.family : "")).append("\",")
                    .append("\"genus\":\"").append(escapeJson(topDetails != null ? topDetails.genus : "")).append("\",")
                    .append("\"speciesName\":\"").append(escapeJson(topDetails != null ? topDetails.speciesName : "")).append("\",")
                    .append("\"kingdom\":\"").append(escapeJson(topDetails != null ? topDetails.kingdom : "Animalia")).append("\",")
                    .append("\"phylum\":\"").append(escapeJson(topDetails != null ? topDetails.phylum : "Arthropoda")).append("\",")
                    .append("\"className\":\"").append(escapeJson(topDetails != null ? topDetails.className : "Insecta")).append("\",")
                    .append("\"order\":\"").append(escapeJson(topDetails != null ? topDetails.order : "Lepidoptera")).append("\",")
                    .append("\"habitat\":\"").append(escapeJson(topDetails != null ? topDetails.habitat : "")).append("\",")
                    .append("\"distribution\":\"").append(escapeJson(topDetails != null ? topDetails.distribution : "")).append("\",")
                    .append("\"description\":\"").append(escapeJson(topDetails != null ? topDetails.description : "")).append("\"")
                    .append("},");

                json.append("\"predictions\":[");
                for (int i = 0; i < Math.min(5, results.size()); i++) {
                    SpeciesModel.PredictionResult r = results.get(i);
                    SpeciesInfo.Details d = SpeciesInfo.getDetails(r.species);
                    if (i > 0) json.append(",");
                    json.append("{")
                        .append("\"rank\":").append(i + 1).append(",")
                        .append("\"commonName\":\"").append(escapeJson(r.species.getCommonName())).append("\",")
                        .append("\"scientificName\":\"").append(escapeJson(r.species.getScientificName())).append("\",")
                        .append("\"family\":\"").append(escapeJson(d != null ? d.family : "")).append("\",")
                        .append("\"confidence\":").append(String.format(Locale.US, "%.1f", r.confidencePercentage))
                        .append("}");
                }
                json.append("]}");

                byte[] resBytes = json.toString().getBytes(StandardCharsets.UTF_8);
                exchange.getResponseHeaders().set("Content-Type", "application/json; charset=UTF-8");
                exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
                exchange.sendResponseHeaders(200, resBytes.length);
                OutputStream os = exchange.getResponseBody();
                os.write(resBytes);
                os.close();

            } catch (Exception e) {
                e.printStackTrace();
                sendError(exchange, 500, "An internal server error occurred while processing the image: " + e.getMessage());
            }
        }

        private byte[] extractImageBytes(byte[] body, String contentType) {
            if (contentType != null && contentType.contains("multipart/form-data")) {
                int boundaryIndex = contentType.indexOf("boundary=");
                if (boundaryIndex != -1) {
                    String boundary = contentType.substring(boundaryIndex + 9);
                    if (boundary.startsWith("\"") && boundary.endsWith("\"")) {
                        boundary = boundary.substring(1, boundary.length() - 1);
                    }
                    byte[] boundaryBytes = ("--" + boundary).getBytes(StandardCharsets.UTF_8);

                    int start = -1;
                    for (int i = 0; i < body.length - 4; i++) {
                        if (body[i] == '\r' && body[i+1] == '\n' && body[i+2] == '\r' && body[i+3] == '\n') {
                            start = i + 4;
                            break;
                        }
                    }
                    if (start != -1) {
                        int end = body.length;
                        for (int i = start; i < body.length - boundaryBytes.length; i++) {
                            boolean match = true;
                            for (int j = 0; j < boundaryBytes.length; j++) {
                                if (body[i + j] != boundaryBytes[j]) {
                                    match = false;
                                    break;
                                }
                            }
                            if (match) {
                                end = i - 2;
                                break;
                            }
                        }
                        if (end > start) {
                            return Arrays.copyOfRange(body, start, end);
                        }
                    }
                }
            }
            return body;
        }

        private void sendError(HttpExchange exchange, int code, String message) throws IOException {
            String json = "{\"success\":false,\"error\":\"" + escapeJson(message) + "\"}";
            byte[] bytes = json.getBytes(StandardCharsets.UTF_8);
            exchange.getResponseHeaders().set("Content-Type", "application/json; charset=UTF-8");
            exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
            exchange.sendResponseHeaders(code, bytes.length);
            OutputStream os = exchange.getResponseBody();
            os.write(bytes);
            os.close();
        }
    }

    private static String escapeJson(String input) {
        if (input == null) return "";
        return input.replace("\\", "\\\\")
                    .replace("\"", "\\\"")
                    .replace("\b", "\\b")
                    .replace("\f", "\\f")
                    .replace("\n", "\\n")
                    .replace("\r", "\\r")
                    .replace("\t", "\\t");
    }
}
