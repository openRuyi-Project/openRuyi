# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name webpki
%global full_version 0.21.4
%global pkgname webpki-0.21

Name:           rust-webpki-0.21
Version:        0.21.4
Release:        %autorelease
Summary:        Rust crate "webpki"
License:        FIXME
URL:            https://github.com/briansmith/webpki
#!RemoteAsset:  sha256:b8e38c0608262c46d4a56202ebabdeb094cef7e560ca7a226c6bf055188aa4ea
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ring-0.16/alloc) >= 0.16.19
Requires:       crate(untrusted-0.7/default) >= 0.7.1
Provides:       crate(webpki) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/trust-anchor-util)

%description
Source code for takopackized Rust crate "webpki"

%package     -n %{name}+default
Summary:        Web PKI X.509 Certificate Verification - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/trust-anchor-util)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust webpki crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
