/**
 * ButterflyAI — Assam Cultural & Ecological UX Logic
 * Celebrating Rare Lepidoptera of Assam and Northeast India
 */

document.addEventListener('DOMContentLoaded', () => {
    let selectedFile = null;
    let allSpeciesData = [];
    let currentFamilyFilter = 'ALL';
    let searchQuery = '';

    // --- DOM Elements ---
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');
    const uploadPrompt = document.getElementById('uploadPrompt');
    const previewContainer = document.getElementById('previewContainer');
    const imagePreview = document.getElementById('imagePreview');
    const fileNameText = document.getElementById('fileNameText');
    const fileDimsText = document.getElementById('fileDimsText');
    const replaceFileBtn = document.getElementById('replaceFileBtn');
    const removeFileBtn = document.getElementById('removeFileBtn');
    const identifyBtn = document.getElementById('identifyBtn');
    const pasteBtn = document.getElementById('pasteBtn');
    const scannerOverlay = document.getElementById('scannerOverlay');
    const scannerStatusText = document.getElementById('scannerStatusText');

    const emptyState = document.getElementById('emptyState');
    const errorCard = document.getElementById('errorCard');
    const errorTitle = document.getElementById('errorTitle');
    const errorDesc = document.getElementById('errorDesc');
    const errorDismissBtn = document.getElementById('errorDismissBtn');
    const resultCard = document.getElementById('resultCard');

    // Result Card Elements
    const resCommonName = document.getElementById('resCommonName');
    const resSciName = document.getElementById('resSciName');
    const resConfidenceText = document.getElementById('resConfidenceText');
    const resConfidenceBar = document.getElementById('resConfidenceBar');
    const resFamily = document.getElementById('resFamily');
    const resHabitat = document.getElementById('resHabitat');
    const resDescription = document.getElementById('resDescription');
    const predictionsList = document.getElementById('predictionsList');

    // Taxonomy Grid Elements
    const taxKingdom = document.getElementById('taxKingdom');
    const taxPhylum = document.getElementById('taxPhylum');
    const taxClass = document.getElementById('taxClass');
    const taxOrder = document.getElementById('taxOrder');
    const taxFamily = document.getElementById('taxFamily');
    const taxGenus = document.getElementById('taxGenus');
    const taxSpecies = document.getElementById('taxSpecies');

    const speciesCatalogGrid = document.getElementById('speciesCatalogGrid');
    const catalogSearchInput = document.getElementById('catalogSearchInput');
    const familyPills = document.querySelectorAll('.family-pill');

    // --- 1. Navigation Handling ---
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('.section');

    function switchSection(targetId) {
        navLinks.forEach(link => {
            if (link.dataset.target === targetId) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });

        sections.forEach(sec => {
            if (sec.id === targetId) {
                sec.classList.add('active-section');
                sec.scrollIntoView({ behavior: 'smooth' });
            } else {
                sec.classList.remove('active-section');
            }
        });
    }

    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            switchSection(link.dataset.target);
        });
    });

    document.querySelectorAll('#heroCta, #navCta').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            switchSection('identify');
        });
    });

    document.querySelectorAll('#catalogCta').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            switchSection('species');
        });
    });

    // --- 2. File Upload, Drag-and-Drop & Clipboard Paste ---
    uploadPrompt.addEventListener('click', (e) => {
        if (e.target.closest('#pasteBtn')) return;
        fileInput.click();
    });
    replaceFileBtn.addEventListener('click', () => fileInput.click());

    fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
            handleFileSelect(e.target.files[0]);
        }
    });

    ['dragenter', 'dragover'].forEach(eventName => {
        dropZone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropZone.classList.add('drag-over');
        }, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropZone.classList.remove('drag-over');
        }, false);
    });

    dropZone.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        if (dt.files && dt.files[0]) {
            handleFileSelect(dt.files[0]);
        }
    });

    removeFileBtn.addEventListener('click', clearSelectedFile);

    // Clipboard Paste Button Click Handler
    if (pasteBtn) {
        pasteBtn.addEventListener('click', async (e) => {
            e.stopPropagation();
            try {
                if (navigator.clipboard && navigator.clipboard.read) {
                    const clipboardItems = await navigator.clipboard.read();
                    let foundImage = false;
                    for (const item of clipboardItems) {
                        for (const type of item.types) {
                            if (type.startsWith('image/')) {
                                const blob = await item.getType(type);
                                const file = new File([blob], `pasted_specimen_${Date.now()}.png`, { type });
                                handleFileSelect(file);
                                foundImage = true;
                                break;
                            }
                        }
                        if (foundImage) break;
                    }
                    if (!foundImage) {
                        alert("No image data found in clipboard. Copy an image to your clipboard first, or press Ctrl+V / Cmd+V!");
                    }
                } else {
                    alert("Press Ctrl+V (or Cmd+V on Mac) to paste an image directly from your clipboard!");
                }
            } catch (err) {
                alert("Please press Ctrl+V or Cmd+V to paste your copied butterfly image.");
            }
        });
    }

    // Global Window Paste Event Listener
    window.addEventListener('paste', (e) => {
        const clipboardData = e.clipboardData;
        if (!clipboardData) return;

        // Check files in clipboard
        if (clipboardData.files && clipboardData.files.length > 0) {
            for (let i = 0; i < clipboardData.files.length; i++) {
                const file = clipboardData.files[i];
                if (file.type.startsWith('image/')) {
                    switchSection('identify');
                    handleFileSelect(file);
                    return;
                }
            }
        }

        // Check items in clipboard
        if (clipboardData.items && clipboardData.items.length > 0) {
            for (let i = 0; i < clipboardData.items.length; i++) {
                const item = clipboardData.items[i];
                if (item.kind === 'file' && item.type.startsWith('image/')) {
                    const file = item.getAsFile();
                    if (file) {
                        switchSection('identify');
                        handleFileSelect(file);
                        return;
                    }
                }
            }
        }
    });

    function handleFileSelect(file) {
        if (!file.type.match('image.*')) {
            showError("Invalid File Format", "Please select or paste a valid image file (JPG, PNG, or WEBP).");
            return;
        }

        selectedFile = file;
        fileNameText.textContent = file.name || "pasted_specimen.jpg";

        const reader = new FileReader();
        reader.onload = (e) => {
            const imgUrl = e.target.result;
            imagePreview.src = imgUrl;

            const img = new Image();
            img.onload = () => {
                const sizeMb = (file.size / (1024 * 1024)).toFixed(1);
                fileDimsText.textContent = `${img.width} × ${img.height} px • ${sizeMb} MB`;
            };
            img.src = imgUrl;

            uploadPrompt.classList.add('hidden');
            previewContainer.classList.remove('hidden');
            hideError();
        };
        reader.readAsDataURL(file);
    }

    function clearSelectedFile() {
        selectedFile = null;
        fileInput.value = '';
        imagePreview.src = '';
        uploadPrompt.classList.remove('hidden');
        previewContainer.classList.add('hidden');
        showEmptyState();
    }

    // Sample Thumbnail Chips for Assam Species
    document.querySelectorAll('.sample-chip-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const path = btn.dataset.img;
            const name = btn.querySelector('span') ? btn.querySelector('span').textContent : 'sample';
            fetchSampleImage(path, name);
        });
    });

    function fetchSampleImage(path, name) {
        const sampleUrl = `/api/sample?path=${encodeURIComponent(path)}`;
        fetch(sampleUrl)
            .then(res => {
                if (!res.ok) throw new Error("Could not load sample");
                return res.blob();
            })
            .then(blob => {
                const ext = path.toLowerCase().endsWith('.jpg') ? 'jpg' : 'png';
                const file = new File([blob], `${name.toLowerCase().replace(/[^a-z0-9]+/g, '_')}.${ext}`, { type: `image/${ext}` });
                handleFileSelect(file);
            })
            .catch(() => {
                showError("Sample Load Failed", "Could not load sample field photograph from the dataset.");
            });
    }

    // --- 3. AI Classification Scanner ---
    identifyBtn.addEventListener('click', runClassification);

    function runClassification() {
        if (!selectedFile) return;

        scannerOverlay.classList.remove('hidden');
        
        scannerStatusText.textContent = "Analyzing wing patterns...";
        setTimeout(() => {
            scannerStatusText.textContent = "Extracting ventral & dorsal features...";
        }, 350);
        setTimeout(() => {
            scannerStatusText.textContent = "Matching Assam Lepidoptera taxonomy...";
        }, 700);

        const formData = new FormData();
        formData.append("image", selectedFile, selectedFile.name || "specimen.jpg");

        fetch('/api/classify', {
            method: 'POST',
            headers: {
                'X-File-Name': selectedFile.name || "specimen.jpg"
            },
            body: formData
        })
        .then(res => {
            if (!res.ok) throw new Error("Classification request failed");
            return res.json();
        })
        .then(data => {
            setTimeout(() => {
                scannerOverlay.classList.add('hidden');
                if (data.success) {
                    renderResults(data);
                } else {
                    showError("Prediction Error", data.error || "Model could not classify species.");
                }
            }, 850);
        })
        .catch(() => {
            scannerOverlay.classList.add('hidden');
            showError("Connection Error", "Failed to connect to ButterflyAI inference engine.");
        });
    }

    // --- 4. Render Prediction Results ---
    function renderResults(data) {
        emptyState.classList.add('hidden');
        errorCard.classList.add('hidden');
        resultCard.classList.remove('hidden');

        const primary = data.primary;

        resCommonName.textContent = primary.commonName;
        resSciName.textContent = primary.scientificName;
        resFamily.textContent = primary.family || 'Nymphalidae';
        resHabitat.textContent = primary.habitat || 'Tropical rainforests & hill tracts of Assam';
        resDescription.textContent = primary.description || 'Rare Lepidoptera species identified by MobileNetV2 neural vision pipeline.';

        animateConfidenceCount(primary.confidence);

        taxKingdom.textContent = primary.kingdom || 'Animalia';
        taxPhylum.textContent = primary.phylum || 'Arthropoda';
        taxClass.textContent = primary.className || 'Insecta';
        taxOrder.textContent = primary.order || 'Lepidoptera';
        taxFamily.textContent = primary.family || 'Nymphalidae';
        taxGenus.textContent = primary.genus || primary.scientificName.split(' ')[0] || 'Euthalia';
        taxSpecies.textContent = primary.speciesName || primary.scientificName || 'E. zubeengargi';

        predictionsList.innerHTML = '';
        if (data.predictions) {
            data.predictions.forEach(pred => {
                const row = document.createElement('div');
                row.className = 'pred-row';
                row.innerHTML = `
                    <div class="pred-name-group">
                        <span class="pred-rank">${pred.rank}.</span>
                        <span class="pred-common">${pred.commonName}</span>
                        <span class="pred-sci">(${pred.scientificName})</span>
                    </div>
                    <div class="pred-bar-wrap">
                        <div class="pred-mini-bar">
                            <div class="pred-mini-fill" style="width: ${pred.confidence}%"></div>
                        </div>
                        <span class="pred-pct">${pred.confidence}%</span>
                    </div>
                `;
                predictionsList.appendChild(row);
            });
        }
    }

    function animateConfidenceCount(targetConfidence) {
        const duration = 800;
        const startTime = performance.now();

        resConfidenceBar.style.width = '0%';

        function updateCount(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const easeProgress = 1 - Math.pow(1 - progress, 3);
            const current = easeProgress * targetConfidence;

            resConfidenceText.textContent = `${current.toFixed(1)}%`;
            resConfidenceBar.style.width = `${current.toFixed(1)}%`;

            if (progress < 1) {
                requestAnimationFrame(updateCount);
            } else {
                resConfidenceText.textContent = `${targetConfidence.toFixed(1)}%`;
                resConfidenceBar.style.width = `${targetConfidence.toFixed(1)}%`;
            }
        }

        requestAnimationFrame(updateCount);
    }

    // --- 5. Species Catalog Loading & Filtering (Assam & NE Fauna) ---
    function loadSpeciesCatalog() {
        fetch('/api/species')
            .then(res => res.json())
            .then(data => {
                // Filter out baseline North American species (IDs 001 through 010)
                // Keep only Assam and Northeast India regional species (IDs 011 through 125)
                allSpeciesData = data.filter(sp => {
                    const idNum = parseInt(sp.id, 10);
                    return idNum > 10;
                });
                applyCatalogFilters();
            })
            .catch(err => {
                console.error("Error fetching species catalog:", err);
            });
    }

    function applyCatalogFilters() {
        let filtered = allSpeciesData;

        // Family filter
        if (currentFamilyFilter !== 'ALL') {
            filtered = filtered.filter(sp => (sp.family || '').toUpperCase() === currentFamilyFilter);
        }

        // Search query filter
        if (searchQuery.trim()) {
            const q = searchQuery.toLowerCase().trim();
            filtered = filtered.filter(sp => 
                (sp.commonName || '').toLowerCase().includes(q) ||
                (sp.scientificName || '').toLowerCase().includes(q) ||
                (sp.family || '').toLowerCase().includes(q) ||
                (sp.habitat || '').toLowerCase().includes(q) ||
                (sp.description || '').toLowerCase().includes(q)
            );
        }

        renderSpeciesCatalog(filtered);
    }

    function renderSpeciesCatalog(items) {
        speciesCatalogGrid.innerHTML = '';

        if (items.length === 0) {
            speciesCatalogGrid.innerHTML = `
                <div style="grid-column: 1 / -1; text-align: center; padding: 3rem 1rem; color: var(--charcoal-600);">
                    <p style="font-size: 1.1rem; font-weight: 700;">No species found matching your search.</p>
                    <p style="font-size: 0.9rem; margin-top: 0.5rem;">Try another keyword or select "All Species".</p>
                </div>
            `;
            return;
        }

        items.forEach(sp => {
            const card = document.createElement('div');
            card.className = 'species-card';
            
            const famClass = (sp.family || 'nymphalidae').toLowerCase();
            const sampleImgPath = sp.sampleImagePath || `dataset/train/${sp.id}_${sp.scientificName.replace(/\s+/g, '_')}/${sp.id}0001.jpg`;

            card.innerHTML = `
                <div class="species-card-img-wrap">
                    <img src="/api/sample?path=${encodeURIComponent(sampleImgPath)}" 
                         alt="${sp.commonName}" 
                         class="species-card-img"
                         onerror="this.onerror=null; this.src='/api/sample?path=dataset/train/081_Euthalia_zubeengargi/0810001.jpg';">
                </div>
                <div class="species-card-body">
                    <span class="species-card-family ${famClass}">${sp.family}</span>
                    <h3 class="species-card-name">${sp.commonName}</h3>
                    <div class="species-card-sci">${sp.scientificName}</div>
                    <p class="species-card-desc">${sp.description || sp.habitat || 'Rare butterfly species of Assam and Northeast India.'}</p>
                    <button type="button" class="btn-test-sample" data-img="${sampleImgPath}" data-name="${sp.commonName}">
                        Test Sample Image →
                    </button>
                </div>
            `;
            speciesCatalogGrid.appendChild(card);
        });

        document.querySelectorAll('.btn-test-sample').forEach(btn => {
            btn.addEventListener('click', () => {
                const imgPath = btn.dataset.img;
                const name = btn.dataset.name;
                switchSection('identify');
                fetchSampleImage(imgPath, name);
            });
        });
    }

    // Family filter chip event listeners
    familyPills.forEach(pill => {
        pill.addEventListener('click', () => {
            familyPills.forEach(p => p.classList.remove('active'));
            pill.classList.add('active');
            currentFamilyFilter = pill.dataset.family;
            applyCatalogFilters();
        });
    });

    // Real-time search event listener
    if (catalogSearchInput) {
        catalogSearchInput.addEventListener('input', (e) => {
            searchQuery = e.target.value;
            applyCatalogFilters();
        });
    }

    function showError(title, desc) {
        emptyState.classList.add('hidden');
        resultCard.classList.add('hidden');
        errorTitle.textContent = title;
        errorDesc.textContent = desc;
        errorCard.classList.remove('hidden');
    }

    function hideError() {
        errorCard.classList.add('hidden');
    }

    function showEmptyState() {
        hideError();
        resultCard.classList.add('hidden');
        emptyState.classList.remove('hidden');
    }

    errorDismissBtn.addEventListener('click', showEmptyState);

    // Initial catalog load
    loadSpeciesCatalog();
});
