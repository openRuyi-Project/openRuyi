# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name futures-channel
%global full_version 0.3.32
%global pkgname futures-channel-0.3

Name:           rust-futures-channel-0.3
Version:        0.3.32
Release:        %autorelease
Summary:        Rust crate "futures-channel"
License:        MIT OR Apache-2.0
URL:            https://rust-lang.github.io/futures-rs
#!RemoteAsset:  sha256:07bbe89c50d7a535e539b8c17bc0b49bdb77747034daa8087407d655f3f7cc1d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-core-0.3) >= 0.3.32
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/cfg-target-has-atomic) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "futures-channel"

%package     -n %{name}+alloc
Summary:        Channels for asynchronous communication using futures-rs - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3/alloc) >= 0.3.32
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust futures-channel crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-sink
Summary:        Channels for asynchronous communication using futures-rs - feature "futures-sink" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-sink-0.3) >= 0.3.32
Provides:       crate(%{pkgname}/futures-sink) = %{version}
Provides:       crate(%{pkgname}/sink) = %{version}

%description -n %{name}+futures-sink
This metapackage enables feature "futures-sink" for the Rust futures-channel crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "sink" feature.

%package     -n %{name}+std
Summary:        Channels for asynchronous communication using futures-rs - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(futures-core-0.3/std) >= 0.3.32
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust futures-channel crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
