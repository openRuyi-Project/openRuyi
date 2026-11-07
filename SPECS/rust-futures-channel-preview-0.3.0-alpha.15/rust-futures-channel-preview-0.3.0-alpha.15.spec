# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name futures-channel-preview
%global full_version 0.3.0-alpha.15
%global pkgname futures-channel-preview-0.3.0-alpha.15

Name:           rust-futures-channel-preview-0.3.0-alpha.15
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "futures-channel-preview"
License:        MIT OR Apache-2.0
URL:            https://rust-lang-nursery.github.io/futures-rs
#!RemoteAsset:  sha256:edf150887ba490560f3d732e479a383ca4b8696af98651806d3f4edc1d968585
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-core-preview-0.3.0-alpha.15) >= 0.3.0-alpha.15

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "futures-channel-preview"

%package     -n %{name}+std
Summary:        Channels for asynchronous communication using futures-rs - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-preview-0.3.0-alpha.15/std) >= 0.3.0-alpha.15
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust futures-channel-preview crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%install -a
# Keep prerelease sources separate from the corresponding stable release.
mv %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version} %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
