# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-diff
%global full_version 0.53.0
%global pkgname gix-diff-0.53

Name:           rust-gix-diff-0.53
Version:        0.53.0
Release:        %autorelease
Summary:        Rust crate "gix-diff"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:de854852010d44a317f30c92d67a983e691c9478c8a3fb4117c1f48626bcdea8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1.0) >= 1.12.1
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(gix-object-0.50/default) >= 0.50.2
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "gix-diff"

%package     -n %{name}+blob
Summary:        Calculate differences between various git objects - feature "blob"
Requires:       crate(%{pkgname})
Requires:       crate(gix-command-0.6/default) >= 0.6.5
Requires:       crate(gix-filter-0.20/default) >= 0.20.0
Requires:       crate(gix-fs-0.16/default) >= 0.16.1
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-tempfile-18.0/default) >= 18.0.0
Requires:       crate(gix-trace-0.1/default) >= 0.1.18
Requires:       crate(gix-traverse-0.47/default) >= 0.47.0
Requires:       crate(gix-worktree-0.42/attributes) >= 0.42.0
Requires:       crate(imara-diff-0.1/default) >= 0.1.8
Provides:       crate(%{pkgname}/blob)

%description -n %{name}+blob
This metapackage enables feature "blob" for the Rust gix-diff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Calculate differences between various git objects - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/blob)
Requires:       crate(%{pkgname}/index)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust gix-diff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+document-features
Summary:        Calculate differences between various git objects - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-diff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+index
Summary:        Calculate differences between various git objects - feature "index"
Requires:       crate(%{pkgname})
Requires:       crate(gix-attributes-0.27/default) >= 0.27.0
Requires:       crate(gix-index-0.41/default) >= 0.41.0
Requires:       crate(gix-pathspec-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/index)

%description -n %{name}+index
This metapackage enables feature "index" for the Rust gix-diff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Calculate differences between various git objects - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(gix-hash-0.19/serde) >= 0.19.0
Requires:       crate(gix-index-0.41/serde) >= 0.41.0
Requires:       crate(gix-object-0.50/serde) >= 0.50.2
Requires:       crate(serde-1.0/derive) >= 1.0.114
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-diff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm
Summary:        Calculate differences between various git objects - feature "wasm"
Requires:       crate(%{pkgname})
Requires:       crate(getrandom-0.2/js) >= 0.2.8
Provides:       crate(%{pkgname}/wasm)

%description -n %{name}+wasm
This metapackage enables feature "wasm" for the Rust gix-diff crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
