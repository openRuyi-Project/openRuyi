# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name qtls
%global full_version 0.1.0
%global pkgname qtls-0.1

Name:           rust-qtls-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "qtls"
License:        Apache-2.0
URL:            https://github.com/genmeta/dquic
#!RemoteAsset:  sha256:427f5e986d4ce4a397f8712265e1b3dfaf043d5c2d300e0f836ecc3a9f601b06
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(der-0.8/default) >= 0.8.0
Requires:       crate(pkix-path-0.3/std) >= 0.3.2
Requires:       crate(pkix-revocation-0.3/ocsp) >= 0.3.3
Requires:       crate(qrustls-0.23/std) >= 0.23.45
Requires:       crate(signature-2/default) >= 2.0.0
Requires:       crate(signature-3/default) >= 3.0.0
Requires:       crate(spki-0.8/default) >= 0.8.0
Requires:       crate(thiserror-2/default) >= 2.0.20
Requires:       crate(x509-cert-0.2/default) >= 0.2.0
Requires:       crate(x509-cert-0.3/default) >= 0.3.0
Requires:       crate(x509-parser-0.18/default) >= 0.18.0
Requires:       crate(zeroize-1/default) >= 1.7.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "qtls"

%package     -n %{name}+aws-lc-rs
Summary:        Connection-independent QUIC TLS 1.3 state machine for dquic - feature "aws-lc-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aws-lc-rs-1) >= 1.12.0
Requires:       crate(qrustls-0.23/aws-lc-rs) >= 0.23.45
Requires:       crate(qrustls-0.23/std) >= 0.23.45
Provides:       crate(%{pkgname}/aws-lc-rs) = %{version}

%description -n %{name}+aws-lc-rs
This metapackage enables feature "aws-lc-rs" for the Rust qtls crate, by
pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fips
Summary:        Connection-independent QUIC TLS 1.3 state machine for dquic - feature "fips"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aws-lc-rs) = %{version}
Requires:       crate(aws-lc-rs-1/fips) >= 1.12.0
Requires:       crate(qrustls-0.23/fips) >= 0.23.45
Requires:       crate(qrustls-0.23/std) >= 0.23.45
Provides:       crate(%{pkgname}/fips) = %{version}

%description -n %{name}+fips
This metapackage enables feature "fips" for the Rust qtls crate, by pulling
in any additional dependencies needed by that feature.

%package     -n %{name}+ring
Summary:        Connection-independent QUIC TLS 1.3 state machine for dquic - feature "ring" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(qrustls-0.23/ring) >= 0.23.45
Requires:       crate(qrustls-0.23/std) >= 0.23.45
Requires:       crate(ring-0.17/default) >= 0.17.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/ring) = %{version}

%description -n %{name}+ring
This metapackage enables feature "ring" for the Rust qtls crate, by pulling
in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
