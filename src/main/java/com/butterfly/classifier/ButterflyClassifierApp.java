package com.butterfly.classifier;

import javax.swing.*;
import javax.swing.border.EmptyBorder;
import java.awt.*;
import java.net.ServerSocket;
import java.net.URI;


public class ButterflyClassifierApp extends JFrame {

    private static final String MODEL_PATH = "model/butterfly_species_model.h5";
    private static final int DEFAULT_PORT = 8080;

    private SpeciesModel model;
    private ButterflyWebServer webServer;
    private int serverPort;

    private JLabel statusLabel;
    private JLabel urlLabel;
    private JButton openBrowserBtn;

    public ButterflyClassifierApp() {
        super("ButterflyAI — System Launcher & Control Center");
        initUI();
        initApp();
    }

    private void initUI() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(480, 360);
        setResizable(false);
        setLocationRelativeTo(null);

        // Modern Dark Nature Theme for Control Panel
        Color bgDark = Color.decode("#0F291E");
        Color cardBg = Color.decode("#1B3D2F");
        Color textLight = Color.decode("#ECFDF5");
        Color accentEmerald = Color.decode("#10B981");

        getContentPane().setBackground(bgDark);
        setLayout(new BorderLayout(15, 15));

        // Header Panel
        JPanel headerPanel = new JPanel();
        headerPanel.setOpaque(false);
        headerPanel.setLayout(new BoxLayout(headerPanel, BoxLayout.Y_AXIS));
        headerPanel.setBorder(new EmptyBorder(20, 20, 10, 20));

        JLabel titleLabel = new JLabel("ButterflyAI");
        titleLabel.setFont(new Font("Segoe UI", Font.BOLD, 24));
        titleLabel.setForeground(textLight);
        titleLabel.setAlignmentX(Component.LEFT_ALIGNMENT);

        JLabel subtitleLabel = new JLabel("AI-Powered Butterfly Species Identification System");
        subtitleLabel.setFont(new Font("Segoe UI", Font.PLAIN, 12));
        subtitleLabel.setForeground(Color.decode("#A7F3D0"));
        subtitleLabel.setAlignmentX(Component.LEFT_ALIGNMENT);

        headerPanel.add(titleLabel);
        headerPanel.add(Box.createRigidArea(new Dimension(0, 4)));
        headerPanel.add(subtitleLabel);

        add(headerPanel, BorderLayout.NORTH);

        // Status Card Panel
        JPanel cardPanel = new JPanel();
        cardPanel.setBackground(cardBg);
        cardPanel.setBorder(BorderFactory.createCompoundBorder(
            BorderFactory.createLineBorder(Color.decode("#2D5A47"), 1),
            new EmptyBorder(15, 20, 15, 20)
        ));
        cardPanel.setLayout(new BoxLayout(cardPanel, BoxLayout.Y_AXIS));

        statusLabel = new JLabel("● Initializing AI engine and Web Server...");
        statusLabel.setFont(new Font("Segoe UI", Font.BOLD, 13));
        statusLabel.setForeground(Color.decode("#FCD34D")); // Amber loading
        statusLabel.setAlignmentX(Component.LEFT_ALIGNMENT);

        urlLabel = new JLabel("Web Interface: http://localhost:" + DEFAULT_PORT);
        urlLabel.setFont(new Font("Segoe UI", Font.PLAIN, 12));
        urlLabel.setForeground(textLight);
        urlLabel.setAlignmentX(Component.LEFT_ALIGNMENT);

        JLabel modelInfoLabel = new JLabel("Inference Engine: MobileNetV2 / Fallback Color Evaluator");
        modelInfoLabel.setFont(new Font("Segoe UI", Font.PLAIN, 11));
        modelInfoLabel.setForeground(Color.decode("#9CA3AF"));
        modelInfoLabel.setAlignmentX(Component.LEFT_ALIGNMENT);

        cardPanel.add(statusLabel);
        cardPanel.add(Box.createRigidArea(new Dimension(0, 10)));
        cardPanel.add(urlLabel);
        cardPanel.add(Box.createRigidArea(new Dimension(0, 6)));
        cardPanel.add(modelInfoLabel);

        JPanel centerContainer = new JPanel(new BorderLayout());
        centerContainer.setOpaque(false);
        centerContainer.setBorder(new EmptyBorder(0, 20, 0, 20));
        centerContainer.add(cardPanel, BorderLayout.CENTER);

        add(centerContainer, BorderLayout.CENTER);

        // Bottom Controls
        JPanel bottomPanel = new JPanel(new FlowLayout(FlowLayout.RIGHT, 15, 15));
        bottomPanel.setOpaque(false);

        openBrowserBtn = new JButton("Open ButterflyAI Web App →");
        openBrowserBtn.setFont(new Font("Segoe UI", Font.BOLD, 13));
        openBrowserBtn.setBackground(accentEmerald);
        openBrowserBtn.setForeground(Color.WHITE);
        openBrowserBtn.setFocusPainted(false);
        openBrowserBtn.setCursor(new Cursor(Cursor.HAND_CURSOR));
        openBrowserBtn.setBorder(BorderFactory.createEmptyBorder(10, 20, 10, 20));
        openBrowserBtn.setEnabled(false);
        openBrowserBtn.addActionListener(e -> openBrowser());

        bottomPanel.add(openBrowserBtn);
        add(bottomPanel, BorderLayout.SOUTH);
    }

    private void initApp() {
        SwingWorker<Void, Void> worker = new SwingWorker<>() {
            @Override
            protected Void doInBackground() throws Exception {
                // 1. Initialize AI Species Model Engine
                model = new SpeciesModel(MODEL_PATH);

                // 2. Find available port
                serverPort = findAvailablePort(DEFAULT_PORT);

                // 3. Start Embedded Web Server
                webServer = new ButterflyWebServer(serverPort, model);
                webServer.start();

                return null;
            }

            @Override
            protected void done() {
                try {
                    get(); // Check for exceptions
                    statusLabel.setText("● Server & AI Engine Active");
                    statusLabel.setForeground(Color.decode("#34D399")); // Active emerald green
                    urlLabel.setText("Web Interface: http://localhost:" + serverPort);
                    openBrowserBtn.setEnabled(true);

                    // Automatically open browser window
                    openBrowser();

                } catch (Exception e) {
                    statusLabel.setText("● Error starting application");
                    statusLabel.setForeground(Color.decode("#F87171"));
                    JOptionPane.showMessageDialog(ButterflyClassifierApp.this,
                        "Failed to start ButterflyAI Web Server: " + e.getMessage(),
                        "Startup Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        };
        worker.execute();
    }

    private void openBrowser() {
        try {
            String url = "http://localhost:" + serverPort;
            if (Desktop.isDesktopSupported() && Desktop.getDesktop().isSupported(Desktop.Action.BROWSE)) {
                Desktop.getDesktop().browse(new URI(url));
            } else {
                Runtime.getRuntime().exec("cmd /c start " + url);
            }
        } catch (Exception e) {
            System.err.println("Could not launch default browser automatically: " + e.getMessage());
        }
    }

    private int findAvailablePort(int startingPort) {
        for (int p = startingPort; p < startingPort + 50; p++) {
            try (ServerSocket socket = new ServerSocket(p)) {
                return p;
            } catch (Exception ignored) {
            }
        }
        return startingPort;
    }

    public static void main(String[] args) {
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
