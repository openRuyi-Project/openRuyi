# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name etherparse
%global full_version 0.19.0
%global pkgname etherparse-0.19

Name:           rust-etherparse-0.19
Version:        0.19.0
Release:        %autorelease
Summary:        Rust crate "etherparse"
License:        MIT OR Apache-2.0
URL:            https://github.com/JulianSchmid/etherparse
#!RemoteAsset:  sha256:b119b9796ff800751a220394b8b3613f26dd30c48f254f6837e64c464872d1c7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrayvec-0.7) >= 0.7.2
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "etherparse"

%package     -n %{name}+std
Summary:        Parsing & writing a bunch of packet based protocols (EthernetII, IPv4, IPv6, UDP, TCP ...) - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrayvec-0.7/std) >= 0.7.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust etherparse crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
