# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vte
%global full_version 0.11.1
%global pkgname vte-0.11

Name:           rust-vte-0.11
Version:        0.11.1
Release:        %autorelease
Summary:        Rust crate "vte"
License:        Apache-2.0 OR MIT
URL:            https://github.com/alacritty/vte
#!RemoteAsset:  sha256:f5022b5fbf9407086c180e9557be968742d839e68346af7792b8592489732197
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(utf8parse-0.2/default) >= 0.2.0
Requires:       crate(vte-generate-state-changes-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "vte"

%package     -n %{name}+arrayvec
Summary:        Parser for implementing terminal emulators - feature "arrayvec" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrayvec-0.7) >= 0.7.2
Provides:       crate(%{pkgname}/arrayvec) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/no-std) = %{version}

%description -n %{name}+arrayvec
This metapackage enables feature "arrayvec" for the Rust vte crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "no_std" features.

%package     -n %{name}+log
Summary:        Parser for implementing terminal emulators - feature "log" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.17
Provides:       crate(%{pkgname}/ansi) = %{version}
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust vte crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "ansi" feature.

%package     -n %{name}+nightly
Summary:        Parser for implementing terminal emulators - feature "nightly"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(utf8parse-0.2/nightly) >= 0.2.0
Provides:       crate(%{pkgname}/nightly) = %{version}

%description -n %{name}+nightly
This metapackage enables feature "nightly" for the Rust vte crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Parser for implementing terminal emulators - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.160
Requires:       crate(serde-1/derive) >= 1.0.160
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust vte crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
