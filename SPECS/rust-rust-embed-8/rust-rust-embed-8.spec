# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rust-embed
%global full_version 8.8.0
%global pkgname rust-embed-8

Name:           rust-rust-embed-8
Version:        8.8.0
Release:        %autorelease
Summary:        Rust crate "rust-embed"
License:        MIT
URL:            https://pyrossh.dev/repos/rust-embed
#!RemoteAsset:  sha256:fb44e1917075637ee8c7bcb865cf8830e3a92b5b1189e44e3a0ab5a0d5be314b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rust-embed-impl-8/default) >= 8.8.0
Requires:       crate(rust-embed-utils-8/default) >= 8.8.0
Requires:       crate(walkdir-2/default) >= 2.3.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rust-embed"

%package     -n %{name}+actix
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "actix"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/actix-web) = %{version}
Requires:       crate(%{pkgname}/mime-guess) = %{version}
Provides:       crate(%{pkgname}/actix) = %{version}

%description -n %{name}+actix
This metapackage enables feature "actix" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+actix-web
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "actix-web"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(actix-web-4/default) >= 4.0.0
Provides:       crate(%{pkgname}/actix-web) = %{version}

%description -n %{name}+actix-web
This metapackage enables feature "actix-web" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+axum
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "axum"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(axum-0.8/http1) >= 0.8.0
Requires:       crate(axum-0.8/tokio) >= 0.8.0
Provides:       crate(%{pkgname}/axum) = %{version}

%description -n %{name}+axum
This metapackage enables feature "axum" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+axum-ex
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "axum-ex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/axum) = %{version}
Requires:       crate(%{pkgname}/mime-guess) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Provides:       crate(%{pkgname}/axum-ex) = %{version}

%description -n %{name}+axum-ex
This metapackage enables feature "axum-ex" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compression
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "compression"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/include-flate) = %{version}
Requires:       crate(rust-embed-impl-8/compression) >= 8.8.0
Provides:       crate(%{pkgname}/compression) = %{version}

%description -n %{name}+compression
This metapackage enables feature "compression" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug-embed
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "debug-embed"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-embed-impl-8/debug-embed) >= 8.8.0
Requires:       crate(rust-embed-utils-8/debug-embed) >= 8.8.0
Provides:       crate(%{pkgname}/debug-embed) = %{version}

%description -n %{name}+debug-embed
This metapackage enables feature "debug-embed" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deterministic-timestamps
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "deterministic-timestamps"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-embed-impl-8/deterministic-timestamps) >= 8.8.0
Provides:       crate(%{pkgname}/deterministic-timestamps) = %{version}

%description -n %{name}+deterministic-timestamps
This metapackage enables feature "deterministic-timestamps" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hex
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "hex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hex-0.4/default) >= 0.4.3
Provides:       crate(%{pkgname}/hex) = %{version}

%description -n %{name}+hex
This metapackage enables feature "hex" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+include-exclude
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "include-exclude"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-embed-impl-8/include-exclude) >= 8.8.0
Requires:       crate(rust-embed-utils-8/include-exclude) >= 8.8.0
Provides:       crate(%{pkgname}/include-exclude) = %{version}

%description -n %{name}+include-exclude
This metapackage enables feature "include-exclude" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+include-flate
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "include-flate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(include-flate-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/include-flate) = %{version}

%description -n %{name}+include-flate
This metapackage enables feature "include-flate" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+interpolate-folder-path
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "interpolate-folder-path"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-embed-impl-8/interpolate-folder-path) >= 8.8.0
Provides:       crate(%{pkgname}/interpolate-folder-path) = %{version}

%description -n %{name}+interpolate-folder-path
This metapackage enables feature "interpolate-folder-path" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mime-guess
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "mime_guess"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mime-guess-2/default) >= 2.0.5
Requires:       crate(rust-embed-impl-8/mime-guess) >= 8.8.0
Requires:       crate(rust-embed-utils-8/mime-guess) >= 8.8.0
Provides:       crate(%{pkgname}/mime-guess) = %{version}

%description -n %{name}+mime-guess
This metapackage enables feature "mime_guess" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+poem
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "poem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(poem-1/server) >= 1.3.30
Provides:       crate(%{pkgname}/poem) = %{version}

%description -n %{name}+poem
This metapackage enables feature "poem" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+poem-ex
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "poem-ex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hex) = %{version}
Requires:       crate(%{pkgname}/mime-guess) = %{version}
Requires:       crate(%{pkgname}/poem) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Provides:       crate(%{pkgname}/poem-ex) = %{version}

%description -n %{name}+poem-ex
This metapackage enables feature "poem-ex" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rocket
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "rocket"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rocket-0.5.0-rc.2) >= 0.5.0-rc.2
Provides:       crate(%{pkgname}/rocket) = %{version}

%description -n %{name}+rocket
This metapackage enables feature "rocket" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+salvo
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "salvo"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(salvo-0.16) >= 0.16.0
Provides:       crate(%{pkgname}/salvo) = %{version}

%description -n %{name}+salvo
This metapackage enables feature "salvo" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+salvo-ex
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "salvo-ex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hex) = %{version}
Requires:       crate(%{pkgname}/mime-guess) = %{version}
Requires:       crate(%{pkgname}/salvo) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Provides:       crate(%{pkgname}/salvo-ex) = %{version}

%description -n %{name}+salvo-ex
This metapackage enables feature "salvo-ex" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/macros) >= 1.0.0
Requires:       crate(tokio-1/rt-multi-thread) >= 1.0.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+warp
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "warp"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(warp-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/warp) = %{version}

%description -n %{name}+warp
This metapackage enables feature "warp" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+warp-ex
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "warp-ex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/mime-guess) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(%{pkgname}/warp) = %{version}
Provides:       crate(%{pkgname}/warp-ex) = %{version}

%description -n %{name}+warp-ex
This metapackage enables feature "warp-ex" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
