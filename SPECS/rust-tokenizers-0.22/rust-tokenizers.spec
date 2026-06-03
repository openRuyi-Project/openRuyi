# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokenizers
%global full_version 0.22.2
%global pkgname tokenizers-0.22

Name:           rust-tokenizers-0.22
Version:        0.22.2
Release:        %autorelease
Summary:        Rust crate "tokenizers"
License:        Apache-2.0
URL:            https://github.com/huggingface/tokenizers
#!RemoteAsset:  sha256:b238e22d44a15349529690fb07bd645cf58149a1b1e44d6cb5bd1641ff1a6223
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ahash-0.8/default) >= 0.8.12
Requires:       crate(ahash-0.8/serde) >= 0.8.12
Requires:       crate(aho-corasick-1.0/default) >= 1.1.4
Requires:       crate(compact-str-0.9/default) >= 0.9.0
Requires:       crate(compact-str-0.9/serde) >= 0.9.0
Requires:       crate(dary-heap-0.3/default) >= 0.3.8
Requires:       crate(dary-heap-0.3/serde) >= 0.3.8
Requires:       crate(derive-builder-0.20/default) >= 0.20.2
Requires:       crate(esaxx-rs-0.1) >= 0.1.10
Requires:       crate(getrandom-0.3/default) >= 0.3.4
Requires:       crate(itertools-0.14/default) >= 0.14.0
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(macro-rules-attribute-0.2/default) >= 0.2.2
Requires:       crate(monostate-0.1/default) >= 0.1.18
Requires:       crate(paste-1.0/default) >= 1.0.15
Requires:       crate(rand-0.9/default) >= 0.9.2
Requires:       crate(rayon-1.0/default) >= 1.11.0
Requires:       crate(rayon-cond-0.4/default) >= 0.4.0
Requires:       crate(regex-1.0/default) >= 1.12.2
Requires:       crate(regex-syntax-0.8/default) >= 0.8.8
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Requires:       crate(spm-precompiled-0.1/default) >= 0.1.4
Requires:       crate(thiserror-2.0/default) >= 2.0.17
Requires:       crate(unicode-categories-0.1/default) >= 0.1.1
Requires:       crate(unicode-normalization-alignments-0.1/default) >= 0.1.12
Requires:       crate(unicode-segmentation-1.0/default) >= 1.12.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "tokenizers"

%package     -n %{name}+default
Summary:        Provides an implementation of today's most used tokenizers, with a focus on performances and versatility - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/esaxx-fast)
Requires:       crate(%{pkgname}/onig)
Requires:       crate(%{pkgname}/progressbar)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tokenizers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+esaxx-fast
Summary:        Provides an implementation of today's most used tokenizers, with a focus on performances and versatility - feature "esaxx_fast"
Requires:       crate(%{pkgname})
Requires:       crate(esaxx-rs-0.1/cpp) >= 0.1.10
Provides:       crate(%{pkgname}/esaxx-fast)

%description -n %{name}+esaxx-fast
This metapackage enables feature "esaxx_fast" for the Rust tokenizers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fancy-regex
Summary:        Provides an implementation of today's most used tokenizers, with a focus on performances and versatility - feature "fancy-regex"
Requires:       crate(%{pkgname})
Requires:       crate(fancy-regex-0.14/default) >= 0.14.0
Provides:       crate(%{pkgname}/fancy-regex)

%description -n %{name}+fancy-regex
This metapackage enables feature "fancy-regex" for the Rust tokenizers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hf-hub
Summary:        Provides an implementation of today's most used tokenizers, with a focus on performances and versatility - feature "hf-hub" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(hf-hub-0.4/ureq) >= 0.4.1
Provides:       crate(%{pkgname}/hf-hub)
Provides:       crate(%{pkgname}/http)

%description -n %{name}+hf-hub
This metapackage enables feature "hf-hub" for the Rust tokenizers crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "http" feature.

%package     -n %{name}+indicatif
Summary:        Provides an implementation of today's most used tokenizers, with a focus on performances and versatility - feature "indicatif" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(indicatif-0.18/default) >= 0.18.0
Provides:       crate(%{pkgname}/indicatif)
Provides:       crate(%{pkgname}/progressbar)

%description -n %{name}+indicatif
This metapackage enables feature "indicatif" for the Rust tokenizers crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "progressbar" feature.

%package     -n %{name}+onig
Summary:        Provides an implementation of today's most used tokenizers, with a focus on performances and versatility - feature "onig"
Requires:       crate(%{pkgname})
Requires:       crate(onig-6.0) >= 6.5.1
Provides:       crate(%{pkgname}/onig)

%description -n %{name}+onig
This metapackage enables feature "onig" for the Rust tokenizers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-tls
Summary:        Provides an implementation of today's most used tokenizers, with a focus on performances and versatility - feature "rustls-tls"
Requires:       crate(%{pkgname})
Requires:       crate(hf-hub-0.4/rustls-tls) >= 0.4.1
Requires:       crate(hf-hub-0.4/ureq) >= 0.4.1
Provides:       crate(%{pkgname}/rustls-tls)

%description -n %{name}+rustls-tls
This metapackage enables feature "rustls-tls" for the Rust tokenizers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-wasm
Summary:        Provides an implementation of today's most used tokenizers, with a focus on performances and versatility - feature "unstable_wasm"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/fancy-regex)
Requires:       crate(getrandom-0.3/wasm-js) >= 0.3.4
Provides:       crate(%{pkgname}/unstable-wasm)

%description -n %{name}+unstable-wasm
This metapackage enables feature "unstable_wasm" for the Rust tokenizers crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
