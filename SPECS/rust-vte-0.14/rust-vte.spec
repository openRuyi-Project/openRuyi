# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vte
%global full_version 0.14.1
%global pkgname vte-0.14

Name:           rust-vte-0.14
Version:        0.14.1
Release:        %autorelease
Summary:        Rust crate "vte"
License:        Apache-2.0 OR MIT
URL:            https://github.com/alacritty/vte
#!RemoteAsset:  sha256:231fdcd7ef3037e8330d8e17e61011a2c244126acc0a982f4040ac3f9f0bc077
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2.0/default) >= 2.7.4
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "vte"

%package     -n %{name}+ansi
Summary:        Parser for implementing terminal emulators - feature "ansi"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(%{pkgname}/cursor-icon)
Requires:       crate(%{pkgname}/log)
Provides:       crate(%{pkgname}/ansi)

%description -n %{name}+ansi
This metapackage enables feature "ansi" for the Rust vte crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arrayvec
Summary:        Parser for implementing terminal emulators - feature "arrayvec" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(arrayvec-0.7) >= 0.7.2
Provides:       crate(%{pkgname}/arrayvec)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/no-std)

%description -n %{name}+arrayvec
This metapackage enables feature "arrayvec" for the Rust vte crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "no_std" features.

%package     -n %{name}+bitflags
Summary:        Parser for implementing terminal emulators - feature "bitflags"
Requires:       crate(%{pkgname})
Requires:       crate(bitflags-2.0) >= 2.3.3
Provides:       crate(%{pkgname}/bitflags)

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust vte crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cursor-icon
Summary:        Parser for implementing terminal emulators - feature "cursor-icon"
Requires:       crate(%{pkgname})
Requires:       crate(cursor-icon-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/cursor-icon)

%description -n %{name}+cursor-icon
This metapackage enables feature "cursor-icon" for the Rust vte crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Parser for implementing terminal emulators - feature "log"
Requires:       crate(%{pkgname})
Requires:       crate(log-0.4/default) >= 0.4.17
Provides:       crate(%{pkgname}/log)

%description -n %{name}+log
This metapackage enables feature "log" for the Rust vte crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Parser for implementing terminal emulators - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.160
Requires:       crate(serde-1.0/derive) >= 1.0.160
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust vte crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
