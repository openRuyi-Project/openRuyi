# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-pack
%global full_version 0.60.0
%global pkgname gix-pack-0.60

Name:           rust-gix-pack-0.60
Version:        0.60.0
Release:        %autorelease
Summary:        Rust crate "gix-pack"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:d8571df89bfca5abb49c3e3372393f7af7e6f8b8dbe2b96303593cef5b263019
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gix-chunk-0.4/default) >= 0.4.12
Requires:       crate(gix-features-0.43/crc32) >= 0.43.1
Requires:       crate(gix-features-0.43/default) >= 0.43.1
Requires:       crate(gix-features-0.43/progress) >= 0.43.1
Requires:       crate(gix-features-0.43/zlib) >= 0.43.1
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(gix-object-0.50/default) >= 0.50.2
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(memmap2-0.9/default) >= 0.9.10
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "gix-pack"

%package     -n %{name}+default
Summary:        Implements git packs and related data structures - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/generate)
Requires:       crate(%{pkgname}/streaming-input)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust gix-pack crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+document-features
Summary:        Implements git packs and related data structures - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-pack crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+generate
Summary:        Implements git packs and related data structures - feature "generate"
Requires:       crate(%{pkgname})
Requires:       crate(gix-diff-0.53) >= 0.53.0
Requires:       crate(gix-hashtable-0.9/default) >= 0.9.0
Requires:       crate(gix-traverse-0.47/default) >= 0.47.0
Requires:       crate(parking-lot-0.12) >= 0.12.5
Provides:       crate(%{pkgname}/generate)

%description -n %{name}+generate
This metapackage enables feature "generate" for the Rust gix-pack crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+object-cache-dynamic
Summary:        Implements git packs and related data structures - feature "object-cache-dynamic"
Requires:       crate(%{pkgname})
Requires:       crate(clru-0.6/default) >= 0.6.3
Requires:       crate(gix-hashtable-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/object-cache-dynamic)

%description -n %{name}+object-cache-dynamic
This metapackage enables feature "object-cache-dynamic" for the Rust gix-pack crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pack-cache-lru-dynamic
Summary:        Implements git packs and related data structures - feature "pack-cache-lru-dynamic"
Requires:       crate(%{pkgname})
Requires:       crate(clru-0.6/default) >= 0.6.3
Provides:       crate(%{pkgname}/pack-cache-lru-dynamic)

%description -n %{name}+pack-cache-lru-dynamic
This metapackage enables feature "pack-cache-lru-dynamic" for the Rust gix-pack crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pack-cache-lru-static
Summary:        Implements git packs and related data structures - feature "pack-cache-lru-static"
Requires:       crate(%{pkgname})
Requires:       crate(uluru-3.0/default) >= 3.0.0
Provides:       crate(%{pkgname}/pack-cache-lru-static)

%description -n %{name}+pack-cache-lru-static
This metapackage enables feature "pack-cache-lru-static" for the Rust gix-pack crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Implements git packs and related data structures - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(gix-object-0.50/serde) >= 0.50.2
Requires:       crate(serde-1.0/derive) >= 1.0.114
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-pack crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+streaming-input
Summary:        Implements git packs and related data structures - feature "streaming-input"
Requires:       crate(%{pkgname})
Requires:       crate(gix-tempfile-18.0) >= 18.0.0
Requires:       crate(parking-lot-0.12) >= 0.12.5
Provides:       crate(%{pkgname}/streaming-input)

%description -n %{name}+streaming-input
This metapackage enables feature "streaming-input" for the Rust gix-pack crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm
Summary:        Implements git packs and related data structures - feature "wasm"
Requires:       crate(%{pkgname})
Requires:       crate(gix-diff-0.53/wasm) >= 0.53.0
Provides:       crate(%{pkgname}/wasm)

%description -n %{name}+wasm
This metapackage enables feature "wasm" for the Rust gix-pack crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
