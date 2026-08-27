package com.butterfly.classifier;

import javax.swing.*;
import javax.swing.border.EmptyBorder;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.awt.*;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.util.List;
import javax.imageio.ImageIO;

/**
 * Swing GUI application for the Butterfly Species Classifier.
 */
public class ButterflyClassifierApp extends JFrame {

    // Theme Colors (matching app.py design)
    private static final Color BG_COLOR = Color.decode("#F0F4F8");
    private static final Color HEADER_BG = Color.decode("#0D1B2A");
    private static final Color PRIMARY_COLOR = Color.decode("#00A896");
    private static final Color PREVIEW_BG = Color.decode("#E2E8F0");

    private static final String MODEL_PATH = "model/butterfly_species_model.h5";

    private SpeciesModel model;
    private PreviewPanel previewPanel;
    private JButton browseBtn;
    private JLabel commonNameLabel;
    private JLabel sciNameLabel;
    private JLabel confidenceLabel;
    private JTextArea top3TextArea;

    public ButterflyClassifierApp() {
        super("Butterfly Species Classifier");
        initUI();
        loadModelAsync();
    }

    private void initUI() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(440, 640);
        setResizable(false);
        setLocationRelativeTo(null); // Center on screen
        getContentPane().setBackground(BG_COLOR);
        setLayout(new BorderLayout());

        // 1. Header Bar
        JPanel headerPanel = new JPanel(new GridBagLayout());
        headerPanel.setBackground(HEADER_BG);
        headerPanel.setPreferredSize(new Dimension(440, 60));

        JLabel titleLabel = new JLabel("Butterfly Species Classifier");
        titleLabel.setForeground(Color.WHITE);
        titleLabel.setFont(new Font("Helvetica", Font.BOLD, 16));
        headerPanel.add(titleLabel);

        add(headerPanel, BorderLayout.NORTH);

        // 2. Central Content Panel
        JPanel contentPanel = new JPanel();
        contentPanel.setLayout(new BoxLayout(contentPanel, BoxLayout.Y_AXIS));
        contentPanel.setBackground(BG_COLOR);
        contentPanel.setBorder(new EmptyBorder(15, 20, 10, 20));

        // Preview Area (300x300)
        previewPanel = new PreviewPanel();
        previewPanel.setAlignmentX(Component.CENTER_ALIGNMENT);
        contentPanel.add(previewPanel);
        contentPanel.add(Box.createRigidArea(new Dimension(0, 15)));

        // Browse Button
        browseBtn = new JButton("Browse Image");
        browseBtn.setAlignmentX(Component.CENTER_ALIGNMENT);
        browseBtn.setFont(new Font("Helvetica", Font.BOLD, 13));
        browseBtn.setBackground(PRIMARY_COLOR);
        browseBtn.setForeground(Color.WHITE);
        browseBtn.setFocusPainted(false);
        browseBtn.setCursor(new Cursor(Cursor.HAND_CURSOR));
        browseBtn.setBorder(BorderFactory.createEmptyBorder(10, 25, 10, 25));
        browseBtn.addActionListener(e -> browseImage());
        contentPanel.add(browseBtn);
        contentPanel.add(Box.createRigidArea(new Dimension(0, 15)));

        // Result Panel
        JPanel resultPanel = new JPanel();
        resultPanel.setLayout(new BoxLayout(resultPanel, BoxLayout.Y_AXIS));
        resultPanel.setBackground(BG_COLOR);
        resultPanel.setAlignmentX(Component.CENTER_ALIGNMENT);

        commonNameLabel = new JLabel("", SwingConstants.CENTER);
        commonNameLabel.setFont(new Font("Helvetica", Font.BOLD, 20));
        commonNameLabel.setForeground(PRIMARY_COLOR);
        commonNameLabel.setAlignmentX(Component.CENTER_ALIGNMENT);

        sciNameLabel = new JLabel("", SwingConstants.CENTER);
        sciNameLabel.setFont(new Font("Helvetica", Font.ITALIC, 13));
        sciNameLabel.setForeground(Color.decode("#4A5568"));
        sciNameLabel.setAlignmentX(Component.CENTER_ALIGNMENT);

        confidenceLabel = new JLabel("", SwingConstants.CENTER);
        confidenceLabel.setFont(new Font("Helvetica", Font.PLAIN, 12));
        confidenceLabel.setForeground(Color.decode("#2D3748"));
        confidenceLabel.setAlignmentX(Component.CENTER_ALIGNMENT);

        top3TextArea = new JTextArea();
        top3TextArea.setEditable(false);
        top3TextArea.setFocusable(false);
        top3TextArea.setBackground(BG_COLOR);
        top3TextArea.setForeground(Color.decode("#718096"));
        top3TextArea.setFont(new Font("Helvetica", Font.PLAIN, 11));
        top3TextArea.setAlignmentX(Component.CENTER_ALIGNMENT);

        resultPanel.add(commonNameLabel);
        resultPanel.add(Box.createRigidArea(new Dimension(0, 3)));
        resultPanel.add(sciNameLabel);
        resultPanel.add(Box.createRigidArea(new Dimension(0, 5)));
        resultPanel.add(confidenceLabel);
        resultPanel.add(Box.createRigidArea(new Dimension(0, 8)));
        resultPanel.add(top3TextArea);

        contentPanel.add(resultPanel);
        add(contentPanel, BorderLayout.CENTER);

        // 3. Footer Bar
        JLabel footerLabel = new JLabel("Leeds Butterfly Dataset — MobileNetV2 Transfer Learning", SwingConstants.CENTER);
        footerLabel.setFont(new Font("Helvetica", Font.PLAIN, 10));
        footerLabel.setForeground(Color.decode("#A0AEC0"));
        footerLabel.setBorder(new EmptyBorder(5, 0, 10, 0));
        add(footerLabel, BorderLayout.SOUTH);
    }

    private void loadModelAsync() {
        SwingWorker<SpeciesModel, Void> worker = new SwingWorker<>() {
            @Override
            protected SpeciesModel doInBackground() {
                return new SpeciesModel(MODEL_PATH);
            }

            @Override
            protected void done() {
                try {
                    model = get();
                    System.out.println("Model engine initialized.");
                } catch (Exception e) {
                    System.err.println("Error initializing model: " + e.getMessage());
                }
            }
        };
        worker.execute();
    }

    private void browseImage() {
        JFileChooser chooser = new JFileChooser();
        chooser.setDialogTitle("Select an Image");
        chooser.setFileFilter(new FileNameExtensionFilter("Image Files (*.jpg, *.jpeg, *.png)", "jpg", "jpeg", "png"));

        int choice = chooser.showOpenDialog(this);
        if (choice == JFileChooser.APPROVE_OPTION) {
            File selectedFile = chooser.getSelectedFile();
            processImage(selectedFile);
        }
    }

    private void processImage(File file) {
        try {
            BufferedImage originalImage = ImageIO.read(file);
            if (originalImage == null) {
                JOptionPane.showMessageDialog(this, "Failed to load image file.", "Image Error", JOptionPane.ERROR_MESSAGE);
                return;
            }

            previewPanel.setImage(originalImage);

            // Update UI to identifying status
            commonNameLabel.setText("Identifying...");
            commonNameLabel.setForeground(Color.decode("#718096"));
            sciNameLabel.setText("");
            confidenceLabel.setText("");
            top3TextArea.setText("");

            // Process prediction asynchronously
            SwingWorker<List<SpeciesModel.PredictionResult>, Void> worker = new SwingWorker<>() {
                @Override
                protected List<SpeciesModel.PredictionResult> doInBackground() {
                    if (model == null) {
                        model = new SpeciesModel(MODEL_PATH);
                    }
                    return model.predict(file, originalImage);
                }

                @Override
                protected void done() {
                    try {
                        List<SpeciesModel.PredictionResult> results = get();
                        updateResults(results);
                    } catch (Exception e) {
                        commonNameLabel.setText("Error");
                        JOptionPane.showMessageDialog(ButterflyClassifierApp.this,
                                "Failed to predict image: " + e.getMessage(), "Prediction Error", JOptionPane.ERROR_MESSAGE);
                    }
                }
            };
            worker.execute();

        } catch (Exception e) {
            JOptionPane.showMessageDialog(this, "Error reading image: " + e.getMessage(), "File Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void updateResults(List<SpeciesModel.PredictionResult> results) {
        if (results == null || results.isEmpty()) return;

        SpeciesModel.PredictionResult top1 = results.get(0);
        commonNameLabel.setText(top1.species.getCommonName());
        commonNameLabel.setForeground(PRIMARY_COLOR);
        sciNameLabel.setText(top1.species.getScientificName());
        confidenceLabel.setText(String.format("Confidence: %.1f%%", top1.confidencePercentage));

        StringBuilder sb = new StringBuilder("Top 3 Predictions:\n");
        for (int i = 0; i < Math.min(3, results.size()); i++) {
            SpeciesModel.PredictionResult res = results.get(i);
            sb.append(String.format("%d. %s (%.1f%%)\n", i + 1, res.species.getCommonName(), res.confidencePercentage));
        }
        top3TextArea.setText(sb.toString().trim());
    }

    // Custom 300x300 Preview Panel
    private static class PreviewPanel extends JPanel {
        private BufferedImage image;

        public PreviewPanel() {
            setPreferredSize(new Dimension(300, 300));
            setMaximumSize(new Dimension(300, 300));
            setMinimumSize(new Dimension(300, 300));
            setBackground(PREVIEW_BG);
        }

        public void setImage(BufferedImage img) {
            this.image = img;
            repaint();
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            Graphics2D g2d = (Graphics2D) g.create();
            g2d.setRenderingHint(RenderingHints.KEY_INTERPOLATION, RenderingHints.VALUE_INTERPOLATION_BILINEAR);
            g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

            if (image == null) {
                g2d.setColor(Color.decode("#718096"));
                g2d.setFont(new Font("Helvetica", Font.PLAIN, 13));
                FontMetrics fm = g2d.getFontMetrics();
                String text = "No Image Selected";
                int textX = (getWidth() - fm.stringWidth(text)) / 2;
                int textY = (getHeight() + fm.getAscent()) / 2 - 2;
                g2d.drawString(text, textX, textY);
            } else {
                // Scale image preserving aspect ratio within 300x300
                int imgW = image.getWidth();
                int imgH = image.getHeight();

                double scale = Math.min(300.0 / imgW, 300.0 / imgH);
                int targetW = (int) (imgW * scale);
                int targetH = (int) (imgH * scale);

                int x = (300 - targetW) / 2;
                int y = (300 - targetH) / 2;

                g2d.drawImage(image, x, y, targetW, targetH, null);
            }
            g2d.dispose();
        }
    }

    public static void main(String[] args) {
        // Set System Look & Feel for Windows native styling
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception ignored) {
        }

        SwingUtilities.invokeLater(() -> {
            ButterflyClassifierApp app = new ButterflyClassifierApp();
            app.setVisible(true);
        });
    }
}
