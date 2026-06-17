# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name kasuari
%global full_version 0.4.12
%global pkgname kasuari-0.4

Name:           rust-kasuari-0.4
Version:        0.4.12
Release:        %autorelease
Summary:        Rust crate "kasuari"
License:        MIT OR Apache-2.0
URL:            https://github.com/ratatui/kasuari
#!RemoteAsset:  sha256:bde5057d6143cc94e861d90f591b9303d6716c6b9602309150bd068853c10899
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hashbrown-0.16/default) >= 0.16.0
Requires:       crate(thiserror-2) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
A fork of the unmaintained cassowary-rs crate with improvments and bug fixes. Kasuari is the indonesian name for the cassowary bird.
Source code for takopackized Rust crate "kasuari"

%package     -n %{name}+document-features
Summary:        Rust layout solver for GUIs, based on the Cassowary algorithm - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
A fork of the unmaintained cassowary-rs crate with improvments and bug fixes. Kasuari is the indonesian name for the cassowary bird.
This metapackage enables feature "document-features" for the Rust kasuari crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic
Summary:        Rust layout solver for GUIs, based on the Cassowary algorithm - feature "portable-atomic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(portable-atomic-1/require-cas) >= 1.13.0
Requires:       crate(portable-atomic-util-0.2/alloc) >= 0.2.5
Requires:       crate(portable-atomic-util-0.2/default) >= 0.2.5
Provides:       crate(%{pkgname}/portable-atomic) = %{version}

%description -n %{name}+portable-atomic
A fork of the unmaintained cassowary-rs crate with improvments and bug fixes. Kasuari is the indonesian name for the cassowary bird.
This metapackage enables feature "portable-atomic" for the Rust kasuari crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Rust layout solver for GUIs, based on the Cassowary algorithm - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(portable-atomic-1/require-cas) >= 1.13.0
Requires:       crate(portable-atomic-1/std) >= 1.13.0
Requires:       crate(thiserror-2/std) >= 2.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
A fork of the unmaintained cassowary-rs crate with improvments and bug fixes. Kasuari is the indonesian name for the cassowary bird.
This metapackage enables feature "std" for the Rust kasuari crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
