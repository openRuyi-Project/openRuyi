# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name object_store
%global full_version 0.13.2
%global pkgname object-store-0.13

Name:           rust-object-store-0.13
Version:        0.13.2
Release:        %autorelease
Summary:        Rust crate "object_store"
License:        MIT OR Apache-2.0
URL:            https://github.com/apache/arrow-rs-object-store
#!RemoteAsset:  sha256:622acbc9100d3c10e2ee15804b0caa40e55c933d5aa53814cd520805b7958a49
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-trait-0.1/default) >= 0.1.53
Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(chrono-0.4/clock) >= 0.4.34
Requires:       crate(futures-channel-0.3/default) >= 0.3.0
Requires:       crate(futures-channel-0.3/sink) >= 0.3.0
Requires:       crate(futures-core-0.3/default) >= 0.3.0
Requires:       crate(futures-util-0.3/default) >= 0.3.0
Requires:       crate(futures-util-0.3/sink) >= 0.3.0
Requires:       crate(http-1/default) >= 1.2.0
Requires:       crate(humantime-2/default) >= 2.1.0
Requires:       crate(itertools-0.14/default) >= 0.14.0
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Requires:       crate(percent-encoding-2/default) >= 2.1.0
Requires:       crate(thiserror-2/default) >= 2.0.2
Requires:       crate(url-2/default) >= 2.2.0
Requires:       crate(wasm-bindgen-futures-0.4/default) >= 0.4.18
Requires:       crate(web-time-1/default) >= 1.1.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "object_store"

%package     -n %{name}+aws
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "aws"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cloud) = %{version}
Requires:       crate(%{pkgname}/md-5) = %{version}
Provides:       crate(%{pkgname}/aws) = %{version}

%description -n %{name}+aws
This metapackage enables feature "aws" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+azure
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "azure"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cloud) = %{version}
Requires:       crate(%{pkgname}/httparse) = %{version}
Provides:       crate(%{pkgname}/azure) = %{version}

%description -n %{name}+azure
This metapackage enables feature "azure" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+base64
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "base64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64-0.22/std) >= 0.22.0
Provides:       crate(%{pkgname}/base64) = %{version}

%description -n %{name}+base64
This metapackage enables feature "base64" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cloud
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "cloud" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/base64) = %{version}
Requires:       crate(%{pkgname}/form-urlencoded) = %{version}
Requires:       crate(%{pkgname}/http-body-util) = %{version}
Requires:       crate(%{pkgname}/hyper) = %{version}
Requires:       crate(%{pkgname}/quick-xml) = %{version}
Requires:       crate(%{pkgname}/rand) = %{version}
Requires:       crate(%{pkgname}/reqwest) = %{version}
Requires:       crate(%{pkgname}/ring) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Requires:       crate(%{pkgname}/serde-urlencoded) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(chrono-0.4/clock) >= 0.4.34
Requires:       crate(chrono-0.4/serde) >= 0.4.34
Requires:       crate(reqwest-0.12/http2) >= 0.12.0
Requires:       crate(reqwest-0.12/rustls-tls-native-roots) >= 0.12.0
Requires:       crate(reqwest-0.12/stream) >= 0.12.0
Provides:       crate(%{pkgname}/cloud) = %{version}
Provides:       crate(%{pkgname}/http) = %{version}

%description -n %{name}+cloud
This metapackage enables feature "cloud" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "http" feature.

%package     -n %{name}+form-urlencoded
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "form_urlencoded"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(form-urlencoded-1/default) >= 1.2.0
Provides:       crate(%{pkgname}/form-urlencoded) = %{version}

%description -n %{name}+form-urlencoded
This metapackage enables feature "form_urlencoded" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fs
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "fs" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(%{pkgname}/walkdir) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/fs) = %{version}

%description -n %{name}+fs
This metapackage enables feature "fs" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+gcp
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "gcp"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cloud) = %{version}
Requires:       crate(%{pkgname}/rustls-pki-types) = %{version}
Provides:       crate(%{pkgname}/gcp) = %{version}

%description -n %{name}+gcp
This metapackage enables feature "gcp" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http-body-util
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "http-body-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(http-body-util-0.1/default) >= 0.1.2
Provides:       crate(%{pkgname}/http-body-util) = %{version}

%description -n %{name}+http-body-util
This metapackage enables feature "http-body-util" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+httparse
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "httparse"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(httparse-1/std) >= 1.8.0
Provides:       crate(%{pkgname}/httparse) = %{version}

%description -n %{name}+httparse
This metapackage enables feature "httparse" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hyper
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "hyper"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-1) >= 1.2.0
Provides:       crate(%{pkgname}/hyper) = %{version}

%description -n %{name}+hyper
This metapackage enables feature "hyper" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+integration
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "integration"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Provides:       crate(%{pkgname}/integration) = %{version}

%description -n %{name}+integration
This metapackage enables feature "integration" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+md-5
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "md-5"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(md-5-0.10) >= 0.10.6
Provides:       crate(%{pkgname}/md-5) = %{version}

%description -n %{name}+md-5
This metapackage enables feature "md-5" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quick-xml
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "quick-xml"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quick-xml-0.39/default) >= 0.39.0
Requires:       crate(quick-xml-0.39/overlapped-lists) >= 0.39.0
Requires:       crate(quick-xml-0.39/serialize) >= 0.39.0
Provides:       crate(%{pkgname}/quick-xml) = %{version}

%description -n %{name}+quick-xml
This metapackage enables feature "quick-xml" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.10/std) >= 0.10.0
Requires:       crate(rand-0.10/std-rng) >= 0.10.0
Requires:       crate(rand-0.10/thread-rng) >= 0.10.0
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+reqwest
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "reqwest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.12/http2) >= 0.12.0
Requires:       crate(reqwest-0.12/rustls-tls-native-roots) >= 0.12.0
Provides:       crate(%{pkgname}/reqwest) = %{version}

%description -n %{name}+reqwest
This metapackage enables feature "reqwest" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ring
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ring-0.17/std) >= 0.17.0
Provides:       crate(%{pkgname}/ring) = %{version}

%description -n %{name}+ring
This metapackage enables feature "ring" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-pki-types
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "rustls-pki-types"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustls-pki-types-1/std) >= 1.9.0
Provides:       crate(%{pkgname}/rustls-pki-types) = %{version}

%description -n %{name}+rustls-pki-types
This metapackage enables feature "rustls-pki-types" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-urlencoded
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "serde_urlencoded"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-urlencoded-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/serde-urlencoded) = %{version}

%description -n %{name}+serde-urlencoded
This metapackage enables feature "serde_urlencoded" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tls-webpki-roots
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "tls-webpki-roots"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.12/http2) >= 0.12.0
Requires:       crate(reqwest-0.12/rustls-tls-native-roots) >= 0.12.0
Requires:       crate(reqwest-0.12/rustls-tls-webpki-roots) >= 0.12.0
Provides:       crate(%{pkgname}/tls-webpki-roots) = %{version}

%description -n %{name}+tls-webpki-roots
This metapackage enables feature "tls-webpki-roots" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.29.0
Requires:       crate(tokio-1/io-util) >= 1.29.0
Requires:       crate(tokio-1/macros) >= 1.29.0
Requires:       crate(tokio-1/rt) >= 1.29.0
Requires:       crate(tokio-1/sync) >= 1.29.0
Requires:       crate(tokio-1/time) >= 1.29.0
Requires:       crate(tracing-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+walkdir
Summary:        Generic object store interface for uniformly interacting with AWS S3, Google Cloud Storage, Azure Blob Storage and local files - feature "walkdir"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(walkdir-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/walkdir) = %{version}

%description -n %{name}+walkdir
This metapackage enables feature "walkdir" for the Rust object_store crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
