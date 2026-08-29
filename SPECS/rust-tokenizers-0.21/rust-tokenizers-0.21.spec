# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokenizers
%global full_version 0.21.2
%global pkgname tokenizers-0.21

Name:           rust-tokenizers-0.21
Version:        0.21.2
Release:        %autorelease
Summary:        Rust crate "tokenizers"
License:        Apache-2.0
URL:            https://github.com/huggingface/tokenizers
#!RemoteAsset:  sha256:4c3846d8588abed0daba25a0e47edd58ea15e450a6088b2575f5116fdb0b27ca
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ahash-0.8/default) >= 0.8.11
Requires:       crate(ahash-0.8/serde) >= 0.8.11
Requires:       crate(aho-corasick-1/default) >= 1.1.0
Requires:       crate(compact-str-0.9/default) >= 0.9.0
Requires:       crate(compact-str-0.9/serde) >= 0.9.0
Requires:       crate(dary-heap-0.3/default) >= 0.3.6
Requires:       crate(dary-heap-0.3/serde) >= 0.3.6
Requires:       crate(derive-builder-0.20/default) >= 0.20.0
Requires:       crate(esaxx-rs-0.1) >= 0.1.10
Requires:       crate(getrandom-0.3/default) >= 0.3.0
Requires:       crate(itertools-0.14/default) >= 0.14.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(macro-rules-attribute-0.2/default) >= 0.2.0
Requires:       crate(monostate-0.1/default) >= 0.1.12
Requires:       crate(paste-1/default) >= 1.0.14
Requires:       crate(rand-0.9/default) >= 0.9.0
Requires:       crate(rayon-1/default) >= 1.10.0
Requires:       crate(rayon-cond-0.4/default) >= 0.4.0
Requires:       crate(regex-1/default) >= 1.10.0
Requires:       crate(regex-syntax-0.8/default) >= 0.8.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(spm-precompiled-0.1/default) >= 0.1.3
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(unicode-categories-0.1/default) >= 0.1.0
Requires:       crate(unicode-normalization-alignments-0.1/default) >= 0.1.0
Requires:       crate(unicode-segmentation-1/default) >= 1.11.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "tokenizers"

%package     -n %{name}+default
Summary:        Provides an implementation of today's most used tokenizers, with a focus on performances and versatility - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/esaxx-fast) = %{version}
Requires:       crate(%{pkgname}/onig) = %{version}
Requires:       crate(%{pkgname}/progressbar) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tokenizers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+esaxx-fast
Summary:        Provides an implementation of today's most used tokenizers, with a focus on performances and versatility - feature "esaxx_fast"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(esaxx-rs-0.1/cpp) >= 0.1.10
Provides:       crate(%{pkgname}/esaxx-fast) = %{version}

%description -n %{name}+esaxx-fast
This metapackage enables feature "esaxx_fast" for the Rust tokenizers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fancy-regex
Summary:        Provides an implementation of today's most used tokenizers, with a focus on performances and versatility - feature "fancy-regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fancy-regex-0.14/default) >= 0.14.0
Provides:       crate(%{pkgname}/fancy-regex) = %{version}

%description -n %{name}+fancy-regex
This metapackage enables feature "fancy-regex" for the Rust tokenizers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hf-hub
Summary:        Provides an implementation of today's most used tokenizers, with a focus on performances and versatility - feature "hf-hub" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hf-hub-0.4/ureq) >= 0.4.1
Provides:       crate(%{pkgname}/hf-hub) = %{version}
Provides:       crate(%{pkgname}/http) = %{version}

%description -n %{name}+hf-hub
This metapackage enables feature "hf-hub" for the Rust tokenizers crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "http" feature.

%package     -n %{name}+indicatif
Summary:        Provides an implementation of today's most used tokenizers, with a focus on performances and versatility - feature "indicatif" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indicatif-0.17/default) >= 0.17.0
Provides:       crate(%{pkgname}/indicatif) = %{version}
Provides:       crate(%{pkgname}/progressbar) = %{version}

%description -n %{name}+indicatif
This metapackage enables feature "indicatif" for the Rust tokenizers crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "progressbar" feature.

%package     -n %{name}+onig
Summary:        Provides an implementation of today's most used tokenizers, with a focus on performances and versatility - feature "onig"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(onig-6) >= 6.5.1
Provides:       crate(%{pkgname}/onig) = %{version}

%description -n %{name}+onig
This metapackage enables feature "onig" for the Rust tokenizers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-tls
Summary:        Provides an implementation of today's most used tokenizers, with a focus on performances and versatility - feature "rustls-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hf-hub-0.4/rustls-tls) >= 0.4.1
Requires:       crate(hf-hub-0.4/ureq) >= 0.4.1
Provides:       crate(%{pkgname}/rustls-tls) = %{version}

%description -n %{name}+rustls-tls
This metapackage enables feature "rustls-tls" for the Rust tokenizers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-wasm
Summary:        Provides an implementation of today's most used tokenizers, with a focus on performances and versatility - feature "unstable_wasm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fancy-regex) = %{version}
Requires:       crate(getrandom-0.3/wasm-js) >= 0.3.0
Provides:       crate(%{pkgname}/unstable-wasm) = %{version}

%description -n %{name}+unstable-wasm
This metapackage enables feature "unstable_wasm" for the Rust tokenizers crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
