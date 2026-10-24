/**
 * ButterflyAI — Senior UX Frontend Logic
 */

document.addEventListener('DOMContentLoaded', () => {
    let selectedFile = null;
    let speciesData = [];

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

    // --- 2. File Upload & Drag-and-Drop ---
    uploadPrompt.addEventListener('click', () => fileInput.click());
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

    function handleFileSelect(file) {
        if (!file.type.match('image.*')) {
            showError("Invalid File Format", "Please select a valid image file (JPG, PNG, or WEBP).");
            return;
        }

        selectedFile = file;
        fileNameText.textContent = file.name;

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

    // Sample Thumbnail Chips
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
            .then(res => res.blob())
            .then(blob => {
                const file = new File([blob], `${name.toLowerCase().replace(/\s+/g, '_')}.png`, { type: 'image/png' });
                handleFileSelect(file);
            })
            .catch(() => {
                showError("Sample Load Failed", "Could not load sample butterfly image.");
            });
    }

    // --- 3. AI Classification Scanner ---
    identifyBtn.addEventListener('click', runClassification);

    function runClassification() {
        if (!selectedFile) return;

        scannerOverlay.classList.remove('hidden');
        
        scannerStatusText.textContent = "Analyzing image...";
        setTimeout(() => {
            scannerStatusText.textContent = "Detecting visual features...";
        }, 350);
        setTimeout(() => {
            scannerStatusText.textContent = "Identifying species...";
        }, 700);

        const formData = new FormData();
        formData.append("image", selectedFile, selectedFile.name);

        fetch('/api/classify', {
            method: 'POST',
            headers: {
                'X-File-Name': selectedFile.name
            },
            body: formData
        })
        .then(async res => {
            let data = null;
            try {
                data = await res.json();
            } catch (e) {}

            if (!res.ok) {
                const msg = (data && data.error) ? data.error : ("Server returned status " + res.status);
                throw new Error(msg);
            }
            return data;
        })
        .then(data => {
            setTimeout(() => {
                scannerOverlay.classList.add('hidden');
                if (data && data.success) {
                    renderResults(data);
                } else {
                    showError("Prediction Error", (data && data.error) || "Model could not classify species.");
                }
            }, 850);
        })
        .catch(err => {
            scannerOverlay.classList.add('hidden');
            showError("Classification Error", err.message || "Failed to connect to ButterflyAI inference engine.");
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
        resHabitat.textContent = primary.habitat || 'Forests & Meadows';
        resDescription.textContent = primary.description || 'Butterfly species identified by mobile vision tensor model.';

        animateConfidenceCount(primary.confidence);

        taxKingdom.textContent = primary.kingdom || 'Animalia';
        taxPhylum.textContent = primary.phylum || 'Arthropoda';
        taxClass.textContent = primary.className || 'Insecta';
        taxOrder.textContent = primary.order || 'Lepidoptera';
        taxFamily.textContent = primary.family || 'Nymphalidae';
        taxGenus.textContent = primary.genus || 'Danaus';
        taxSpecies.textContent = primary.speciesName || 'D. plexippus';

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
        let current = 0;
        const duration = 800;
        const startTime = performance.now();

        resConfidenceBar.style.width = '0%';

        function updateCount(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const easeProgress = 1 - Math.pow(1 - progress, 3);
            current = easeProgress * targetConfidence;

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

    // --- 5. Species Catalog ---
    function loadSpeciesCatalog() {
        fetch('/api/species')
            .then(res => res.json())
            .then(data => {
                speciesData = data;
                renderSpeciesCatalog(data);
            })
            .catch(err => {
                console.error("Error fetching species catalog:", err);
            });
    }

    function renderSpeciesCatalog(items) {
        speciesCatalogGrid.innerHTML = '';
        items.forEach(sp => {
            const card = document.createElement('div');
            card.className = 'species-card';
            card.innerHTML = `
                <img src="/api/sample?path=${encodeURIComponent(sp.sampleImagePath)}" alt="${sp.commonName}" class="species-card-img">
                <div class="species-card-body">
                    <span class="species-card-family">${sp.family}</span>
                    <h3 class="species-card-name">${sp.commonName}</h3>
                    <div class="species-card-sci">${sp.scientificName}</div>
                    <p class="species-card-desc">${sp.description}</p>
                    <button type="button" class="btn-test-sample" data-img="${sp.sampleImagePath}" data-name="${sp.commonName}">
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

    loadSpeciesCatalog();
});
