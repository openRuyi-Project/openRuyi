# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name futures-sink-preview
%global full_version 0.3.0-alpha.15
%global pkgname futures-sink-preview-0.3.0-alpha.15

Name:           rust-futures-sink-preview-0.3.0-alpha.15
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "futures-sink-preview"
License:        MIT OR Apache-2.0
URL:            https://rust-lang-nursery.github.io/futures-rs
#!RemoteAsset:  sha256:f64fa75a0ce02dee949c8c9447abfc117df214054d6e96755d329c9053baf2fd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-channel-preview-0.3.0-alpha.15) >= 0.3.0-alpha.15
Requires:       crate(futures-core-preview-0.3.0-alpha.15) >= 0.3.0-alpha.15

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "futures-sink-preview"

%package     -n %{name}+alloc
Summary:        Asynchronous `Sink` trait for the futures-rs library - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-preview-0.3.0-alpha.15/alloc) >= 0.3.0-alpha.15
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust futures-sink-preview crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nightly
Summary:        Asynchronous `Sink` trait for the futures-rs library - feature "nightly"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-preview-0.3.0-alpha.15/nightly) >= 0.3.0-alpha.15
Provides:       crate(%{pkgname}/nightly) = %{version}

%description -n %{name}+nightly
This metapackage enables feature "nightly" for the Rust futures-sink-preview crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Asynchronous `Sink` trait for the futures-rs library - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(futures-channel-preview-0.3.0-alpha.15/std) >= 0.3.0-alpha.15
Requires:       crate(futures-core-preview-0.3.0-alpha.15/std) >= 0.3.0-alpha.15
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust futures-sink-preview crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%install -a
# Keep prerelease sources separate from the corresponding stable release.
mv %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version} %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
