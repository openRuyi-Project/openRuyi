# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name polyval
%global full_version 0.7.1
%global pkgname polyval-0.7

Name:           rust-polyval-0.7
Version:        0.7.1
Release:        %autorelease
Summary:        Rust crate "polyval"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/universal-hashes
#!RemoteAsset:  sha256:7dfc63250416fea14f5749b90725916a6c903f599d51cb635aa7a52bfd03eede
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cpubits-0.1/default) >= 0.1.0
Requires:       crate(cpufeatures-0.3/default) >= 0.3.0
Requires:       crate(universal-hash-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/hazmat) = %{version}

%description
Source code for takopackized Rust crate "polyval"

%package     -n %{name}+zeroize
Summary:        GHASH-like universal hash over GF(2^128) useful for constructing a Message Authentication Code (MAC) - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust polyval crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
