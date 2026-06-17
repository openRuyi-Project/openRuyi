# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aws-lc-sys
%global full_version 0.35.0
%global pkgname aws-lc-sys-0.35

Name:           rust-aws-lc-sys-0.35
Version:        0.35.0
Release:        %autorelease
Summary:        Rust crate "aws-lc-sys"
License:        ISC AND (Apache-2.0 OR ISC) AND OpenSSL
URL:            https://github.com/aws/aws-lc-rs
#!RemoteAsset:  sha256:b45afffdee1e7c9126814751f88dddc747f41d91da16c9551a0f1e8a11e788a1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.2.26
Requires:       crate(cc-1/parallel) >= 1.2.26
Requires:       crate(cmake-0.1) >= 0.1.54
Requires:       crate(dunce-1) >= 1.0.5
Requires:       crate(fs-extra-1) >= 1.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/all-bindings) = %{version}
Provides:       crate(%{pkgname}/asan) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/prebuilt-nasm) = %{version}

%description
It іs based on code from the Google BoringSSL project and the OpenSSL project.
Source code for takopackized Rust crate "aws-lc-sys"

%package     -n %{name}+bindgen
Summary:        AWS-LC is a general-purpose cryptographic library maintained by the AWS Cryptography team for AWS and their customers - feature "bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bindgen-0.72/default) >= 0.72.0
Provides:       crate(%{pkgname}/bindgen) = %{version}

%description -n %{name}+bindgen
It іs based on code from the Google BoringSSL project and the OpenSSL project.
This metapackage enables feature "bindgen" for the Rust aws-lc-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ssl
Summary:        AWS-LC is a general-purpose cryptographic library maintained by the AWS Cryptography team for AWS and their customers - feature "ssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/all-bindings) = %{version}
Requires:       crate(%{pkgname}/bindgen) = %{version}
Provides:       crate(%{pkgname}/ssl) = %{version}

%description -n %{name}+ssl
It іs based on code from the Google BoringSSL project and the OpenSSL project.
This metapackage enables feature "ssl" for the Rust aws-lc-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
