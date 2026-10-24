package com.butterfly.classifier;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.util.*;

// Organizes the raw images in the 'images/' folder into an 80/20 train/test split
// under 'dataset/train' and 'dataset/test'.

public class DatasetPreparer {

    private static final String IMAGES_DIR = "images";
    private static final String DATASET_DIR = "dataset";
    private static final double TEST_RATIO = 0.20; // 20% test, 80% train

    public static void main(String[] args) {
        prepareDataset();
    }

    public static void prepareDataset() {
        File datasetFolder = new File(DATASET_DIR);
        if (datasetFolder.exists()) {
            System.out.println("Dataset directory '" + DATASET_DIR + "' already exists. Skipping reorganization.");
            return;
        }

        File imagesFolder = new File(IMAGES_DIR);
        if (!imagesFolder.exists() || !imagesFolder.isDirectory()) {
            System.err.println("Error: Directory '" + IMAGES_DIR + "' not found.");
            return;
        }

        File[] imageFiles = imagesFolder.listFiles((dir, name) -> {
            String lowercase = name.toLowerCase();
            return lowercase.endsWith(".png") || lowercase.endsWith(".jpg") || lowercase.endsWith(".jpeg");
        });

        if (imageFiles == null || imageFiles.length == 0) {
            System.out.println("No image files found in '" + IMAGES_DIR + "'.");
            return;
        }

        System.out.println("Found " + imageFiles.length + " images. Grouping by species class ID...");

        // Group images by 3-digit class prefix (e.g. 001, 002)
        Map<String, List<File>> classMap = new HashMap<>();
        for (File img : imageFiles) {
            String filename = img.getName();
            if (filename.length() >= 3) {
                String classId = filename.substring(0, 3);
                classMap.computeIfAbsent(classId, k -> new ArrayList<>()).add(img);
            }
        }

        Random random = new Random(42); // Fixed seed for reproducible split
        int totalTrain = 0;
        int totalTest = 0;

        for (Map.Entry<String, List<File>> entry : classMap.entrySet()) {
            String classId = entry.getKey();
            List<File> files = entry.getValue();
            Collections.shuffle(files, random);

            int testSize = (int) Math.round(files.size() * TEST_RATIO);
            List<File> testFiles = files.subList(0, testSize);
            List<File> trainFiles = files.subList(testSize, files.size());

            Species species = Species.getById(classId);
            String speciesFolderName;
            if (species != null) {
                speciesFolderName = classId + "_" + sanitizeFolderName(species.getScientificName() + "_" + species.getCommonName());
            } else {
                speciesFolderName = classId + "_Unknown";
            }

            copyFiles(trainFiles, "train", speciesFolderName);
            copyFiles(testFiles, "test", speciesFolderName);

            totalTrain += trainFiles.size();
            totalTest += testFiles.size();
        }

        System.out.println("Dataset reorganization complete!");
        System.out.println("Training images: " + totalTrain);
        System.out.println("Testing images: " + totalTest);
    }

    private static void copyFiles(List<File> files, String split, String folderName) {
        Path destDir = Path.of(DATASET_DIR, split, folderName);
        try {
            Files.createDirectories(destDir);
            for (File file : files) {
                Path target = destDir.resolve(file.getName());
                Files.copy(file.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
            }
        } catch (IOException e) {
            System.err.println("Error copying files for split " + split + ": " + e.getMessage());
        }
    }

    private static String sanitizeFolderName(String name) {
        return name.replace(' ', '_').replaceAll("[^a-zA-Z0-9_]", "");
    }
}
