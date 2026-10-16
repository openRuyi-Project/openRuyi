# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sop
%global full_version 0.8.2
%global pkgname sop-0.8

Name:           rust-sop-0.8
Version:        0.8.2
Release:        %autorelease
Summary:        Rust crate "sop"
License:        MIT
URL:            https://sequoia-pgp.org/
#!RemoteAsset:  sha256:178bb001c144c5b83c9420f5ac1c4acc3b6e13b2f40914d150dddf54babf4714
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memsec-0.5) >= 0.5.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(thiserror-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sop"

%package     -n %{name}+anyhow
Summary:        Rust Interface for the Stateless OpenPGP Interface - feature "anyhow"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anyhow-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/anyhow) = %{version}

%description -n %{name}+anyhow
This metapackage enables feature "anyhow" for the Rust sop crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        Rust Interface for the Stateless OpenPGP Interface - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/default) >= 0.4.10
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust sop crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clap
Summary:        Rust Interface for the Stateless OpenPGP Interface - feature "clap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/derive) >= 4.0.0
Requires:       crate(clap-4/help) >= 4.0.0
Requires:       crate(clap-4/std) >= 4.0.0
Requires:       crate(clap-4/usage) >= 4.0.0
Requires:       crate(clap-4/wrap-help) >= 4.0.0
Provides:       crate(%{pkgname}/clap) = %{version}

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust sop crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clap-complete
Summary:        Rust Interface for the Stateless OpenPGP Interface - feature "clap_complete"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-complete-4) >= 4.0.0
Provides:       crate(%{pkgname}/clap-complete) = %{version}

%description -n %{name}+clap-complete
This metapackage enables feature "clap_complete" for the Rust sop crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clap-mangen
Summary:        Rust Interface for the Stateless OpenPGP Interface - feature "clap_mangen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-mangen-0.2/default) >= 0.2.19
Provides:       crate(%{pkgname}/clap-mangen) = %{version}

%description -n %{name}+clap-mangen
This metapackage enables feature "clap_mangen" for the Rust sop crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cli
Summary:        Rust Interface for the Stateless OpenPGP Interface - feature "cli" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/anyhow) = %{version}
Requires:       crate(%{pkgname}/chrono) = %{version}
Requires:       crate(%{pkgname}/clap) = %{version}
Requires:       crate(%{pkgname}/clap-complete) = %{version}
Requires:       crate(%{pkgname}/clap-mangen) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Provides:       crate(%{pkgname}/cli) = %{version}
Provides:       crate(%{pkgname}/cliv) = %{version}

%description -n %{name}+cli
This metapackage enables feature "cli" for the Rust sop crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "cliv" feature.

%package     -n %{name}+libc
Summary:        Rust Interface for the Stateless OpenPGP Interface - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust sop crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
