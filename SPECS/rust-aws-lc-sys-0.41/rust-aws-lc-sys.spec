# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aws-lc-sys
%global full_version 0.41.0
%global pkgname aws-lc-sys-0.41

Name:           rust-aws-lc-sys-0.41
Version:        0.41.0
Release:        %autorelease
Summary:        Rust crate "aws-lc-sys"
License:        ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)
URL:            https://github.com/aws/aws-lc-rs
#!RemoteAsset:  sha256:1a2f9779ce85b93ab6170dd940ad0169b5766ff848247aff13bb788b832fe3f4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0/default) >= 1.2.26
Requires:       crate(cc-1.0/parallel) >= 1.2.26
Requires:       crate(cmake-0.1/default) >= 0.1.54
Requires:       crate(dunce-1.0/default) >= 1.0.5
Requires:       crate(fs-extra-1.0/default) >= 1.3.0
Provides:       crate(aws-lc-sys) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/all-bindings)
Provides:       crate(%{pkgname}/asan)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/disable-prebuilt-nasm)
Provides:       crate(%{pkgname}/prebuilt-nasm)

%description
It іs based on code from the Google BoringSSL project and the OpenSSL project.
Source code for takopackized Rust crate "aws-lc-sys"

%package     -n %{name}+bindgen
Summary:        AWS-LC is a general-purpose cryptographic library maintained by the AWS Cryptography team for AWS and their customers - feature "bindgen" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(bindgen-0.72/default) >= 0.72.0
Provides:       crate(%{pkgname}/bindgen)
Provides:       crate(%{pkgname}/fips)

%description -n %{name}+bindgen
It іs based on code from the Google BoringSSL project and the OpenSSL project.
This metapackage enables feature "bindgen" for the Rust aws-lc-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "fips" feature.

%package     -n %{name}+ssl
Summary:        AWS-LC is a general-purpose cryptographic library maintained by the AWS Cryptography team for AWS and their customers - feature "ssl"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/all-bindings)
Requires:       crate(%{pkgname}/bindgen)
Provides:       crate(%{pkgname}/ssl)

%description -n %{name}+ssl
It іs based on code from the Google BoringSSL project and the OpenSSL project.
This metapackage enables feature "ssl" for the Rust aws-lc-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
