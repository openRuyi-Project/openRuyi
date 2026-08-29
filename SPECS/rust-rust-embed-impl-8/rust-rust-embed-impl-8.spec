# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rust-embed-impl
%global full_version 8.8.0
%global pkgname rust-embed-impl-8

Name:           rust-rust-embed-impl-8
Version:        8.8.0
Release:        %autorelease
Summary:        Rust crate "rust-embed-impl"
License:        MIT
URL:            https://pyrossh.dev/repos/rust-embed
#!RemoteAsset:  sha256:382499b49db77a7c19abd2a574f85ada7e9dbe125d5d1160fa5cad7c4cf71fc9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(rust-embed-utils-8/default) >= 8.8.0
Requires:       crate(syn-2/derive) >= 2.0.0
Requires:       crate(syn-2/parsing) >= 2.0.0
Requires:       crate(syn-2/printing) >= 2.0.0
Requires:       crate(syn-2/proc-macro) >= 2.0.0
Requires:       crate(walkdir-2/default) >= 2.3.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/compression) = %{version}
Provides:       crate(%{pkgname}/debug-embed) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/deterministic-timestamps) = %{version}

%description
Source code for takopackized Rust crate "rust-embed-impl"

%package     -n %{name}+include-exclude
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "include-exclude"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-embed-utils-8/include-exclude) >= 8.8.0
Provides:       crate(%{pkgname}/include-exclude) = %{version}

%description -n %{name}+include-exclude
This metapackage enables feature "include-exclude" for the Rust rust-embed-impl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mime-guess
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "mime-guess"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-embed-utils-8/mime-guess) >= 8.8.0
Provides:       crate(%{pkgname}/mime-guess) = %{version}

%description -n %{name}+mime-guess
This metapackage enables feature "mime-guess" for the Rust rust-embed-impl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+shellexpand
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "shellexpand" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(shellexpand-3/default) >= 3.0.0
Provides:       crate(%{pkgname}/interpolate-folder-path) = %{version}
Provides:       crate(%{pkgname}/shellexpand) = %{version}

%description -n %{name}+shellexpand
This metapackage enables feature "shellexpand" for the Rust rust-embed-impl crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "interpolate-folder-path" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
