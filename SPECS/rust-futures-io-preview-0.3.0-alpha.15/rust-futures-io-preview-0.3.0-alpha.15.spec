# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name futures-io-preview
%global full_version 0.3.0-alpha.15
%global pkgname futures-io-preview-0.3.0-alpha.15

Name:           rust-futures-io-preview-0.3.0-alpha.15
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "futures-io-preview"
License:        MIT OR Apache-2.0
URL:            https://rust-lang-nursery.github.io/futures-rs
#!RemoteAsset:  sha256:b24891994ce1445f7e0cd494e4f57fd79f5bd9d37e9cc90a31d109e9a06d9073
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-core-preview-0.3.0-alpha.15) >= 0.3.0-alpha.15

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "futures-io-preview"

%package     -n %{name}+iovec
Summary:        `AsyncRead` and `AsyncWrite` traits for the futures-rs library - feature "iovec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(iovec-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/iovec) = %{version}

%description -n %{name}+iovec
This metapackage enables feature "iovec" for the Rust futures-io-preview crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        `AsyncRead` and `AsyncWrite` traits for the futures-rs library - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/iovec) = %{version}
Requires:       crate(futures-core-preview-0.3.0-alpha.15/std) >= 0.3.0-alpha.15
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust futures-io-preview crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%install -a
# Keep prerelease sources separate from the corresponding stable release.
mv %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version} %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
