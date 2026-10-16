# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name openpgp-cert-d
%global full_version 0.3.4
%global pkgname openpgp-cert-d-0.3

Name:           rust-openpgp-cert-d-0.3
Version:        0.3.4
Release:        %autorelease
Summary:        Rust crate "openpgp-cert-d"
License:        MIT
URL:            https://gitlab.com/sequoia-pgp/pgp-cert-d
#!RemoteAsset:  sha256:d3dd47b0b6df1022ca8a9a06791261c3153028abef191fe53aa326b7f443f2d6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/std) >= 1.0.0
Requires:       crate(dirs-5) >= 5.0.0
Requires:       crate(fd-lock-3) >= 3.0.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(sha1collisiondetection-0.3) >= 0.3.0
Requires:       crate(sha2-0.10/std) >= 0.10.0
Requires:       crate(tempfile-3) >= 3.2.0
Requires:       crate(thiserror-1) >= 1.0.0
Requires:       crate(walkdir-2) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "openpgp-cert-d"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
